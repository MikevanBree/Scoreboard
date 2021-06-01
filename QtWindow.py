import configparser
from PySide6 import QtWidgets

def Save():
    print("Test button")

width = 1024

app = QtWidgets.QApplication()
wid = QtWidgets.QWidget()
wid.show()

layout = QtWidgets.QFormLayout(wid) # Nieuw Grid -> Form

label1 = QtWidgets.QLabel("Team 1:")
edit = QtWidgets.QTextEdit()
layout.addRow(label1, edit)

label2 = QtWidgets.QLabel("Team 2:")
edit = QtWidgets.QTextEdit()
layout.addRow(label2, edit)

button = QtWidgets.QPushButton("Save", wid)
button.show()
button.clicked.connect(Save)

app.exec_()
