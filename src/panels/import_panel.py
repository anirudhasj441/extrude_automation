# @file extrude_panel.py
#
# @author Anirudha Jadhav
#

from operators.import_operator import ImportStlOperator
import bpy

class ImportStlPanel( bpy.types.Panel ):
    """
    @class ImportStlPanel
    @brief Creates a UI panel in the 3D Viewport for importing STL files.

    This panel provides:
    - A button to open the file selector and import an STL file into the current
        scene using the custom ImportStlOperator.
    """

    bl_label = "Import STL"
    bl_idname = "VIEW3D_UI_PT_importSTL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "CustomTools"

    def draw(self, aContext: bpy.types.Context ):
        """
        @brief Draws the UI elements for the STL import panel.

        @param aContext The current Blender context.
        """

        layout: bpy.types.UILayout | None = self.layout

        # layout.prop( aContext.scene, "stlFilePath" )
        layout.operator(ImportStlOperator.bl_idname, text="Import" )
    
