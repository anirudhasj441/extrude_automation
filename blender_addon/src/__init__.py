# __init__.py at root of the addon
bl_info = {
    "name": "Custom STL Tools",
    "author": "Anirudha Jadhav",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > CustomTools",
    "description": "Import/export STL with custom controls",
    "category": "Import-Export",
}

import importlib
from . import main

def register():
    importlib.reload(main)
    main.register()
    main.registerProps()

def unregister():
    main.unregister()
    main.unregisterProps()