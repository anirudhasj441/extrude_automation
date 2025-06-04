# @file export_plane_operator.py
#
# @autor Anurudha Jadha
# 

from utils.enums import Axis, FaceSide
import bpy
import bmesh
from bmesh.types import BMesh
from bpy.types import Operator, Context, Object, Event
from bpy_extras.io_utils import ExportHelper
from typing import List, Dict

class ExportPlaneOperator( Operator, ExportHelper ):
    """
    @class ExportPlaneOperator
    @brief Custom Blender operator to export a single face (plane) from a mesh 
        object.

    The operator:
    - Takes a mesh object from scene properties (`stlObject`)
    - Duplicates it
    - Deletes all faces except the one along the chosen axis and side 
        (`faceToExport`)
    - Exports the remaining face as an STL using ExportHelper
    """
    bl_label = "Export Plane"
    bl_idname = "custom_tools.export_plane"

    filename_ext = ".stl"

    def invoke(self, aContext: Context , aEvent: Event):
        """
        @brief Called when the operator is invoked (e.g., button click).
        Prevents file dialog if no object is selected.

        @param aContext Current Blender context
        @param aEvent UI event
        @return Operator status dict
        """
        obj: Object = aContext.scene.stlObject
        if not obj: return {"CANCELLED"}

        return super().invoke( aContext, aEvent )
        

    def execute(self, aContext: Context ):
        obj: Object = aContext.scene.stlObject
        if not obj: return {"CANCELLED"}

        if not self.filepath or self.filepath.strip() == "": 
            return {"CANCELLED"}
        
        faceToExport: FaceSide = FaceSide(aContext.scene.faceToExport)


        # Deselect all
        bpy.ops.object.select_all(action='DESELECT')

        obj.select_set( True )
        bpy.ops.object.duplicate()
        obj_copy = aContext.selected_objects[0]
        aContext.view_layer.objects.active = obj_copy

        bpy.ops.object.mode_set( mode="EDIT")
        bm: BMesh = bmesh.from_edit_mesh( obj_copy.data )
        bm.faces.ensure_lookup_table()

        for face in bm.faces:
            face.select = True

        negativeSides: List[FaceSide] = [ 
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
        
        axis = axisFaceMap[faceToExport]

        maxCenterMedian: int = 0
        minCenterMedian: int = 0

        if Axis.X == axis:
            maxCenterMedian = max([ 
                face.calc_center_median().x for face in bm.faces 
            ])
            minCenterMedian =  min([ 
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

        for face in bm.faces:
            axisFaceCenterMedianMap: Dict[Axis, int]  = {
                Axis.X: face.calc_center_median().x,
                Axis.Y: face.calc_center_median().y,
                Axis.Z: face.calc_center_median().z
            }

            centerMedian = ( minCenterMedian if faceToExport in 
                    negativeSides else maxCenterMedian )
            
            if axisFaceCenterMedianMap[ axis ] == centerMedian:
                face.select = False

        bpy.ops.mesh.delete( type="FACE" )

        bpy.ops.object.mode_set( mode="OBJECT" )

        bpy.ops.export_mesh.stl( filepath=self.filepath, use_selection=True )

        bpy.data.objects.remove( obj_copy, do_unlink=True )

        return {"FINISHED"}


        

            






        
