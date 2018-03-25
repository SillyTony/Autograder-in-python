class gOutput:
    def __init__(self,userO):
        self.output = userO+"\n"

    def getUserO(self):
        return self.output

    def similar(self,other):
        return self.output == other
    def __str__(self):
        changeString = ""

        for i in self.output:
            changeString+=i+" "

        return changeString