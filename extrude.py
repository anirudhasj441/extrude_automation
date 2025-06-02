import bpy 
import bmesh
from mathutils import Vector
from enum import Enum
import sys

class Axix(Enum):
    X = 1
    Y = 2
    Z = 3
## end class Axix

def clearAll():
    '''
    clear all the objects present in scene
    '''
    for object in bpy.data.objects:
        bpy.data.objects.remove(object)
## end clearAll()

def importStl( aFilepath: str ):
    '''
    Import the stl file into scene
    @param aFilepath: path of the stl file to be imported
    '''
    bpy.ops.import_mesh.stl( filepath=aFilepath )
## end importStl()

def extrudeObj( aObj: bpy.types.Object, aExtrudeBy: int = 1, 
            aExtrudeAlong: Axix = Axix.Z ):
    '''
    Extrude the object
    @param aObj: the object to be extruded
    '''
    
    # deslect all other object 
    bpy.ops.object.select_all(action="DESELECT")
    
    # select object
    aObj.select_set( True )
    
    # make object active
    bpy.context.view_layer.objects.active = aObj
    
    # open edit mode
    bpy.ops.object.mode_set(mode="EDIT")
    
    # Get BMesh
    bm = bmesh.from_edit_mesh(aObj.data)
    bm.faces.ensure_lookup_table()
    
    # Deselect all faces
    for f in bm.faces:
        f.select = False

    ## Selecting the Farthest Face Along a Given Axis
    maxCenterMedian  = 0

    if Axix.X == aExtrudeAlong:
        maxCenterMedian = max([ f.calc_center_median().x for f in bm.faces ])
    elif Axix.Y == aExtrudeAlong:
        maxCenterMedian = max([ f.calc_center_median().y for f in bm.faces ])
    elif Axix.Z == aExtrudeAlong:
        maxCenterMedian = max([ f.calc_center_median().z for f in bm.faces ])


    for face in bm.faces:
        axisFaceCenterMedianMap = {
            Axix.X: face.calc_center_median().x,
            Axix.Y: face.calc_center_median().y,
            Axix.Z: face.calc_center_median().z
        }

        if axisFaceCenterMedianMap[aExtrudeAlong] == maxCenterMedian:
            face.select = True
            
    bmesh.update_edit_mesh(bpy.context.edit_object.data)

    extrudeValue = (
        aExtrudeBy if Axix.X == aExtrudeAlong else 0,
        aExtrudeBy if Axix.Y == aExtrudeAlong else 0,
        aExtrudeBy if Axix.Z == aExtrudeAlong else 0
    )
    
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={
        "value": extrudeValue
    })
    
    bpy.ops.object.mode_set(mode="OBJECT")
## end extrudeObj()        


def exportStl( aObj: bpy.types.Object, aFilePath: str ):
    '''
    export the given object to give filepath
    '''
    ## deselect all other objects
    bpy.ops.object.select_all(action="DESELECT")

    ## select exporting object
    aObj.select_set( True )

    bpy.context.view_layer.objects.active = aObj

    ## Export the object
    bpy.ops.export_mesh.stl( filepath = aFilePath, use_selection=True )
## end exportStl()

def exportPlane( aObj: bpy.types.Object, aFilePath: str ):
    ## deselect all other objects
    bpy.ops.object.select_all(action="DESELECT")

    ## select exporting object
    aObj.select_set( True )

    bpy.context.view_layer.objects.active = aObj

    bpy.ops.object.mode_set( mode="EDIT")

     # Get BMesh
    bm = bmesh.from_edit_mesh(aObj.data)
    bm.faces.ensure_lookup_table()

    # selecting all faces
    for face in bm.faces:
        face.select = True

    ## Selecting the Farthest Face Along a Given Axis
    maxCenterMedian  = 0

    maxCenterMedian = max([ f.calc_center_median().z for f in bm.faces ])

    # deselct the faces that to be exported currently that along to z axis
    for face in bm.faces:
        if face.calc_center_median().z == maxCenterMedian:
            face.select = False

    ## delete the selected faces
    bpy.ops.mesh.delete( type = 'FACE' )

    ## retun to object mode
    bpy.ops.object.mode_set( mode='OBJECT' )

    ## export the object
    exportStl( aObj, aFilePath )  

    
if __name__ == "__main__":
    try:
        standardArgsCount = 4 ## 4 args are fixed ( blender.exe, --background, 
                              ## -P, python_script )
        standardArgsLastIndex = standardArgsCount - 1

        if len(sys.argv) < standardArgsCount + 2:
            print("Invalid number of arguments.")
            print("Usage: <input_stl_file> <output_stl_file>")
            sys.exit( 1 )

        inputStl = sys.argv[ standardArgsLastIndex + 1 ]
        outStl = sys.argv[ standardArgsLastIndex + 2 ]
        
        # clear all default objects(cube, light camera)
        clearAll()
        
        importStl( inputStl )
        
        obj: bpy.types.Object = bpy.data.objects[ 0 ] ## assuming stl file has only
                                                    ## one mesh object

        # extrudeObj( obj, 5, Axix.Z )

        # exportStl( obj, outStl )

        exportPlane( obj, outStl )

        clearAll()
    
    except Exception as error:
        print( "Something wrong: ",  str(error))
    
    
    
    