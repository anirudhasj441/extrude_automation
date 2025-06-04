# @file extrude_operator.py
#
# @autor Anurudha Jadha
# 

from utils.enums import Axis
from typing import Dict, Tuple
import bpy
import bmesh


class ExtrudeOperator( bpy.types.Operator ):
    """
    @class ExtrudeOperator
    @brief Custom Blender operator to extrude the farthest face of a mesh object
        along a user-defined axis.

    The operator:
    - Selects the farthest face along a given axis (X, Y, or Z).
    - Extrudes that face by a user-defined amount.
    - Uses the `stlObject`, `alongAxis`, and `extrudeBy` scene properties for 
        its operation.
    """
    bl_idname = "custom_tools.extrude"
    bl_label = "Extrude"

    def execute(self, aContext: bpy.types.Context ):
        obj: bpy.types.Object = aContext.scene.stlObject
        axis: Axis = Axis(aContext.scene.alongAxis)
        extrudeBy: int = aContext.scene.extrudeBy

        if not obj: return {'CANCELLED'}

        ## deslect all object
        bpy.ops.object.select_all( action='DESELECT' )

        obj.select_set( True )

        aContext.view_layer.objects.active = obj

        bpy.ops.object.mode_set( mode='EDIT' )

        bm:bmesh.types.BMesh = bmesh.from_edit_mesh( obj.data )
        bm.faces.ensure_lookup_table()

        for face in bm.faces:
            face.select = False

        maxCenterMedian: int = 0

        if Axis.X == axis:
            maxCenterMedian = max([ 
                face.calc_center_median().x for face in bm.faces 
            ])
            
        elif Axis.Y == axis:
            maxCenterMedian = max([ 
                face.calc_center_median().y for face in bm.faces 
            ])
            
        elif Axis.Z == axis:
            maxCenterMedian = max([ 
                face.calc_center_median().z for face in bm.faces 
            ])
            
        for face in bm.faces:
            axisFaceCenterMedianMap: Dict[Axis, int]  = {
                Axis.X: face.calc_center_median().x,
                Axis.Y: face.calc_center_median().y,
                Axis.Z: face.calc_center_median().z
            }

            if axisFaceCenterMedianMap[ axis ] == maxCenterMedian:
                face.select = True

        bmesh.update_edit_mesh( aContext.edit_object.data )

        extrudeValue: Tuple[int] = (
            extrudeBy if Axis.X == axis else 0,
            extrudeBy if Axis.Y == axis else 0,
            extrudeBy if Axis.Z == axis else 0
        )

        bpy.ops.mesh.extrude_region_move( TRANSFORM_OT_translate={
            "value": extrudeValue
        })

        bpy.ops.object.mode_set( mode='OBJECT' )

        return {'FINISHED'}
