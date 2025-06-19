from enum import Enum
from bpy.types import Object
import sys
import bpy 


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

def scaleStl( aObj: Object, aScaleBy: float ):
    bpy.ops.object.mode_set( mode="OBJECT" )

    ## deselect all
    bpy.ops.object.select_all( action="DESELECT" )
    
    ## select obj which to de scale
    aObj.select_set( True )

    ## scale with all axes by aScaleBy value
    bpy.ops.transform.resize( value=(aScaleBy, aScaleBy, aScaleBy))
## end scaleStl()

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





if __name__ == "__main__":
    try:
        standardArgsCount = 4 ## 4 args are fixed ( blender.exe, --background, 
                              ## -P, python_script )

        standardArgsLastIndex = standardArgsCount - 1

        if len( sys.argv ) < standardArgsCount + 2:
            print("Invalid number of arguments.")
            print("Usage: <input_stl_file> <output_stl_file>")
            sys.exit( 1 )

        inputStl = sys.argv[ standardArgsLastIndex + 1 ]
        outStl = sys.argv[ standardArgsLastIndex + 2 ]

        clearAll()

        importStl( inputStl )

        obj: Object = bpy.data.objects[ 0 ] ## assuming stl contains only one 
                                            ## object

        scaleStl( obj, 0.01 )

        exportStl( obj, outStl )

    except Exception as e:
        print( "Something wrong: ", e )


