from .lang import *
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import os

class mainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #very important
        #title
        self.setWindowTitle("Project Creator")
        #layout
        self.setLayout(qtw.QVBoxLayout())
        #label
        label = qtw.QLabel("")
        label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(label)

        #name box label
        namelab = qtw.QLabel("Project Name")
        namelab.setFont(qtg.QFont('Helvetica', 10))
        self.layout().addWidget(namelab)

        #the name box
        Namebox = qtw.QLineEdit()
        Namebox.setObjectName("name_field")
        self.layout().addWidget(Namebox)

        #path label
        pathlab = qtw.QLabel("Project Path")
        pathlab.setFont(qtg.QFont('Helvetica', 10))
        self.layout().addWidget(pathlab)

        #the path box
        Pathbox = qtw.QLineEdit("~/projects/")
        Pathbox.setObjectName("path_field")
        self.layout().addWidget(Pathbox)

        #language box
        langlab = qtw.QLabel("Project Language")
        langlab.setFont(qtg.QFont('Helvetica', 10))
        self.layout().addWidget(langlab)

        #the lang box
        langbox = qtw.QComboBox(self)
        langbox.addItem("Python")
        langbox.addItem("C++")
        self.layout().addWidget(langbox)

        #type box
        typelab = qtw.QLabel("Project Type")
        typelab.setFont(qtg.QFont('Helvetica', 10))
        self.layout().addWidget(typelab)

        #the type box
        typebox = qtw.QComboBox(self)
        typebox.addItem("Empty")
        self.layout().addWidget(typebox)

        #button
        button = qtw.QPushButton("Create project!", clicked = lambda: clicked())
        self.layout().addWidget(button)
        #show the window
        self.setFixedSize(350,250)
        self.show()

        def clicked():
            Name = Namebox.text()
            Lang = langbox.currentText()
            Path = Pathbox.text()
            Type = typebox.currentText()
            if Lang == "Python":
                pyLang(Name,Type,Path)
                label.setText("Project Created Successfully")
            elif Lang == "C++":
                cppLang(Name,Type,Path)
                label.setText("Project Created Successfully")

def comboInit():
    app = qtw.QApplication([])
    win = mainWindow()

    #run the app
    app.exec_()
