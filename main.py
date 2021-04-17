"""
MAL Groupwatch: main
=================================================

Module Description:
This is the main module of the MAL Groupwatch project.
This is the module that you should run to start the program!
"""
import sys

from PyQt5 import QtWidgets
from main_window import UiMainWindow

if __name__ == '__main__':
    # import python_ta.contracts
    # python_ta.contracts.check_all_contracts()

    # import doctest
    # doctest.testmod()
    #
    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 100,
    #     'disable': ['E1136'],
    #     'extra-imports': ['PyQt5', 'sys', 'main_window'],
    # })

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
