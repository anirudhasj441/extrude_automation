
# @file import_operator.py
#
# @autor Anurudha Jadha
# 


from utils.helper_functions import *
from bpy_extras.io_utils import ImportHelper
import bpy

class ImportStlOperator( bpy.types.Operator, ImportHelper ):
    """
    @class ImportStlOperator
    @brief Operator for importing STL files through the Blender UI.

    This class extends Blender's built-in Operator and ImportHelper to provide a file browser
    and import an STL file into the scene using bpy.ops.import_mesh.stl.
    
    @note This operator clears the current scene before importing.
    """

    bl_idname = "custom_tools.import_stl"
    bl_label = "Import STL"
    
    filename_ext = ".stl"
    
    def execute(self, aContext: bpy.types.Context ):
        if ( not self.filepath or 
            self.filepath.strip() == ""): return {'CANCELLED'}
        
        clearAll()
        bpy.ops.import_mesh.stl( filepath = self.filepath )
    
        return {'FINISHED'}
