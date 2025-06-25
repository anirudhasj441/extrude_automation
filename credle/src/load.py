

from win32com.client import VARIANT, CDispatch
import win32com.client
import os
import pythoncom

pythoncom.CoInitialize()

preApp: CDispatch = win32com.client.Dispatch( "STpre_Bx64net.Application.2025" )


doc = preApp.GetDocument


doc._FlagAsMethod( "CreateCubeModel" )
cube = doc.CreateCubeModel( "cube", 0, 0, 0, 5, 5, 5 )

cube._FlagAsMethod( "SaveStlFile" )
print( os.path.abspath("cube.stl") )

retVale = cube.SaveStlFile( os.path.join(os.path.dirname( __file__ ), "cube1.stl") )

print( retVale )


pythoncom.CoUninitialize()

