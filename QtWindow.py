import configparser
from PySide6 import QtWidgets

config = configparser.ConfigParser()
config.read("config.ini")

logofile1 = config["TeamA"]["logo"]
logofile2 = config["TeamB"]["logo"]
def openLogo1():
    global logofile1
    logofile1 = QtWidgets.QFileDialog.getOpenFileName()[0]

def openLogo2():
    global logofile2
    logofile2 = QtWidgets.QFileDialog.getOpenFileName()[0]


def Save():
    config["TeamA"]["naam"] = editname1.toPlainText()
    config["TeamB"]["naam"] = editname2.toPlainText()
    config["TeamA"]["logo"] = logofile1
    config["TeamB"]["logo"] = logofile2
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

labellogo1 = QtWidgets.QLabel("Logo Team 1:")
logo1 = QtWidgets.QPushButton("Browse")
logo1.clicked.connect(openLogo1)
layout.addRow(labellogo1, logo1)

label2 = QtWidgets.QLabel("Team 2:")
editname2 = QtWidgets.QTextEdit(config["TeamB"]["naam"])
layout.addRow(label2, editname2)

labellogo2 = QtWidgets.QLabel("Logo Team 2:")
logo2 = QtWidgets.QPushButton("Browse")
logo2.clicked.connect(openLogo2)
layout.addRow(labellogo2, logo2)

button = QtWidgets.QPushButton("Save")
layout.addRow(button)
button.clicked.connect(Save)

app.exec_()
