from scores import score
from graderInput import gInput
from graderOutput import gOutput
import subprocess
import os

class autoGrader:
    def __init__(self,directory,input,output,writtenTo):
        self.directory = directory
        self.input = gInput(input)
        self.output = gOutput(output)
        self.file = writtenTo

    def writeToChild(self,child):
        str = ""
        for i in self.input.getUserI():
            str+=i+"\n"
        out = child.communicate(str)[0]
        return out

    def openChild(self):
        list = os.listdir(self.directory)
        f = open(self.file, "w")
        for i in list:
            print("Hello")
            output = "\n"
            i= self.directory+i
            name = self.getStudentName(i)
            file = subprocess.Popen(["python",i],bufsize= 1,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
            out = self.writeToChild(file)
            listsa = out.split('\n')
            print(listsa)
            """
            if self.output.similar(output):
                temp = score(name,"100%","GOOD JOB COMPLETED ASSIGNMENTasdf")
            else:
                temp = score(name,"0%","There is an error in this programa")
            f.write(temp.__repr__()+" " + output)
            """
        f.close()

    def getStudentName(self,file):
        f = open(file,"r")
        f.readline()
        name = f.readline()
        f.close()
        return name












