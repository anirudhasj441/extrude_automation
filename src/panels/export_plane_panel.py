# @file export_plane_panel.py
#
# @author Anirudha Jadhav
#

from operators.export_plane_operator import ExportPlaneOperator
from bpy.types import (
    Panel,
    Context,
    UILayout
)

class ExportPlanePanel( Panel ):
    """
    @class ExportPlanePanel
    @brief Creates a panel in the 3D Viewport UI for exporting a specific face of a mesh object.

    This panel:
    - Allows the user to select a mesh object from the scene.
    - Lets the user choose a face direction to export.
    - Provides a button to export only the selected face of the object as an STL file.
    """
    bl_label = "Export Plane"
    bl_idname = "VIEW3D_UI_PT_export_plane"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "CustomTools"

    def draw(self, aContex: Context):
        """
        @brief Draws the UI elements for the export plane panel.

        @param aContex The current Blender context.
        """
        layout: UILayout | None = self.layout
        layout.prop( aContex.scene, "stlObject")
        layout.prop( aContex.scene, "faceToExport" )
        layout.operator( ExportPlaneOperator.bl_idname, text="Export" )
