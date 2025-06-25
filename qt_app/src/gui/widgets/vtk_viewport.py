from PySide6.QtWidgets import QWidget, QVBoxLayout
from vtk import (
    vtkRenderer, 
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkInteractorStyleTrackballCamera,
    vtkPolyDataMapper,
    vtkCubeSource,
    vtkActor,
    vtkSTLReader,
    vtkActorCollection,
    vtkOrientationMarkerWidget,
    vtkAxesActor
)
import os

from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class VtkViewport( QWidget ):
    mWidget: QVTKRenderWindowInteractor
    mRenderWindow: vtkRenderWindow
    mRenderer: vtkRenderer
    mInteractor: vtkRenderWindowInteractor
    mInteractorStyle: vtkInteractorStyleTrackballCamera
    mAxesActor: vtkAxesActor
    mMarkerWidget: vtkOrientationMarkerWidget

    def __init__( self, aParent = None ):
        super().__init__( aParent )

    def initialize( self ):
        self.mWidget = QVTKRenderWindowInteractor( self )
        self.mRenderWindow = self.mWidget.GetRenderWindow()
        self.mRenderer = vtkRenderer()
        self.mInteractor = self.mRenderWindow.GetInteractor()
        self.mInteractorStyle = vtkInteractorStyleTrackballCamera()
        self.mMarkerWidget = vtkOrientationMarkerWidget()
        self.mAxesActor = vtkAxesActor()

        self.mRenderWindow.AddRenderer( self.mRenderer )
        self.mRenderer.SetBackground(( 0.321, 0.383, 79.535 ))
        self.mInteractor.SetInteractorStyle( self.mInteractorStyle )

        self.mInteractor.Initialize( )

        self.mAxesActor.SetTotalLength( 1, 1, 1 )
        self.mAxesActor.SetShaftTypeToCylinder( )
        self.mAxesActor.SetAxisLabels( 1 )
        self.mAxesActor.SetCylinderRadius( 0.05 )

        self.mMarkerWidget.SetOrientationMarker( self.mAxesActor )
        self.mMarkerWidget.SetInteractor( self.mInteractor )
        self.mMarkerWidget.SetViewport( 0.0, 0.0, 0.2, 0.2 )
        self.mMarkerWidget.SetEnabled( True )
        self.mMarkerWidget.InteractiveOff( )

        layout: QVBoxLayout = QVBoxLayout( self )
        layout.setContentsMargins( 0, 0, 0, 0 )
        layout.addWidget( self.mWidget )
        self.setLayout( layout )

    def clear( self ):
        actors:vtkActorCollection = self.mRenderer.GetActors()
        actors.InitTraversal()

        for _ in range( actors.GetNumberOfItems()):
            actor:vtkActor = actors.GetNextActor()
            self.mRenderer.RemoveActor( actor )


    def drawCube( self ):
        cubeSource: vtkCubeSource = vtkCubeSource()
        cubeSource.SetXLength( 1.0 )
        cubeSource.SetYLength( 1.0 )
        cubeSource.SetZLength( 1.0 )

        cubeSource.SetCenter( 0, 0, 0 )

        cubeSource.Update()

        mapper: vtkPolyDataMapper = vtkPolyDataMapper()
        mapper.SetInputConnection( cubeSource.GetOutputPort())

        actor:vtkActor = vtkActor()
        actor.SetMapper( mapper )

        self.mRenderer.AddActor( actor )
        self.mRenderer.Render() 

    def loadStl( self, aFilePath: str ):
        if not os.path.exists( aFilePath ): return 

        self.clear()

        reader: vtkSTLReader = vtkSTLReader()

        reader.SetFileName( aFilePath )

        mapper: vtkPolyDataMapper = vtkPolyDataMapper()
        mapper.SetInputConnection( reader.GetOutputPort())

        actor: vtkActor = vtkActor()
        actor.SetMapper( mapper )

        self.mRenderer.AddActor( actor )
        self.mRenderer.Render()



