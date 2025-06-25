from credle import CredlePreProcessor
import os
preApp = CredlePreProcessor()

cube = preApp.createCube((0,0,0), (5,5,5))

preApp.exportStl( cube, os.path.join( os.path.dirname( __file__), "cube.stl"))
