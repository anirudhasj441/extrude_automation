from bpy.app.handlers import persistent
import bpy

class ObjectSelectionHandler:
    @staticmethod
    @persistent
    def depsgraph_update( aScene, aDepsgraph ):
        """
        Handler to update the scene when the active object changes.
        This is useful for ensuring that the UI reflects the current selection.
        """
        if not hasattr( aScene, "stlObject" ):
            return
        
        if aScene.stlObject is None:
            if bpy.context.view_layer.objects.active is None: return
                
            # if bpy.context.view_layer.objects.active is not None:
            aScene.stlObject = bpy.context.view_layer.objects.active
            
            return
        
        print("objects",  aScene.objects )
        for obj in aScene.objects:
            print("obj", obj.name, aScene.stlObject.name)

        if aScene.stlObject.name not in aScene.objects:
            aScene.stlObject = None
        



            