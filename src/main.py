'''
@file main.py

@author Anirudha Jadhav

'''

import bpy 
import sys
import os

# Get the directory where main.py is located
current_dir = os.path.dirname(__file__)

# Add the project root (src/) to sys.path
if current_dir not in sys.path:
    sys.path.append(current_dir)
    
# My Imports
from utils.enums import Axis, FaceSide, MeshType
from panels.import_panel import ImportStlPanel
from panels.extrude_panel import ExtrudePanel
from operators.import_operator import ImportStlOperator
from operators.extrude_operator import ExtrudeOperator
from panels.export_panel import ExportPanel
from operators.export_operator import ExportOperator
from panels.export_plane_panel import ExportPlanePanel
from operators.export_plane_operator import ExportPlaneOperator
from operators.add_mesh_operator import AddMeshOperator
from panels.add_mesh_panel import AddMeshPanel

## registering props
def registerProps():
    bpy.types.Scene.stlObject = bpy.props.PointerProperty( 
        name="Mesh Object", 
        type=bpy.types.Object,
        poll= lambda self, obj: obj.type == "MESH"
    )

    bpy.types.Scene.alongAxis = bpy.props.EnumProperty( 
        name="Along Axix",
        items = [
            ( Axis.X.value, 'X Axis', 'X Axis' ),
            ( Axis.Y.value, 'Y Axis', 'Y Axis' ),
            ( Axis.Z.value, 'Z Axis', 'Z Axis' )
        ],
        
        default = Axis.Z.value
    )

    bpy.types.Scene.extrudeBy = bpy.props.IntProperty( 
        name="extride by"
    )

    bpy.types.Scene.faceToExport = bpy.props.EnumProperty( 
        name="Face to export",
        items = [
            ( FaceSide.FRONT.value, "Front", "Front" ),
            ( FaceSide.BACK.value, "Back", "Back" ),
            ( FaceSide.TOP.value, "Top", "Top" ),
            ( FaceSide.BOTTOM.value, "Bottom", "Bottom" ),
            ( FaceSide.LEFT.value, "Left", "Left" ),
            ( FaceSide.RIGHT.value, "Right", "Right" ),
        ],
        
        default = FaceSide.FRONT.value
    )

    bpy.types.Scene.mesh = bpy.props.EnumProperty(
        name="Add Mesh",
        items=[
            ( MeshType.PLANE.value, "PLANE", "PLANE" ),
            ( MeshType.CUBE.value, "CUBE", "CUBE" ),
            ( MeshType.CYLINDER.value, "CYLINDER", "CYLINDER" ),
            ( MeshType.CONE.value, "CONE", "CONE" ),
            ( MeshType.SPHERE.value, "SPHERE", "SPHERE" )
        ],
        default=MeshType.PLANE.value
    )



## registering Panels and operators
def register():
    bpy.utils.register_class( ImportStlPanel )
    bpy.utils.register_class( ImportStlOperator )
    bpy.utils.register_class( ExtrudePanel )
    bpy.utils.register_class( ExtrudeOperator )
    bpy.utils.register_class( ExportPanel )
    bpy.utils.register_class( ExportOperator )
    bpy.utils.register_class( ExportPlanePanel )
    bpy.utils.register_class( ExportPlaneOperator )
    bpy.utils.register_class( AddMeshPanel )
    bpy.utils.register_class( AddMeshOperator )


## unregistering props
def unregisterProps():
    del bpy.types.Scene.stlObject
    del bpy.types.Scene.alongAxis
    del bpy.types.Scene.extrudeBy
    del bpy.types.Scene.faceToExport
    del bpy.types.Scene.mesh

## unregistering Panels and operators
def unregister():
    bpy.utils.unregister_class( ImportStlPanel )
    bpy.utils.unregister_class( ImportStlOperator )
    bpy.utils.unregister_class( ExtrudePanel )
    bpy.utils.unregister_class( ExtrudeOperator )
    bpy.utils.unregister_class( ExportPanel )
    bpy.utils.unregister_class( ExportOperator )
    bpy.utils.unregister_class( ExportPlanePanel )
    bpy.utils.unregister_class( ExportPlaneOperator )
    bpy.utils.unregister_class( AddMeshPanel )
    bpy.utils.unregister_class( AddMeshOperator )

if __name__ == "__main__":
    register()
    registerProps()
    pass
    
