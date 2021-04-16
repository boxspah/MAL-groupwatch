"""
CSC111 Project: Improving Anime Recommendations using
Weighted Graphs and Extended Metadata : Main Window

Module Description:
====================
The module contains the class that sets up the window where a single user makes their inputs.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Optional
import ui_functions


class UiFrame(object):
    """
    Create the window where a single user can input data.

    Instance Attributes:
        - label: The heading on top of the screen
        - label_2: Heading that labels combo boxes where users submit anime
        - label_3: Heading that labels spin boxes where users submit ratings
        - label_4: Heading that labels combo boxes where users submit anime
        - label_5: Heading that labels spin boxes where users submit ratings
        - label_6: Heading that labels button where users can submit a csv file
        - button: Button that allows users to submit a csv file
        - button_2: Button that allows users to submit input data
        - cBox1: Combo box where users choose an anime
        - cBox2: Combo box where users choose an anime
        - cBox3: Combo box where users choose an anime
        - cBox4: Combo box where users choose an anime
        - cBox5: Combo box where users choose an anime
        - cBox6: Combo box where users choose an anime
        - cBox7: Combo box where users choose an anime
        - cBox8: Combo box where users choose an anime
        - cBox9: Combo box where users choose an anime
        - cBox10: Combo box where users choose an anime
        - spinBox: Spin box where users choose a rating
        - sBox2: Spin box where users choose a rating
        - sBox3: Spin box where users choose a rating
        - sBox4: Spin box where users choose a rating
        - sBox5: Spin box where users choose a rating
        - sBox6: Spin box where users choose a rating
        - sBox7: Spin box where users choose a rating
        - sBox8: Spin box where users choose a rating
        - sBox9: Spin box where users choose a rating
        - sBox10: Spin box where users choose a rating
    """

    label: Optional[QtWidgets.QLabel]
    label_2: Optional[QtWidgets.QLabel]
    label_3: Optional[QtWidgets.QLabel]
    label_4: Optional[QtWidgets.QLabel]
    label_5: Optional[QtWidgets.QLabel]
    label_6: Optional[QtWidgets.QLabel]
    button: Optional[QtWidgets.QPushButton]
    button_2: Optional[QtWidgets.QPushButton]
    cBox1: Optional[QtWidgets.QComboBox]
    cBox2: Optional[QtWidgets.QComboBox]
    cBox3: Optional[QtWidgets.QComboBox]
    cBox4: Optional[QtWidgets.QComboBox]
    cBox5: Optional[QtWidgets.QComboBox]
    cBox6: Optional[QtWidgets.QComboBox]
    cBox7: Optional[QtWidgets.QComboBox]
    cBox8: Optional[QtWidgets.QComboBox]
    cBox9: Optional[QtWidgets.QComboBox]
    cBox10: Optional[QtWidgets.QComboBox]
    spinBox: Optional[QtWidgets.QSpinBox]
    sBox2: Optional[QtWidgets.QSpinBox]
    sBox3: Optional[QtWidgets.QSpinBox]
    sBox4: Optional[QtWidgets.QSpinBox]
    sBox5: Optional[QtWidgets.QSpinBox]
    sBox6: Optional[QtWidgets.QSpinBox]
    sBox7: Optional[QtWidgets.QSpinBox]
    sBox8: Optional[QtWidgets.QSpinBox]
    sBox9: Optional[QtWidgets.QSpinBox]
    sBox10: Optional[QtWidgets.QSpinBox]

    def __init__(self) -> None:
        """Set all attributes necessary for UiFrame to None by default."""
        self.label = None
        self.label_2 = None
        self.label_3 = None
        self.label_4 = None
        self.label_5 = None
        self.label_6 = None
        self.button = None
        self.button_2 = None
        self.cBox1 = None
        self.cBox2 = None
        self.cBox3 = None
        self.cBox4 = None
        self.cBox5 = None
        self.cBox6 = None
        self.cBox7 = None
        self.cBox8 = None
        self.cBox9 = None
        self.cBox10 = None
        self.spinBox = None
        self.sBox2 = None
        self.sBox3 = None
        self.sBox4 = None
        self.sBox5 = None
        self.sBox6 = None
        self.sBox7 = None
        self.sBox8 = None
        self.sBox9 = None
        self.sBox10 = None

    def setup_ui(self, frame: QtWidgets.QFrame) -> None:
        """Set up the user input window and initializes all the variables
        to create the user interface of the window."""
        frame.setObjectName("frame")
        frame.setEnabled(True)
        frame.resize(777, 553)
        frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label = QtWidgets.QLabel(frame)
        self.label.setGeometry(QtCore.QRect(150, 30, 501, 61))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.sBox9 = QtWidgets.QSpinBox(frame)
        self.sBox9.setGeometry(QtCore.QRect(680, 300, 42, 22))
        self.sBox9.setMaximum(10)
        self.sBox9.setObjectName("sBox9")
        self.cBox5 = QtWidgets.QComboBox(frame)
        self.cBox5.setGeometry(QtCore.QRect(60, 350, 231, 21))
        self.cBox5.setEditable(True)
        self.cBox5.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cBox5.setObjectName("cBox5")
        self.cBox5.addItem("")
        self.cBox6 = QtWidgets.QComboBox(frame)
        self.cBox6.setGeometry(QtCore.QRect(430, 150, 231, 21))
        self.cBox6.setEditable(True)
        self.cBox6.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cBox6.setObjectName("cBox6")
        self.cBox6.addItem("")
        self.cBox9 = QtWidgets.QComboBox(frame)
        self.cBox9.setGeometry(QtCore.QRect(430, 300, 231, 21))
        self.cBox9.setEditable(True)
        self.cBox9.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cBox9.setObjectName("cBox9")
        self.cBox9.addItem("")
        self.sBox5 = QtWidgets.QSpinBox(frame)
        self.sBox5.setGeometry(QtCore.QRect(310, 350, 42, 22))
        self.sBox5.setMaximum(10)
        self.sBox5.setObjectName("sBox5")
        self.sBox8 = QtWidgets.QSpinBox(frame)
        self.sBox8.setGeometry(QtCore.QRect(680, 250, 42, 22))
        self.sBox8.setMaximum(10)
        self.sBox8.setObjectName("sBox8")
        self.cBox8 = QtWidgets.QComboBox(frame)
        self.cBox8.setGeometry(QtCore.QRect(430, 250, 231, 21))
        self.cBox8.setEditable(True)
        self.cBox8.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cBox8.setObjectName("cBox8")
        self.cBox8.addItem("")
        self.cBox3 = QtWidgets.QComboBox(frame)
        self.cBox3.setGeometry(QtCore.QRect(60, 250, 231, 21))
        self.cBox3.setEditable(True)
        self.cBox3.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cBox3.setObjectName("cBox3")
        self.cBox3.addItem("")
        self.spinBox = QtWidgets.QSpinBox(frame)
        self.spinBox.setGeometry(QtCore.QRect(310, 150, 42, 22))
        self.spinBox.setMaximum(10)
        self.spinBox.setObjectName("spinBox")
        self.sBox10 = QtWidgets.QSpinBox(frame)
        self.sBox10.setGeometry(QtCore.QRect(680, 350, 42, 22))
        self.sBox10.setMaximum(10)
        self.sBox10.setObjectName("sBox10")
        self.cBox7 = QtWidgets.QComboBox(frame)
        self.cBox7.setGeometry(QtCore.QRect(430, 200, 231, 21))
        self.cBox7.setEditable(True)
        self.cBox7.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cBox7.setObjectName("cBox7")
        self.cBox7.addItem("")
        self.cBox10 = QtWidgets.QComboBox(frame)
        self.cBox10.setGeometry(QtCore.QRect(430, 350, 231, 21))
        self.cBox10.setEditable(True)
        self.cBox10.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cBox10.setObjectName("cBox10")
        self.cBox10.addItem("")
        self.sBox3 = QtWidgets.QSpinBox(frame)
        self.sBox3.setGeometry(QtCore.QRect(310, 250, 42, 22))
        self.sBox3.setMaximum(10)
        self.sBox3.setObjectName("sBox3")
        self.cBox4 = QtWidgets.QComboBox(frame)
        self.cBox4.setGeometry(QtCore.QRect(60, 300, 231, 21))
        self.cBox4.setEditable(True)
        self.cBox4.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cBox4.setObjectName("cBox4")
        self.cBox4.addItem("")
        self.sBox4 = QtWidgets.QSpinBox(frame)
        self.sBox4.setGeometry(QtCore.QRect(310, 300, 42, 22))
        self.sBox4.setMaximum(10)
        self.sBox4.setObjectName("sBox4")
        self.sBox2 = QtWidgets.QSpinBox(frame)
        self.sBox2.setGeometry(QtCore.QRect(310, 200, 42, 22))
        self.sBox2.setMaximum(10)
        self.sBox2.setObjectName("sBox2")
        self.sBox6 = QtWidgets.QSpinBox(frame)
        self.sBox6.setGeometry(QtCore.QRect(680, 150, 42, 22))
        self.sBox6.setMaximum(10)
        self.sBox6.setObjectName("sBox6")
        self.cBox2 = QtWidgets.QComboBox(frame)
        self.cBox2.setGeometry(QtCore.QRect(60, 200, 231, 21))
        self.cBox2.setEditable(True)
        self.cBox2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cBox2.setObjectName("cBox2")
        self.cBox2.addItem("")
        self.sBox7 = QtWidgets.QSpinBox(frame)
        self.sBox7.setGeometry(QtCore.QRect(680, 200, 42, 22))
        self.sBox7.setMaximum(10)
        self.sBox7.setObjectName("sBox7")
        self.cBox1 = QtWidgets.QComboBox(frame)
        self.cBox1.setGeometry(QtCore.QRect(60, 150, 231, 21))
        self.cBox1.setEditable(True)
        self.cBox1.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cBox1.setObjectName("cBox1")
        self.cBox1.addItem("")
        self.button_2 = QtWidgets.QPushButton(frame)
        self.button_2.setGeometry(QtCore.QRect(350, 410, 93, 28))
        self.button_2.setObjectName("button_2")
        self.label_4 = QtWidgets.QLabel(frame)
        self.label_4.setGeometry(QtCore.QRect(60, 120, 55, 16))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(size_policy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(frame)
        self.label_2.setGeometry(QtCore.QRect(430, 120, 55, 16))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(size_policy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(frame)
        self.label_3.setGeometry(QtCore.QRect(310, 120, 55, 16))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(size_policy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(frame)
        self.label_5.setGeometry(QtCore.QRect(680, 120, 55, 16))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(size_policy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(frame)
        self.label_6.setGeometry(QtCore.QRect(280, 480, 241, 16))
        self.label_6.setObjectName("label_6")
        self.button = QtWidgets.QPushButton(frame)
        self.button.setGeometry(QtCore.QRect(350, 510, 93, 28))
        self.button.setObjectName("button")

        self.retranslate_ui(frame)
        QtCore.QMetaObject.connectSlotsByName(frame)

        ui_functions.add_options(self.cBox1)
        ui_functions.add_options(self.cBox2)
        ui_functions.add_options(self.cBox3)
        ui_functions.add_options(self.cBox4)
        ui_functions.add_options(self.cBox5)
        ui_functions.add_options(self.cBox6)
        ui_functions.add_options(self.cBox7)
        ui_functions.add_options(self.cBox8)
        ui_functions.add_options(self.cBox9)
        ui_functions.add_options(self.cBox10)

        self.button_2.clicked.connect(self.get_values)
        self.button.clicked.connect(self.get_file)

    def retranslate_ui(self, frame: QtWidgets.QFrame):
        """Enter the text onto the user interface."""
        _translate = QtCore.QCoreApplication.translate
        frame.setWindowTitle(_translate("frame", "Solo Watch"))
        self.label.setText(_translate("frame",
                                      "Now enter up to 10 anime you have watched "
                                      "recently and your rating for each."))
        self.cBox5.setItemText(0, _translate("frame", "None"))
        self.cBox6.setItemText(0, _translate("frame", "None"))
        self.cBox9.setItemText(0, _translate("frame", "None"))
        self.cBox8.setItemText(0, _translate("frame", "None"))
        self.cBox3.setItemText(0, _translate("frame", "None"))
        self.cBox7.setItemText(0, _translate("frame", "None"))
        self.cBox10.setItemText(0, _translate("frame", "None"))
        self.cBox4.setItemText(0, _translate("frame", "None"))
        self.cBox2.setItemText(0, _translate("frame", "None"))
        self.cBox1.setItemText(0, _translate("frame", "None"))
        self.button_2.setText(_translate("frame", "Let\'s Go!"))
        self.label_4.setText(_translate("frame", "Anime"))
        self.label_2.setText(_translate("frame", "Anime"))
        self.label_3.setText(_translate("frame", "Rating"))
        self.label_5.setText(_translate("frame", "Rating"))
        self.label_6.setText(_translate("frame",
                                        "<html><head/><body><p><span style=\" "
                                        "font-weight:600;\">Returning user? "
                                        "Use your csv data!</span></p></body></html>"))
        self.button.setText(_translate("frame", "Insert CSV"))

    def get_values(self) -> None:
        """Get values from user input (combo boxes and spin boxes)"""
        vals_so_far = dict()
        vals_so_far[self.cBox1.currentText()] = self.spinBox.value()
        vals_so_far[self.cBox2.currentText()] = self.sBox2.value()
        vals_so_far[self.cBox3.currentText()] = self.sBox3.value()
        vals_so_far[self.cBox4.currentText()] = self.sBox4.value()
        vals_so_far[self.cBox5.currentText()] = self.sBox5.value()
        vals_so_far[self.cBox6.currentText()] = self.sBox6.value()
        vals_so_far[self.cBox7.currentText()] = self.sBox7.value()
        vals_so_far[self.cBox8.currentText()] = self.sBox8.value()
        vals_so_far[self.cBox9.currentText()] = self.sBox9.value()
        vals_so_far[self.cBox10.currentText()] = self.sBox10.value()
        print(vals_so_far)

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
