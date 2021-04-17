"""
CSC111 Project: Improving Anime Recommendations using
Weighted Graphs and Extended Metadata : Final Window

Module Description:
====================
The module contains the class that sets up the Final Window that displays the recommendations
in our application.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Optional, Union


class UiForm(object):
    """
     Creates the Final Window for our application that displays the recommendations.

     Instance Attributes:
         - recommendations: List of recommended animes
         - widget: Object upon which we lay the grid for the first five recommendations
         - layout_widget: Object upon which we lay the grid for the second five recommendations
         - grid_layout_1: The grid that holds the labels of our first five recommendations
         - grid_layout_2: The grid that holds the labels of our second five recommendations
         - items: Stores the labels of the recommendations on the list
         - header: Displays the heading on the screen
     """
    widget: Optional[QtWidgets.QWidget]
    layout_widget: Optional[QtWidgets.QWidget]
    grid_layout1: Optional[QtWidgets.QGridLayout]
    grid_layout2: Optional[QtWidgets.QGridLayout]
    items: list[Optional[QtWidgets.QLabel]]
    header: Optional[QtWidgets.QLabel]
    recommendations: list[str]

    def __init__(self, recommendations: list[str]) -> None:
        """Set all attributes necessary for the Final Window to None by default, and stores
         recommendations from previous Window."""
        self.widget = None
        self.layout_widget = None
        self.grid_layout1 = None
        self.grid_layout2 = None
        self.items = [None for _ in range(0, 10)]
        self.header = None
        self.recommendations = recommendations

    def setup_ui(self, form: QtWidgets.QWidget) -> None:
        """Set up the Final Window and initializes all the variables
        to create the user interface of the window."""
        form.setObjectName("Form")
        form.resize(800, 600)
        self.layout_widget = QtWidgets.QWidget(form)
        self.layout_widget.setGeometry(QtCore.QRect(440, 100, 311, 381))
        self.layout_widget.setObjectName("layout_widget")
        self.grid_layout2 = QtWidgets.QGridLayout(self.layout_widget)
        self.grid_layout2.setContentsMargins(0, 0, 0, 0)
        self.grid_layout2.setObjectName("grid_layout2")
        self.items[8] = QtWidgets.QLabel(self.layout_widget)
        self.items[8].setObjectName("item9")
        self.grid_layout2.addWidget(self.items[8], 3, 0, 1, 1)
        self.items[9] = QtWidgets.QLabel(self.layout_widget)
        self.items[9].setObjectName("item10")
        self.grid_layout2.addWidget(self.items[9], 4, 0, 1, 1)
        self.items[6] = QtWidgets.QLabel(self.layout_widget)
        self.items[6].setObjectName("item7")
        self.grid_layout2.addWidget(self.items[6], 1, 0, 1, 1)
        self.items[7] = QtWidgets.QLabel(self.layout_widget)
        self.items[7].setObjectName("item8")
        self.grid_layout2.addWidget(self.items[7], 2, 0, 1, 1)
        self.items[5] = QtWidgets.QLabel(self.layout_widget)
        self.items[5].setObjectName("item6")
        self.grid_layout2.addWidget(self.items[5], 0, 0, 1, 1)
        self.header = QtWidgets.QLabel(form)
        self.header.setGeometry(QtCore.QRect(200, 10, 600, 40))
        self.header.setObjectName("header")
        self.widget = QtWidgets.QWidget(form)
        self.widget.setGeometry(QtCore.QRect(100, 100, 311, 381))
        self.widget.setObjectName("widget")
        self.grid_layout1 = QtWidgets.QGridLayout(self.widget)
        self.grid_layout1.setContentsMargins(0, 0, 0, 0)
        self.grid_layout1.setObjectName("grid_layout1")
        self.items[0] = QtWidgets.QLabel(self.widget)
        self.items[0].setObjectName("item1")
        self.grid_layout1.addWidget(self.items[0], 0, 0, 1, 1)
        self.items[1] = QtWidgets.QLabel(self.widget)
        self.items[1].setObjectName("item2")
        self.grid_layout1.addWidget(self.items[1], 1, 0, 1, 1)
        self.items[2] = QtWidgets.QLabel(self.widget)
        self.items[2].setObjectName("item3")
        self.grid_layout1.addWidget(self.items[2], 2, 0, 1, 1)
        self.items[3] = QtWidgets.QLabel(self.widget)
        self.items[3].setObjectName("item4")
        self.grid_layout1.addWidget(self.items[3], 3, 0, 1, 1)
        self.items[4] = QtWidgets.QLabel(self.widget)
        self.items[4].setObjectName("item5")
        self.grid_layout1.addWidget(self.items[4], 4, 0, 1, 1)

        self.retranslate_ui(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslate_ui(self, form: QtWidgets.QWidget) -> None:
        """Enter the text onto the user interface."""
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Form"))
        for i in range(0, len(self.recommendations)):
            self.items[i].setText(_translate("Form",
                                             str(i + 1) + "." +
                                             self.recommendations[i]))
            self.items[i].setWordWrap(True)
        self.header.setText(_translate("Form",
                                       "<html><head/><body><p><span style=\" "
                                       "font-size:16pt;\">Here's your "
                                       "recommendations!</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form1 = QtWidgets.QWidget()
    recommendations = []
    for i in range(0, 7):
        recommendations.append(str(i))
    ui = UiForm(recommendations)
    ui.setup_ui(form1)
    form1.show()
    sys.exit(app.exec_())
