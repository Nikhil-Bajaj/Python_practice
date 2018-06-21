class db:
    list = []

    def __init__(self,name):
        self.name = name

    def getName(self):
        ip1 = input("Please Enter your name")
        self.name = ip1
    def showName(self):
        print("Hello",self.name)
