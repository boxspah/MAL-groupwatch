"""
CSC111 Project: Improving Anime Recommendations using
Weighted Graphs and Extended Metadata : Main Window

Module Description:
====================
The module contains the class that sets up the Greeting Window in our application.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Optional, Union
import sys
import GroupWatchSolo
import GroupWatchGroup


class UiMainWindow(object):
    """
    Creates the Greeting Window for our application.

    Instance Attributes:
        - window: Object that initializes the Window
        - ui: Object that initializes the next window based on whether we choose solo or group
        recommendations
        - central_widget: Object upon which we lay upon the rest of our information
        - push_button: A button that leads to solo recommendation page
        - push_button2: A button that leads to group recommendation page
        - label: The heading on top of the screen
        - label2: Heading that labels button that leads to solo recommendation page
        - label3: Heading that labels button that leads to group recommendation page
        - label4: Heading that prompts us to choose a button
        - label5: Information about the app at the bottom of the screen
    """
    window: Optional[QtWidgets.QMainWindow]
    ui: Optional[Union[GroupWatchSolo.Ui_Frame, GroupWatchGroup.Ui_Frame]]
    central_widget: Optional[QtWidgets.QWidget]
    push_button: Optional[QtWidgets.QPushButton]
    push_button2: Optional[QtWidgets.QPushButton]
    label: Optional[QtWidgets.QLabel]
    label2: Optional[QtWidgets.QLabel]
    label3: Optional[QtWidgets.QLabel]
    label4: Optional[QtWidgets.QLabel]
    label5: Optional[QtWidgets.QLabel]

    def __init__(self) -> None:
        """Sets all attributes necessary for MainWindow to None by default."""
        self.window = None
        self.ui = None
        self.central_widget = None
        self.push_button = None
        self.push_button2 = None
        self.label = None
        self.label2 = None
        self.label3 = None
        self.label4 = None
        self.label5 = None
        self.menu_bar = None
        self.status_bar = None

    def open_group(self) -> None:
        """Opens the group recommendation page in our application."""
        self.window = QtWidgets.QFrame()
        self.ui = GroupWatchGroup.Ui_Frame()
        self.ui.setupUi(self.window)
        widget.addWidget(self.window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def open_solo(self) -> None:
        """Opens the solo recommendation page in our application."""
        self.window = QtWidgets.QFrame()
        self.ui = GroupWatchSolo.Ui_Frame()
        self.ui.setupUi(self.window)
        widget.addWidget(self.window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def setup_ui(self, main_window: QtWidgets.QMainWindow) -> None:
        """Sets up the Greeting Window and initializes all the variables
        to create the user interface of the window."""
        main_window.setObjectName("MainWindow")
        main_window.setEnabled(True)
        main_window.resize(800, 600)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(size_policy)
        main_window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        main_window.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        main_window.setAcceptDrops(False)
        main_window.setToolTipDuration(-1)
        main_window.setAccessibleName("")
        main_window.setAutoFillBackground(False)
        main_window.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.push_button = QtWidgets.QPushButton(self.central_widget)
        self.push_button.setGeometry(QtCore.QRect(420, 290, 93, 28))
        self.push_button.setObjectName("push_button")
        self.push_button2 = QtWidgets.QPushButton(self.central_widget)
        self.push_button2.setGeometry(QtCore.QRect(420, 360, 93, 28))
        self.push_button2.setObjectName("push_button2")
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(40, 30, 711, 121))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(self.central_widget)
        self.label2.setGeometry(QtCore.QRect(270, 280, 181, 41))
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.central_widget)
        self.label3.setGeometry(QtCore.QRect(270, 360, 191, 31))
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(self.central_widget)
        self.label4.setEnabled(True)
        self.label4.setGeometry(QtCore.QRect(130, 190, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label4.setFont(font)
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(self.central_widget)
        self.label5.setGeometry(QtCore.QRect(110, 480, 581, 71))
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5.setObjectName("label5")
        main_window.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menu_bar.setObjectName("menu_bar")
        main_window.setMenuBar(self.menu_bar)
        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")
        main_window.setStatusBar(self.status_bar)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        self.push_button2.clicked.connect(self.open_group)
        self.push_button.clicked.connect(self.open_solo)

    def retranslate_ui(self, main_window: QtWidgets.QMainWindow) -> None:
        """Enters the text onto the user interface."""
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "GroupWatch"))
        main_window.setToolTip(_translate("MainWindow", "Hi there!"))
        self.push_button.setText(_translate("MainWindow", "Enter"))
        self.push_button2.setText(_translate("MainWindow", "Enter"))
        self.label.setText(_translate("MainWindow",
                                      "Welcome to GroupWatch, an app that recommends shows based "
                                      "on what you and your buddy have already watched"))
        self.label2.setText(_translate("MainWindow", "Solo watch"))
        self.label3.setText(_translate("MainWindow", "Group watch"))
        self.label4.setText(_translate("MainWindow", "Are you venturing alone or together?"))
        self.label5.setText(_translate("MainWindow",
                                       "Data based on the My Anime List database. " 
                                       "This app was made for the final project of CSC111."))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window1 = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(main_window1)
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window1)
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec_())
