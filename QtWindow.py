import configparser
from PySide6 import QtWidgets

config = configparser.ConfigParser()
config.read("config.ini")

def Save():
    config["TeamA"]["naam"] = editname1.toPlainText()
    config["TeamB"]["naam"] = editname2.toPlainText()
    configfile = open("./config.ini", "wt")
    config.write(configfile)
    configfile.close()

width = 1024

app = QtWidgets.QApplication()
wid = QtWidgets.QWidget()
wid.show()

layout = QtWidgets.QFormLayout(wid) # Nieuw Grid -> Form

label1 = QtWidgets.QLabel("Team 1:")
editname1 = QtWidgets.QTextEdit(config["TeamA"]["naam"])
layout.addRow(label1, editname1)

label2 = QtWidgets.QLabel("Team 2:")
editname2 = QtWidgets.QTextEdit(config["TeamB"]["naam"])
layout.addRow(label2, editname2)

button = QtWidgets.QPushButton("Save")
layout.addRow(button)
button.clicked.connect(Save)

app.exec_()
