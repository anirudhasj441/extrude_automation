import bpy
from bpy.types import Operator, Context

class AddMeshOperator(Operator):
    bl_label = "Add Mesh"
    bl_idname = "custom_tools.add_mesh"

    def execute(self, aContext: Context) -> set:
        """
        @brief Adds a new mesh object to the scene.
        
        This operator creates a new mesh object with a default cube mesh and adds it to the current scene.
        """
        
        if aContext.scene.mesh == "PLANE":
            bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0))
        elif aContext.scene.mesh == "CUBE":
            bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0))
        elif aContext.scene.mesh == "CYLINDER":
            bpy.ops.mesh.primitive_cylinder_add(radius=2, enter_editmode=False, align='WORLD', location=(0, 0, 0))
        elif aContext.scene.mesh == "CONE":
            bpy.ops.mesh.primitive_cone_add(radius1=1, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 0))
        elif aContext.scene.mesh == "SPHERE":
            bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0))

        return {'FINISHED'}