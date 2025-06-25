from utils.enums import Axis
from dialog_extrude_inp_ui import Ui_ExtrudeInpDialog

from PySide6.QtWidgets import QDialog, QWidget

class DialogExtrudeInp( QDialog ):
    __axis: Axis
    def __init__( self, aParent: QWidget ):
        super().__init__( aParent )

        self.ui = Ui_ExtrudeInpDialog()
        self.ui.setupUi( self )

        self.ui.cmb_extrudeAxis.addItems([
            axis.name for axis in Axis
        ])

    def axis( self ):
        value = self.ui.cmb_extrudeAxis.currentText()
        return Axis[ value ]



    


    