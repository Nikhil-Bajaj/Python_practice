import Db
class Deserts:
    def __init__(self,desert):
        self.desert = desert
    def getdesName(self):
        d1 = int(input("Do you want to add any deserts?Enter 1 for yes and 0 for No"))
        if (d1==1):
            d2 = int(input('''Which desert would you like to order fromt the following(Enter Number)-
            1. Soft Serve Cone Rs.20
            2. McSwril Chocolate Rs.30
            3. McSwril Butterscotch Rs.35
            4. Soft Serve Chocolate Rs.30
            5. Soft Serve Strawberry Rs.30
            press 0 for none '''
            ))
            if (d2 == 1):
                Db.db.list.append(20)
                self.desert = ('Soft Serve Cone Rs.20')
            elif(d2 == 2):
                Db.db.list.append(30)
                self.desert = ("McSwril Chocolate Rs.30")
            elif(d2 == 3):
                Db.db.list.append(35)
                self.desert = ("McSwril Butterscotch Rs.35")
            elif(d2 == 4):
                Db.db.list.append(30)
                self.desert = ("Soft Serve Chocolate Rs.30")
            elif(d2 == 5):
                Db.db.list.append(30)
                self.desert = ("Soft Serve Strawberry Rs.30")

            else:
                print("No valid input")
                pass
        elif (d1 == 0):
            pass
        else:
            print("No valid input")
            exit()
    def showdesData(self):
        print(self.desert)








