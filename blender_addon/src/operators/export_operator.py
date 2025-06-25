# @file export_operator.py
#
# @autor Anurudha Jadha

from stl_operator import StlOperator
import bpy
from bpy.types import Object, Context, Event
from bpy_extras.io_utils import ExportHelper

class ExportOperator( bpy.types.Operator, ExportHelper ):
    """
    @class ExportOperator
    @brief Custom Blender operator to export a selected mesh object to STL format.

    This operator:
    - Checks if a mesh object is selected in the scene property (`stlObject`)
    - Invokes the file dialog to select export location
    - Exports the selected mesh object as STL using Blender’s built-in `export_mesh.stl`
    """

    bl_idname = "custom_tools.export_stl"
    bl_label = "Export STL"

    filename_ext = ".stl"

    def invoke(self, aContext: Context , aEvent: Event):
        """
        @brief Called when the operator is invoked (e.g., button click).
        Prevents file dialog if no object is selected.

        @param aContext The current context in Blender.
        @param aEvent The UI event that triggered the operator.
        @return A dictionary indicating the result (CANCELLED or run super().invoke).
        """
        obj: Object = aContext.scene.stlObject
        if not obj: return {"CANCELLED"}

        return super().invoke( aContext, aEvent )

    def execute( self, aContext: bpy.types.Context ):
        obj: Object = aContext.scene.stlObject
        filepath = self.filepath
        
        stl: StlOperator = StlOperator()
        stl.exportStl( obj, filepath )
        
        return {"FINISHED"}