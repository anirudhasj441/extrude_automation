# @file export_panel.py
#
# @author Anirudha Jadhav
#

import bpy
from operators.export_operator import ExportOperator

class ExportPanel( bpy.types.Panel ):
    """
    @class ExportPanel
    @brief Creates a panel in the 3D Viewport UI for exporting mesh objects to 
        STL.

    This panel:
    - Appears in the 3D Viewport under the 'CustomTools' tab.
    - Displays a mesh object selector (`stlObject`).
    - Provides a button to trigger STL export using ExportOperator.
    """
    bl_label = "Export"
    bl_idname = "VIEW3D_UI_PT_export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "CustomTools"

    def draw(self, aContext: bpy.types.Context ):
        """
        @brief Draws the UI elements for the export panel.

        @param aContext The current Blender context.
        """
        layout: bpy.types.UILayout | None = self.layout
        layout.prop( aContext.scene, "stlObject")
        layout.operator( ExportOperator.bl_idname, text="Export" )
        