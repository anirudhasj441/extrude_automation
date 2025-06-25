# @file extrude_panel.py
#
# @author Anirudha Jadhav
#

import bpy
from operators.extrude_operator import ExtrudeOperator

class ExtrudePanel( bpy.types.Panel ):
    """
    @class ExtrudePanel
    @brief Creates a UI panel in the 3D Viewport for extruding a mesh object 
        along a selected axis.

    This panel:
    - Allows the user to select an STL mesh object from the scene.
    - Provides a dropdown to select the axis along which to extrude.
    - Takes an input value to determine how far to extrude the mesh.
    - Executes the extrusion via a custom operator.
    """

    bl_label = "Extrude"
    bl_idname = "VIEW3D_UI_PT_extrude"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "CustomTools"

    def draw(self, aContext: bpy.types.Context ):
        """
        @brief Draws the UI elements for the extrusion panel.

        @param aContext The current Blender context.
        """
        layout: bpy.types.UILayout | None = self.layout

        layout.prop( aContext.scene, "stlObject" )
        layout.prop( aContext.scene, "alongAxis" )
        layout.prop( aContext.scene, "extrudeBy" )
        layout.operator( ExtrudeOperator.bl_idname, text="Extrude" )
    
