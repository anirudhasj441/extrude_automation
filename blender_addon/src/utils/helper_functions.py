import bpy

def clearAll():
    '''
    clear all the objects present in scene
    '''
    for object in bpy.data.objects:
        bpy.data.objects.remove(object)
## end clearAll()

