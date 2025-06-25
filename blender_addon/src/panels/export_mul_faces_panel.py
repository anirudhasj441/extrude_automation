from operators.export_mul_faces_operator import ExportMulFacesOperator
import bpy
from bpy.types import Panel, Context, UILayout, Object

class ExportMulFacesPanel( Panel ):
    bl_label = "Export Multiple Faces"
    bl_idname = "VIEW3D_PT_export_mul_faces"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "CustomTools"

    def draw(self, aContext: Context):
        layout: UILayout = self.layout

        layout.prop( aContext.scene, "stlObject" )

        obj: Object = aContext.scene.stlObject

        layout.enabled = obj is not None and obj.mode == 'EDIT'

        layout.operator( ExportMulFacesOperator.bl_idname, text="Export Faces" )