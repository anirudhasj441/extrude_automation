from operators.add_mesh_operator import AddMeshOperator
import bpy
from bpy.types import Panel, Context, UILayout


class AddMeshPanel( Panel ):
    bl_label = "Add Mesh"
    bl_idname = "VIEW3D_UI_PT_add_mesh"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "CustomTools"

    def draw( self, aContex: Context ):
        layout: UILayout = self.layout

        layout.prop( aContex.scene, "mesh")
        layout.operator( AddMeshOperator.bl_idname, text="Add Mesh" )

    
