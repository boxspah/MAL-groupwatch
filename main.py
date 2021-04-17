"""
MAL Groupwatch: main
=================================================

Module Description:
This is the main module of the MAL Groupwatch project.
This is the module that you should run to start the program!
"""
from PyQt5 import QtWidgets
import sys
from main_window import UiMainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window1 = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(main_window1)
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window1)
    widget.resize(800, 600)
    widget.show()
    ui.widget = widget
    sys.exit(app.exec_())
