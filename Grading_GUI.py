"""

"""

from tkinter import *
from tkinter.filedialog import askdirectory
from autograder import autoGrader
import random

class GraderGui:

    def __init__(self, root):
        # Variables:
        self.directory = ""

        # Input:
        inputTitle = Message(root, text = "Input", font=("Times", 16), width = 100)
        inputTitle.grid(row = 0, column = 0)

        self.inputField = Text(root, width = 30, height = 10, padx = 10)
        self.inputField.grid(row = 1, column = 0)

        # Output:
        outputTitle = Message(root, text = "Output", font=("Times", 16), width = 100)
        outputTitle.grid(row = 2, column = 0)

        self.outputField = Text(root, width = 30, height = 10, padx = 10)
        self.outputField.grid(row = 3, column = 0)

        # Text Result
        resultTitle = Message(root, text = "Result", font=("Times", 16), width = 100)
        resultTitle.grid(row = 0, column = 1)

        self.textField = Text(root, width = 55, height = 25, padx = 10)
        self.textField.grid(row = 1, column = 1, rowspan = 3)

        scroll = Scrollbar(root)
        scroll.grid(row = 1, column = 2, sticky = 'ns', rowspan = 3)

        self.textField.config(state = DISABLED)# text in read only
        scroll.config(command = self.textField.yview)
        self.textField.config(yscrollcommand = scroll.set)

        # Directory:
        self.button = Button(root, text = "Choose a directory", command = self.openDirectory, width = 20)
        self.button.grid(row = 4, column = 0, sticky = EW)

        # Run
        self.show = Button(root, text = "Run", command = self.run, width = 10)
        self.show .grid(row = 4, column = 1, columnspan = 2, sticky = EW)


    def updateText(self, text):
        self.textField.config(state = NORMAL)
        self.textField.insert(END, text)
        self.textField.config(state = DISABLED)


    def openDirectory(self):
        self.directory = askdirectory(initialdir = ".", title = "Directory")


    def run(self):
        # 1.0: read from line 1
        # 'end - 1c': end minus 1 character
        input = self.inputField.get("1.0", 'end - 1c')
        output = self.outputField.get("1.0", 'end - 1c')
        auto = autoGrader(self.directory+"/",input,output,"Hello.txt")
        auto.openChild()
        f = open("Hello.txt", "r")
        for line in f:
            self.updateText(line)