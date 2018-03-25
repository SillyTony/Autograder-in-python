
class gInput:
    def __init__(self,userI):
        self.input = self.clean(userI)

    def clean(self,userI):
        return userI.split(',')

    def getUserI(self):
        return self.input

    def __str__(self):
        changeString = ""

        for i in self.input:
            changeString+=i+" "

        return changeString