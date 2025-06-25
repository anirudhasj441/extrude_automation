from utils.constants import PRE_APP
from typing import Any, Tuple
from win32com.client import CDispatch, Dispatch, VARIANT
import pythoncom

Vector3 = Tuple[ float, float, float ]

class CredlePreProcessor:
    __app: CDispatch
    __doc: Any

    def __init__( self ):
        pythoncom.CoInitialize()
        self.__app = Dispatch( PRE_APP )
        self.__doc = self.__app.GetDocument
        self.__doc._FlagAsMethod("SetUnit")
        self.__doc.SetUnit("length","m")

    def createCube( self, aPos: Vector3, aSize: Vector3 ) -> VARIANT:
        self.__doc._FlagAsMethod("CreateCubeModel")
        cube = self.__doc.CreateCubeModel(
            "cube", 
            aPos[0], 
            aPos[1], 
            aPos[2], 
            aSize[0],
            aSize[1], 
            aSize[2]
        )

        return cube

    def exportStl( self, aObject: VARIANT, aFilePath: str ):
        aObject._FlagAsMethod( "SaveStlFile" )
        ret = aObject.SaveStlFile( aFilePath )
        return ret
    

    def __del__( self ):
        self.quit()

    

    def quit( self ):
        pythoncom.CoUninitialize()