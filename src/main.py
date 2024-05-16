"""
    @author rmyazdi
    Main module,
    initiates the timer and application and starts the
    program.
"""

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
import view

if __name__ == "__main__":

    app = QApplication([])
    app.setWindowIcon(QIcon("./img/icon_2.jpeg"))
    window = view.Window()
    window.show()

    sys.exit(app.exec())
