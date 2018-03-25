class score:
    def __init__(self,name,score,comment):
        self.student = name.strip()
        self.score = score.strip()
        self.comment = comment.strip()

    def getStudent(self):
        return self.student

    def getScore(self):
        return self.score

    def getComment(self):
        return self.comment

    def writeToFile(self,file):
        file.write(self.student + " " + self.score + " " + self.comment)

    def __str__(self):
        return(self.student + " " + self.score + " " + self.comment)

    def __repr__(self):
        return(self.student + " " + self.score + " " + self.comment)