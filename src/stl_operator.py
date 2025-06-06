## @file stl_operator.py
##
## @author Anurudha Jadha
##

from utils.enums import Axis, FaceSide
from utils.helper_functions import clearAll
from utils.enums import MeshType
import bpy
from bpy.types import Object
import bmesh
from bmesh.types import BMesh

class StlOperator:
    """
    Base class for STL operators.
    """

    def importStl( self, aFilepath: str):
        """
        Import an STL file into the current Blender context.
        """
        if ( not aFilepath or 
            aFilepath.strip() == ""): return
        
        clearAll()

        bpy.ops.import_mesh.stl(filepath=aFilepath)

    def addMesh( self, aMesh: MeshType ):
        """
        Add a mesh to the current Blender context based on the specified mesh type.
        """
        if aMesh == MeshType.PLANE:
            bpy.ops.mesh.primitive_plane_add(
                size=2, enter_editmode=False, align='WORLD', 
                location=(0, 0, 0)
            )

        elif aMesh == MeshType.CUBE:
            bpy.ops.mesh.primitive_cube_add(
                size=2, enter_editmode=False, align='WORLD', 
                location=(0, 0, 0)
            )

        elif aMesh == MeshType.CYLINDER:
            bpy.ops.mesh.primitive_cylinder_add(
                radius=2, enter_editmode=False, align='WORLD', 
                location=(0, 0, 0)
            )

        elif aMesh == MeshType.CONE:
            bpy.ops.mesh.primitive_cone_add(
                radius1=1, depth=2, enter_editmode=False, align='WORLD', 
                location=(0, 0, 0)
            )

        elif aMesh == MeshType.SPHERE:
            bpy.ops.mesh.primitive_uv_sphere_add(
                radius=1, enter_editmode=False, align='WORLD', 
                location=(0, 0, 0)
            )

    def exportStl( self, aObj: Object, aFilepath: str):
        """
        Export the given object as an STL file.
        """

        if not aFilepath or aFilepath.strip() == "":
            return
        
        if not aObj or not isinstance(aObj, Object):
            return

        ## deselect all objects
        bpy.ops.object.select_all(action='DESELECT')

        ## select the object to export
        aObj.select_set(True)
        bpy.context.view_layer.objects.active = aObj

        ## export the object as STL
        bpy.ops.export_mesh.stl(
            filepath=aFilepath,
            use_selection=True
        )

    def extrudeStl( self, aObj: Object, aAlongAxix: Axis, aExtrudeBy: int ):
        if not aObj or not isinstance(aObj, Object):
            return
        
        ## deselect all objects and select the object to extrude
        bpy.ops.object.select_all(action='DESELECT')
        aObj.select_set(True)
        bpy.context.view_layer.objects.active = aObj

        ## enamble edit mode
        bpy.ops.object.mode_set(mode='EDIT')

        bm: BMesh = bmesh.from_edit_mesh(aObj.data)
        bm.faces.ensure_lookup_table()

        ## Deselect all faces
        for face in bm.faces:
            face.select_set( False )

        ## Find the maximum center median based on the axis
        maxCenterMedian: float = 0.0

        if aAlongAxix == Axis.X:
            maxCenterMedian = max([ 
                face.calc_center_median().x for face in bm.faces 
            ])
        elif aAlongAxix == Axis.Y:
            maxCenterMedian = max([ 
                face.calc_center_median().y for face in bm.faces 
            ])
        elif aAlongAxix == Axis.Z:
            maxCenterMedian = max([ 
                face.calc_center_median().z for face in bm.faces 
            ])

        ## Select faces to extrude
        for face in bm.faces:
            axisFaceCenterMedianMap: dict[Axis, float] = {
                Axis.X: face.calc_center_median().x,
                Axis.Y: face.calc_center_median().y,
                Axis.Z: face.calc_center_median().z
            }

            if axisFaceCenterMedianMap[aAlongAxix] == maxCenterMedian:
                face.select_set(True)

        bmesh.update_edit_mesh(aObj.data)

        ## Extrude the selected faces
        extrudeValue: tuple[int, int, int] = (
            aExtrudeBy if aAlongAxix == Axis.X else 0,
            aExtrudeBy if aAlongAxix == Axis.Y else 0,
            aExtrudeBy if aAlongAxix == Axis.Z else 0
        )

        bpy.ops.mesh.extrude_region_move(
            TRANSFORM_OT_translate={
                "value": extrudeValue
            }
        )

        ## Switch back to object mode
        bpy.ops.object.mode_set(mode='OBJECT')

    def exportFace( self, aObj: Object, aFaceSide: FaceSide, aFilepath: str):
        """
        Export the specified face side of the object as an STL file.
        """
        if not aObj or not isinstance(aObj, Object):
            return

        ## duplicate the object to avoid modifying the original
        obj_copy = aObj.copy()
        obj_copy.data = aObj.data.copy()
        bpy.context.collection.objects.link(obj_copy)

        ## deselect all objects
        bpy.ops.object.select_all(action='DESELECT')

        ## select the object to export
        bpy.context.view_layer.objects.active = obj_copy
        obj_copy.select_set(True)

        ## switch to edit mode
        bpy.ops.object.mode_set(mode='EDIT')

        bm: BMesh = bmesh.from_edit_mesh(obj_copy.data)
        bm.faces.ensure_lookup_table()

        ## Select all faces
        for face in bm.faces:
            face.select_set( True )

        negativeSides: list[FaceSide] = [
            FaceSide.BACK,
            FaceSide.LEFT,
            FaceSide.BOTTOM
        ]

        axisFaceMap = {
            FaceSide.FRONT: Axis.X,
            FaceSide.BACK: Axis.X,
            FaceSide.LEFT: Axis.Y,
            FaceSide.RIGHT: Axis.Y,
            FaceSide.TOP: Axis.Z,
            FaceSide.BOTTOM: Axis.Z
        }

        axis = axisFaceMap[aFaceSide]

        maxCenterMedian: int = 0
        minCenterMedian: int = 0

        if Axis.X == axis:
            maxCenterMedian = max([ 
                face.calc_center_median().x for face in bm.faces 
            ])
            minCenterMedian = min([ 
                face.calc_center_median().x for face in bm.faces 
            ])
        elif Axis.Y == axis:
            maxCenterMedian = max([ 
                face.calc_center_median().y for face in bm.faces 
            ])
            minCenterMedian = min([ 
                face.calc_center_median().y for face in bm.faces 
            ])
        elif Axis.Z == axis:
            maxCenterMedian = max([ 
                face.calc_center_median().z for face in bm.faces 
            ])
            minCenterMedian = min([ 
                face.calc_center_median().z for face in bm.faces 
            ])
        
        ## Deselect faces that to be exported
        for face in bm.faces:
            axisFaceCenterMedianMap: dict[Axis, float] = {
                Axis.X: face.calc_center_median().x,
                Axis.Y: face.calc_center_median().y,
                Axis.Z: face.calc_center_median().z
            }

            centerMedian = ( minCenterMedian if aFaceSide in negativeSides 
                    else maxCenterMedian )

            if axisFaceCenterMedianMap[ axis ] == centerMedian:
                face.select_set( False )

        ## delete the selected faces
        bpy.ops.mesh.delete( type='FACE' )

        bpy.ops.object.mode_set( mode='OBJECT' )

        self.exportStl( obj_copy, aFilepath )

        ## remove the copied object from the scene
        bpy.data.objects.remove( obj_copy, do_unlink=True )

    def exportMulFaces( self, aObj: Object, aFilepath: str):
        """
        Export multiple selected faces of the object as STL files.
        """
        if not aObj or not isinstance(aObj, Object):
            return

        bm: BMesh = bmesh.from_edit_mesh(aObj.data)

        selected_faces = [ face.calc_center_median() for face in bm.faces if face.select ]

        ## back to object mode
        bpy.ops.object.mode_set(mode='OBJECT')

        if len(selected_faces) == 0:
            print("No faces selected")
            return

        ## duplicate the object to avoid modifying the original        
        obj_copy = aObj.copy()
        obj_copy.data = aObj.data.copy()
        bpy.context.collection.objects.link(obj_copy)

        export_objects = []

        for faceCenter in selected_faces:
            ## deselect all objects
            bpy.ops.object.select_all(action='DESELECT')

            ## select the object to export
            bpy.context.view_layer.objects.active = obj_copy
            obj_copy.select_set(True)

            ## switch to edit mode
            bpy.ops.object.mode_set(mode='EDIT')

            bm_copy: BMesh = bmesh.from_edit_mesh(obj_copy.data)
            bm_copy.faces.ensure_lookup_table()

            ## Deselect all faces
            for face in bm_copy.faces:
                face.select_set( faceCenter == face.calc_center_median())

            bmesh.update_edit_mesh(obj_copy.data)

            ## separate the selected face into a new object
            bpy.ops.mesh.separate(type='SELECTED')

            bpy.ops.object.mode_set(mode='OBJECT')

            new_object = [ 
                obj for obj in bpy.context.selected_objects if obj != obj_copy 
            ][-1]

            export_objects.append(new_object)

        for i, obj in enumerate(export_objects, start=1):
            filename = f"{aFilepath}/exported_face_{i}.stl"

            self.exportStl(obj, filename)

        ## remove the copied object from the scene
        bpy.data.objects.remove(obj_copy, do_unlink=True)
    