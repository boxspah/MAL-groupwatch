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
import solo_window
import group_window

class UiForm(object):
    """
     Creates the Final Window for our application that displays the recommendations.

     Instance Attributes:

         - widget: Object upon which we lay the grid for the first five recommendations
         - layout_widget: Object upon which we lay the grid for the second five recommendations
         - grid_layout_1: The grid that holds the labels of our first five recommendations
         - grid_layout_2: The grid that holds the labels of our second five recommendations
         - item1: Displays the first recommendations on the list, if there are that many.
         - item2: Displays the second recommendations on the list, if there are that many.
         - item3: Displays the third recommendations on the list, if there are that many.
         - item4: Displays the fourth recommendations on the list, if there are that many.
         - item5: Displays the fifth recommendations on the list, if there are that many.
         - item6: Displays the sixth recommendations on the list, if there are that many.
         - item7: Displays the seventh recommendations on the list, if there are that many.
         - item8: Displays the eighth recommendations on the list, if there are that many.
         - item9: Displays the ninth recommendations on the list, if there are that many.
         - item10: Displays the tenth recommendations on the list, if there are that many.
         - header: Displays the heading on the screen
     """
    widget: Optional[QtWidgets.QWidget]
    layout_widget: Optional[QtWidgets.QWidget]
    grid_layout1: Optional[QtWidgets.QGridLayout]
    grid_layout2: Optional[QtWidgets.QGridLayout]
    item1: Optional[QtWidgets.QLabel]
    item2: Optional[QtWidgets.QLabel]
    item3: Optional[QtWidgets.QLabel]
    item4: Optional[QtWidgets.QLabel]
    item5: Optional[QtWidgets.QLabel]
    item6: Optional[QtWidgets.QLabel]
    item7: Optional[QtWidgets.QLabel]
    item8: Optional[QtWidgets.QLabel]
    item9: Optional[QtWidgets.QLabel]
    item10: Optional[QtWidgets.QLabel]
    header: Optional[QtWidgets.QLabel]

    def __init__(self) -> None:
        """Set all attributes necessary for MainWindow to None by default."""
        self.widget = None
        self.layout_widget = None
        self.grid_layout1 = None
        self.grid_layout2 = None
        self.item1 = None
        self.item2 = None
        self.item3 = None
        self.item4 = None
        self.item5 = None
        self.item6 = None
        self.item7 = None
        self.item8 = None
        self.item9 = None
        self.item10 = None
        self.header = None

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
        self.item9 = QtWidgets.QLabel(self.layout_widget)
        self.item9.setObjectName("item9")
        self.grid_layout2.addWidget(self.item9, 3, 0, 1, 1)
        self.item10 = QtWidgets.QLabel(self.layout_widget)
        self.item10.setObjectName("item10")
        self.grid_layout2.addWidget(self.item10, 4, 0, 1, 1)
        self.item7 = QtWidgets.QLabel(self.layout_widget)
        self.item7.setObjectName("item7")
        self.grid_layout2.addWidget(self.item7, 1, 0, 1, 1)
        self.item8 = QtWidgets.QLabel(self.layout_widget)
        self.item8.setObjectName("item8")
        self.grid_layout2.addWidget(self.item8, 2, 0, 1, 1)
        self.item6 = QtWidgets.QLabel(self.layout_widget)
        self.item6.setObjectName("item6")
        self.grid_layout2.addWidget(self.item6, 0, 0, 1, 1)
        self.header = QtWidgets.QLabel(form)
        self.header.setGeometry(QtCore.QRect(200, 10, 600, 40))
        self.header.setObjectName("header")
        self.widget = QtWidgets.QWidget(form)
        self.widget.setGeometry(QtCore.QRect(100, 100, 311, 381))
        self.widget.setObjectName("widget")
        self.grid_layout1 = QtWidgets.QGridLayout(self.widget)
        self.grid_layout1.setContentsMargins(0, 0, 0, 0)
        self.grid_layout1.setObjectName("grid_layout1")
        self.item1 = QtWidgets.QLabel(self.widget)
        self.item1.setObjectName("item1")
        self.grid_layout1.addWidget(self.item1, 0, 0, 1, 1)
        self.item2 = QtWidgets.QLabel(self.widget)
        self.item2.setObjectName("item2")
        self.grid_layout1.addWidget(self.item2, 1, 0, 1, 1)
        self.item3 = QtWidgets.QLabel(self.widget)
        self.item3.setObjectName("item3")
        self.grid_layout1.addWidget(self.item3, 2, 0, 1, 1)
        self.item4 = QtWidgets.QLabel(self.widget)
        self.item4.setObjectName("item4")
        self.grid_layout1.addWidget(self.item4, 3, 0, 1, 1)
        self.item5 = QtWidgets.QLabel(self.widget)
        self.item5.setObjectName("item5")
        self.grid_layout1.addWidget(self.item5, 4, 0, 1, 1)

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form: QtWidgets.QWidget):
        """Enter the text onto the user interface."""
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Form"))
        self.item9.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" "
                                      "font-size:16pt;\">9. " "</span></p></body></html>"))
        self.item10.setText(_translate("Form",
                                       "<html><head/><body><p><span style=\" "
                                       "font-size:16pt;\">10. " "</span></p></body></html>"))
        self.item7.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" "
                                      "font-size:16pt;\">7. " "</span></p></body></html>"))
        self.item8.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" "
                                      "font-size:16pt;\">8. " "</span></p></body></html>"))
        self.item6.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" "
                                      "font-size:16pt;\">6. " "</span></p></body></html>"))
        self.header.setText(_translate("Form",
                                       "<html><head/><body><p><span style=\" "
                                       "font-size:16pt;\">Here's your "
                                       "recommendations!</span></p></body></html>"))
        self.item1.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" "
                                      "font-size:16pt;\">1. " "</span></p></body></html>"))
        self.item2.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" "
                                      "font-size:16pt;\">2. " "</span></p></body></html>"))
        self.item3.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" "
                                      "font-size:16pt;\">3. " "</span></p></body></html>"))
        self.item4.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" "
                                      "font-size:16pt;\">4. " "</span></p></body></html>"))
        self.item5.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" "
                                      "font-size:16pt;\">5. " "</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form1 = QtWidgets.QWidget()
    ui = UiForm()
    ui.setup_ui(form1)
    form1.show()
    sys.exit(app.exec_())
