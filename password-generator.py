from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, secrets, string, pyperclip


class MainWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(700, 400, 600, 400)
        self.setWindowTitle("Password Generator")
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.initUI()

        
    def initUI(self):

        # start label
        
        self.start_label = QtWidgets.QLabel(self)
        self.start_label.setFixedWidth(250)
        self.start_label.setText("Create a new password:")
        self.start_label.setAlignment(Qt.AlignLeft)
        self.start_label.move(10, 10)

        # second start label: which characters should be included

        self.start_label = QtWidgets.QLabel(self)
        self.start_label.setFixedWidth(250)
        self.start_label.setText("Characters:")
        self.start_label.setAlignment(Qt.AlignLeft)
        self.start_label.move(10, 50)

        # checkboxes for letters, digits and punctuation

        self.use_letters = QtWidgets.QCheckBox(self)
        self.use_letters.setText("Letters")
        self.use_letters.move(10, 80)

        self.use_digits = QtWidgets.QCheckBox(self)
        self.use_digits.setText("Digits")
        self.use_digits.move(10, 105)

        self.use_punctuation = QtWidgets.QCheckBox(self)
        self.use_punctuation.setText("Punctuation")
        self.use_punctuation.move(10, 130)

        # label next to spinbox

        self.label_spinbox = QtWidgets.QLabel(self)
        self.label_spinbox.setAlignment(Qt.AlignLeft)
        self.label_spinbox.move(10, 170)
        self.label_spinbox.setText("Length:")

        # spinbox for the length of the password

        self.length = QtWidgets.QSpinBox(self)
        self.length.setMinimum(1)
        self.length.setFixedWidth(50)
        self.length.setValue(10)
        self.length.setAlignment(Qt.AlignLeft)
        self.length.move(10, 200)

        # password label

        self.password_label = QtWidgets.QLabel(self)
        self.password_label.setAlignment(Qt.AlignLeft)
        self.password_label.move(10, 250)
        self.password_label.setFixedWidth(1000)
        self.password_label.setText("")

        # button, which generates the password

        self.generate_btn = QtWidgets.QPushButton(self)
        self.generate_btn.setText("Create")

        self.generate_btn.clicked.connect(lambda _: self.create_password(self.length.value(), self.use_letters.isChecked(),
                                                            self.use_digits.isChecked(), self.use_punctuation.isChecked()))

        # button, which copies the password

        self.copy_btn = QtWidgets.QPushButton(self)
        self.copy_btn.setText("Copy")

        self.lay = QtWidgets.QHBoxLayout(self) 
        self.lay.addStretch()    
        self.lay.addWidget(self.copy_btn, alignment=QtCore.Qt.AlignBottom)
        self.lay.addWidget(self.generate_btn, alignment=QtCore.Qt.AlignBottom)
        

    def create_password(self, length, use_letters, use_digits, use_punctuation):

        characters = []

        if use_letters == True:
            for _ in string.ascii_letters:
                characters.append(_)
        
        if use_digits == True:
            for _ in string.digits:
                characters.append(_)

        if use_punctuation == True:
            for _ in string.punctuation:
                characters.append(_)
        
        if len(characters) < 1:
            self.password_label.setText("You need to add at least one type of characters to your password.")
            return

        create_password = []

        for _ in range(length):
            create_password.append(secrets.choice(characters))

        self.password = "".join(create_password)
        self.password_label.setText(f"Your password: {self.password}")
        self.copy_btn.clicked.connect(lambda _: self.copy_password(self.password))

    def copy_password(self, passwd):
        pyperclip.copy(passwd)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
