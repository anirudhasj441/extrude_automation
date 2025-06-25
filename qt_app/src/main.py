import sys
import os
sys.path.append( os.path.join(os.path.dirname( __file__ ), "../auto_gen") )

from PySide6.QtWidgets import QApplication
from gui.win_main import WinMain

if __name__ == "__main__":
    app = QApplication( sys.argv )

    window = WinMain( )
    window.show()

    sys.exit( app.exec())