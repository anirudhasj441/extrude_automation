from utils.enums import MeshType
from stl_operator import StlOperator
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
        stl: StlOperator = StlOperator()
        stl.addMesh( MeshType(aContext.scene.mesh ))

        return {'FINISHED'}