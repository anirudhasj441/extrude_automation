from stl_operator import StlOperator

import bpy
from bpy.types import Operator, Context, UILayout
import bmesh
from bmesh.types import BMesh

class ExportMulFacesOperator(Operator):
    bl_idname = "custom_tools.export_mul_faces"
    bl_label = "Export Multiple Faces"

    directory: bpy.props.StringProperty(
        name="Directory",
        description="Directory to export the selected faces",
        subtype='DIR_PATH'
    ) # type: ignore

    def invoke(self, aContext: Context, aEvent):
        aContext.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, aContext: Context) -> set:
        stl: StlOperator = StlOperator()
        stl.exportMulFaces( aContext.scene.stlObject, self.directory )
        # # Logic to export multiple faces goes here
        # # This is a placeholder for the actual implementation

        # ## get the selected faces
        # bm: BMesh = bmesh.from_edit_mesh(aContext.object.data)

        # bm.faces.ensure_lookup_table()

        # selected_faces = [ face.calc_center_median() for face in bm.faces if face.select ]

        # if len(selected_faces) == 0:
        #     self.report({'WARNING'}, "No faces selected")
        #     return {'CANCELLED'}

        # ## clone the object
        # bpy.ops.object.mode_set(mode='OBJECT')

        # obj_copy = aContext.scene.stlObject.copy()

        # obj_copy.data = aContext.scene.stlObject.data.copy()

        # aContext.collection.objects.link(obj_copy)



        # export_objects = []

        # for faceCenter in selected_faces:
        #     ## select the faces in the cloned object
        #     bpy.ops.object.select_all(action='DESELECT')

        #     obj_copy.select_set(True)
        #     aContext.view_layer.objects.active = obj_copy
        #     bpy.ops.object.mode_set(mode='EDIT')
        #     bm_copy: BMesh = bmesh.from_edit_mesh(obj_copy.data)
        #     bm_copy.faces.ensure_lookup_table()

        #     for face in bm_copy.faces:
        #         face.select_set( faceCenter == face.calc_center_median())

        #     bmesh.update_edit_mesh( obj_copy.data )

        #     bpy.ops.mesh.separate(type='SELECTED')
            
        #     bpy.ops.object.mode_set(mode='OBJECT')
        #     new_object = [ 
        #         obj for obj in aContext.selected_objects if obj != obj_copy 
        #     ][-1]
        #     export_objects.append(new_object)

        # print(f"Exporting {len(export_objects)} objects...")
        
        # for i, obj in enumerate(export_objects, start=1):
        #     bpy.ops.object.select_all(action='DESELECT')

        #     obj.select_set(True)
        #     aContext.view_layer.objects.active = obj

        #     bpy.ops.export_mesh.stl(
        #         filepath=f"{self.directory}/exported_face_{i}.stl",
        #         use_selection=True
        #     )

        # # remove the cloned object and the split objects
        # for obj in export_objects:
        #     bpy.data.objects.remove(obj, do_unlink=True)

        # bpy.data.objects.remove(obj_copy, do_unlink=True)

        return {'FINISHED'}
