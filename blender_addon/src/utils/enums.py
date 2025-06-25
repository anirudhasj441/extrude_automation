from enum import Enum

class Axis( Enum ):
    X = 'X'
    Y = 'Y'
    Z = 'Z'

class MeshType( Enum ):
    CUBE = "CUBE"
    CYLINDER = "CYLINDER"
    PLANE = "PLANE"
    SPHERE = "SPHERE"
    CONE = "CONE"
    
class FaceSide( Enum ):
    FRONT = "FRONT"
    BACK = "BACK"
    TOP = "TOP"
    BOTTOM = "BOTTOM"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

