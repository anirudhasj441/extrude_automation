# @file export_plane_operator.py
#
# @autor Anurudha Jadha
# 

from stl_operator import StlOperator
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
        stl: StlOperator = StlOperator()
        stl.exportFace( 
            aContext.scene.stlObject,
            FaceSide(aContext.scene.faceToExport),
            self.filepath
        )

        return {"FINISHED"}


        

            






        
