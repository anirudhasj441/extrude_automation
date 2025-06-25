from gui.widgets.vtk_viewport import VtkViewport
from gui.dialogs.dialog_extrude_inp import DialogExtrudeInp
from PySide6.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QVBoxLayout,
    QFileDialog,
    QDialog
)
from PySide6.QtCore import QTimer
from win_main_ui import Ui_WinMain


class WinMain( QMainWindow ):
    mViewPort: VtkViewport

    def __init__( self, aParent: QWidget = None ):
        super().__init__( aParent )

        self.ui = Ui_WinMain()
        self.ui.setupUi( self )

        QTimer.singleShot( 0, self.__onMounted )

    def __onMounted( self ):
        self.mViewPort = VtkViewport( self.ui.centralwidget )

        layout: QVBoxLayout = self.ui.centralwidget.layout()

        if layout is None:
            layout = QVBoxLayout()
            self.ui.centralwidget.setLayout( layout )

        layout.addWidget( self.mViewPort )

        self.mViewPort.initialize()
        self.mViewPort.drawCube()

    def actionImportStl_triggerd( self ):
        fileName = QFileDialog.getOpenFileName( 
            self, "Import STL", "", "STL Files (*.stl)"
        )

        if not fileName:
            return
        
        print( fileName )
        self.mViewPort.loadStl( fileName[0] )

    def actionExtrude_triggered( self ):
        dig: DialogExtrudeInp = DialogExtrudeInp( self )
        
        if dig.exec() != 1: return

        print( "Select axis: ", dig.axis())




