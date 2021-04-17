"""
CSC111 Project: Improving Anime Recommendations using
Weighted Graphs and Extended Metadata : Solo Recommendation Window

Module Description:
====================
The module contains the class that sets up the window where a single user makes their inputs.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Optional
import ui_functions
from recommendations_output import UiForm

class UiFrame(object):
    """
    Create the window where a single user can input data.

    Instance Attributes:
        - window: Initializing the window that displays the recommendations
        - ui: Initializing the user interface for the window that displays the recommendations
        - widget: A stack of widgets that allows us to switch screens without opening new windows
        - tab: The heading on top of the screen
        - tab2: Heading that labels combo boxes where users submit anime
        - tab3: Heading that labels spin boxes where users submit ratings
        - tab4: Heading that labels combo boxes where users submit anime
        - tab5: Heading that labels spin boxes where users submit ratings
        - tab6: Heading that labels button where users can submit a csv file
        - button: Button that allows users to submit a csv file
        - button2: Button that allows users to submit input data
        - cbox1: Combo box where users choose an anime
        - cbox2: Combo box where users choose an anime
        - cbox3: Combo box where users choose an anime
        - cbox4: Combo box where users choose an anime
        - cbox5: Combo box where users choose an anime
        - cbox6: Combo box where users choose an anime
        - cbox7: Combo box where users choose an anime
        - cbox8: Combo box where users choose an anime
        - cbox9: Combo box where users choose an anime
        - cbox10: Combo box where users choose an anime
        - spin_box: Spin box where users choose a rating
        - sbox2: Spin box where users choose a rating
        - sbox3: Spin box where users choose a rating
        - sbox4: Spin box where users choose a rating
        - sbox5: Spin box where users choose a rating
        - sbox6: Spin box where users choose a rating
        - sbox7: Spin box where users choose a rating
        - sbox8: Spin box where users choose a rating
        - sbox9: Spin box where users choose a rating
        - sbox10: Spin box where users choose a rating
    """
    window: Optional[QtWidgets.QWidget]
    ui: Optional[UiForm]
    widget: Optional[QtWidgets.QStackedWidget]
    tab: Optional[QtWidgets.QLabel]
    tab2: Optional[QtWidgets.QLabel]
    tab3: Optional[QtWidgets.QLabel]
    tab4: Optional[QtWidgets.QLabel]
    tab5: Optional[QtWidgets.QLabel]
    tab6: Optional[QtWidgets.QLabel]
    button: Optional[QtWidgets.QPushButton]
    button2: Optional[QtWidgets.QPushButton]
    cbox1: Optional[QtWidgets.QComboBox]
    cbox2: Optional[QtWidgets.QComboBox]
    cbox3: Optional[QtWidgets.QComboBox]
    cbox4: Optional[QtWidgets.QComboBox]
    cbox5: Optional[QtWidgets.QComboBox]
    cbox6: Optional[QtWidgets.QComboBox]
    cbox7: Optional[QtWidgets.QComboBox]
    cbox8: Optional[QtWidgets.QComboBox]
    cbox9: Optional[QtWidgets.QComboBox]
    cbox10: Optional[QtWidgets.QComboBox]
    spin_box: Optional[QtWidgets.QSpinBox]
    sbox2: Optional[QtWidgets.QSpinBox]
    sbox3: Optional[QtWidgets.QSpinBox]
    sbox4: Optional[QtWidgets.QSpinBox]
    sbox5: Optional[QtWidgets.QSpinBox]
    sbox6: Optional[QtWidgets.QSpinBox]
    sbox7: Optional[QtWidgets.QSpinBox]
    sbox8: Optional[QtWidgets.QSpinBox]
    sbox9: Optional[QtWidgets.QSpinBox]
    sbox10: Optional[QtWidgets.QSpinBox]

    def __init__(self) -> None:
        """Set all attributes necessary for UiFrame to None by default."""
        self.tab = None
        self.tab2 = None
        self.tab3 = None
        self.tab4 = None
        self.tab5 = None
        self.tab6 = None
        self.button = None
        self.button2 = None
        self.cbox1 = None
        self.cbox2 = None
        self.cbox3 = None
        self.cbox4 = None
        self.cbox5 = None
        self.cbox6 = None
        self.cbox7 = None
        self.cbox8 = None
        self.cbox9 = None
        self.cbox10 = None
        self.spin_box = None
        self.sbox2 = None
        self.sbox3 = None
        self.sbox4 = None
        self.sbox5 = None
        self.sbox6 = None
        self.sbox7 = None
        self.sbox8 = None
        self.sbox9 = None
        self.sbox10 = None
        self.widget = None
        self.window = None
        self.ui = None

    def setup_ui(self, frame: QtWidgets.QFrame) -> None:
        """Set up the user input window and initializes all the variables
        to create the user interface of the window."""
        frame.setObjectName("frame")
        frame.setEnabled(True)
        frame.resize(777, 553)
        frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tab = QtWidgets.QLabel(frame)
        self.tab.setGeometry(QtCore.QRect(150, 30, 501, 61))
        self.tab.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tab.setFont(font)
        self.tab.setAutoFillBackground(False)
        self.tab.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tab.setAlignment(QtCore.Qt.AlignCenter)
        self.tab.setWordWrap(True)
        self.tab.setObjectName("tab")
        self.sbox9 = QtWidgets.QSpinBox(frame)
        self.sbox9.setGeometry(QtCore.QRect(680, 300, 42, 22))
        self.sbox9.setMaximum(10)
        self.sbox9.setObjectName("sbox9")
        self.cbox5 = QtWidgets.QComboBox(frame)
        self.cbox5.setGeometry(QtCore.QRect(60, 350, 231, 21))
        self.cbox5.setEditable(True)
        self.cbox5.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cbox5.setObjectName("cbox5")
        self.cbox5.addItem("")
        self.cbox6 = QtWidgets.QComboBox(frame)
        self.cbox6.setGeometry(QtCore.QRect(430, 150, 231, 21))
        self.cbox6.setEditable(True)
        self.cbox6.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cbox6.setObjectName("cbox6")
        self.cbox6.addItem("")
        self.cbox9 = QtWidgets.QComboBox(frame)
        self.cbox9.setGeometry(QtCore.QRect(430, 300, 231, 21))
        self.cbox9.setEditable(True)
        self.cbox9.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cbox9.setObjectName("cbox9")
        self.cbox9.addItem("")
        self.sbox5 = QtWidgets.QSpinBox(frame)
        self.sbox5.setGeometry(QtCore.QRect(310, 350, 42, 22))
        self.sbox5.setMaximum(10)
        self.sbox5.setObjectName("sbox5")
        self.sbox8 = QtWidgets.QSpinBox(frame)
        self.sbox8.setGeometry(QtCore.QRect(680, 250, 42, 22))
        self.sbox8.setMaximum(10)
        self.sbox8.setObjectName("sbox8")
        self.cbox8 = QtWidgets.QComboBox(frame)
        self.cbox8.setGeometry(QtCore.QRect(430, 250, 231, 21))
        self.cbox8.setEditable(True)
        self.cbox8.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cbox8.setObjectName("cbox8")
        self.cbox8.addItem("")
        self.cbox3 = QtWidgets.QComboBox(frame)
        self.cbox3.setGeometry(QtCore.QRect(60, 250, 231, 21))
        self.cbox3.setEditable(True)
        self.cbox3.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cbox3.setObjectName("cbox3")
        self.cbox3.addItem("")
        self.spin_box = QtWidgets.QSpinBox(frame)
        self.spin_box.setGeometry(QtCore.QRect(310, 150, 42, 22))
        self.spin_box.setMaximum(10)
        self.spin_box.setObjectName("spin_box")
        self.sbox10 = QtWidgets.QSpinBox(frame)
        self.sbox10.setGeometry(QtCore.QRect(680, 350, 42, 22))
        self.sbox10.setMaximum(10)
        self.sbox10.setObjectName("sbox10")
        self.cbox7 = QtWidgets.QComboBox(frame)
        self.cbox7.setGeometry(QtCore.QRect(430, 200, 231, 21))
        self.cbox7.setEditable(True)
        self.cbox7.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cbox7.setObjectName("cbox7")
        self.cbox7.addItem("")
        self.cbox10 = QtWidgets.QComboBox(frame)
        self.cbox10.setGeometry(QtCore.QRect(430, 350, 231, 21))
        self.cbox10.setEditable(True)
        self.cbox10.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cbox10.setObjectName("cbox10")
        self.cbox10.addItem("")
        self.sbox3 = QtWidgets.QSpinBox(frame)
        self.sbox3.setGeometry(QtCore.QRect(310, 250, 42, 22))
        self.sbox3.setMaximum(10)
        self.sbox3.setObjectName("sbox3")
        self.cbox4 = QtWidgets.QComboBox(frame)
        self.cbox4.setGeometry(QtCore.QRect(60, 300, 231, 21))
        self.cbox4.setEditable(True)
        self.cbox4.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cbox4.setObjectName("cbox4")
        self.cbox4.addItem("")
        self.sbox4 = QtWidgets.QSpinBox(frame)
        self.sbox4.setGeometry(QtCore.QRect(310, 300, 42, 22))
        self.sbox4.setMaximum(10)
        self.sbox4.setObjectName("sbox4")
        self.sbox2 = QtWidgets.QSpinBox(frame)
        self.sbox2.setGeometry(QtCore.QRect(310, 200, 42, 22))
        self.sbox2.setMaximum(10)
        self.sbox2.setObjectName("sbox2")
        self.sbox6 = QtWidgets.QSpinBox(frame)
        self.sbox6.setGeometry(QtCore.QRect(680, 150, 42, 22))
        self.sbox6.setMaximum(10)
        self.sbox6.setObjectName("sbox6")
        self.cbox2 = QtWidgets.QComboBox(frame)
        self.cbox2.setGeometry(QtCore.QRect(60, 200, 231, 21))
        self.cbox2.setEditable(True)
        self.cbox2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cbox2.setObjectName("cbox2")
        self.cbox2.addItem("")
        self.sbox7 = QtWidgets.QSpinBox(frame)
        self.sbox7.setGeometry(QtCore.QRect(680, 200, 42, 22))
        self.sbox7.setMaximum(10)
        self.sbox7.setObjectName("sbox7")
        self.cbox1 = QtWidgets.QComboBox(frame)
        self.cbox1.setGeometry(QtCore.QRect(60, 150, 231, 21))
        self.cbox1.setEditable(True)
        self.cbox1.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cbox1.setObjectName("cbox1")
        self.cbox1.addItem("")
        self.button2 = QtWidgets.QPushButton(frame)
        self.button2.setGeometry(QtCore.QRect(350, 410, 93, 28))
        self.button2.setObjectName("button2")
        self.tab4 = QtWidgets.QLabel(frame)
        self.tab4.setGeometry(QtCore.QRect(60, 120, 55, 16))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.tab4.sizePolicy().hasHeightForWidth())
        self.tab4.setSizePolicy(size_policy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tab4.setFont(font)
        self.tab4.setObjectName("tab4")
        self.tab2 = QtWidgets.QLabel(frame)
        self.tab2.setGeometry(QtCore.QRect(430, 120, 55, 16))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.tab2.sizePolicy().hasHeightForWidth())
        self.tab2.setSizePolicy(size_policy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tab2.setFont(font)
        self.tab2.setObjectName("tab2")
        self.tab3 = QtWidgets.QLabel(frame)
        self.tab3.setGeometry(QtCore.QRect(310, 120, 55, 16))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.tab3.sizePolicy().hasHeightForWidth())
        self.tab3.setSizePolicy(size_policy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tab3.setFont(font)
        self.tab3.setObjectName("tab3")
        self.tab5 = QtWidgets.QLabel(frame)
        self.tab5.setGeometry(QtCore.QRect(680, 120, 55, 16))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.tab5.sizePolicy().hasHeightForWidth())
        self.tab5.setSizePolicy(size_policy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tab5.setFont(font)
        self.tab5.setObjectName("tab5")
        self.tab6 = QtWidgets.QLabel(frame)
        self.tab6.setGeometry(QtCore.QRect(280, 480, 241, 16))
        self.tab6.setObjectName("tab6")
        self.button = QtWidgets.QPushButton(frame)
        self.button.setGeometry(QtCore.QRect(350, 510, 93, 28))
        self.button.setObjectName("button")

        self.retranslate_ui(frame)
        QtCore.QMetaObject.connectSlotsByName(frame)

        ui_functions.add_options(self.cbox1)
        ui_functions.add_options(self.cbox2)
        ui_functions.add_options(self.cbox3)
        ui_functions.add_options(self.cbox4)
        ui_functions.add_options(self.cbox5)
        ui_functions.add_options(self.cbox6)
        ui_functions.add_options(self.cbox7)
        ui_functions.add_options(self.cbox8)
        ui_functions.add_options(self.cbox9)
        ui_functions.add_options(self.cbox10)

        self.button2.clicked.connect(self.get_values)
        self.button.clicked.connect(self.get_file)

    def retranslate_ui(self, frame: QtWidgets.QFrame):
        """Enter the text onto the user interface."""
        _translate = QtCore.QCoreApplication.translate
        frame.setWindowTitle(_translate("frame", "Solo Watch"))
        self.tab.setText(_translate("frame",
                                    "Now enter up to 10 anime you have watched "
                                    "recently and your rating for each."))
        self.cbox5.setItemText(0, _translate("frame", "None"))
        self.cbox6.setItemText(0, _translate("frame", "None"))
        self.cbox9.setItemText(0, _translate("frame", "None"))
        self.cbox8.setItemText(0, _translate("frame", "None"))
        self.cbox3.setItemText(0, _translate("frame", "None"))
        self.cbox7.setItemText(0, _translate("frame", "None"))
        self.cbox10.setItemText(0, _translate("frame", "None"))
        self.cbox4.setItemText(0, _translate("frame", "None"))
        self.cbox2.setItemText(0, _translate("frame", "None"))
        self.cbox1.setItemText(0, _translate("frame", "None"))
        self.button2.setText(_translate("frame", "Let\'s Go!"))
        self.tab4.setText(_translate("frame", "Anime"))
        self.tab2.setText(_translate("frame", "Anime"))
        self.tab3.setText(_translate("frame", "Rating"))
        self.tab5.setText(_translate("frame", "Rating"))
        self.tab6.setText(_translate("frame",
                                     "<html><head/><body><p><span style=\" "
                                     "font-weight:600;\">Returning user? "
                                     "Use your csv data!</span></p></body></html>"))
        self.button.setText(_translate("frame", "Insert CSV"))

    def get_values(self) -> None:
        """Get values from user input (combo boxes and spin boxes)"""
        vals_so_far = dict()
        vals_so_far[self.cbox1.currentText()] = self.spin_box.value()
        vals_so_far[self.cbox2.currentText()] = self.sbox2.value()
        vals_so_far[self.cbox3.currentText()] = self.sbox3.value()
        vals_so_far[self.cbox4.currentText()] = self.sbox4.value()
        vals_so_far[self.cbox5.currentText()] = self.sbox5.value()
        vals_so_far[self.cbox6.currentText()] = self.sbox6.value()
        vals_so_far[self.cbox7.currentText()] = self.sbox7.value()
        vals_so_far[self.cbox8.currentText()] = self.sbox8.value()
        vals_so_far[self.cbox9.currentText()] = self.sbox9.value()
        vals_so_far[self.cbox10.currentText()] = self.sbox10.value()
        print(vals_so_far)
        self.window = QtWidgets.QWidget()
        self.ui = UiForm()
        self.ui.setup_ui(self.window)
        self.widget.addWidget(self.window)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def get_file(self) -> None:
        """Create a QDialogBox to get a file."""
        file_name = QtWidgets.QFileDialog.getOpenFileName()[0]
        print(file_name)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    solo_frame = QtWidgets.QFrame()
    ui = UiFrame()
    ui.setup_ui(solo_frame)
    solo_frame.show()
    sys.exit(app.exec_())
