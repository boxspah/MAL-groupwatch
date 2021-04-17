"""
Main module for MAL-groupwatch
"""
from PyQt5 import QtWidgets
import sys
from main_window import UiMainWindow
from load_graph import load_graph

if __name__ == '__main__':
    # graph = load_graph("data/rating.csv", "data/anime.csv")

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
