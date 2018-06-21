import Db
class burger:
    def __init__(self,burger):
        self.burger = burger
    def getburgerName(self):
        b1 = int(input("Do you want to add any burger ?Enter 1 for yes and 0 for No"))
        if (b1==1):
            b2 = int(input('''Which Burger would you like to order fromt the following(Enter Number)
            1.McAlooTikki – Rs.30
            2.VegMcPuff – Rs.35
            3.McEgg – Rs.35
            4.ChickenMcGrill – Rs.45
            5.MasalaGrillVeg – Rs.50
            6.MasalaGrillChicken – Rs.60

            press 0 for none'''
            ))
            if (b2 == 1):
                Db.db.list.append(30)
                self.burger = ("McAlooTikki – Rs.30")
            elif(b2 == 2):
                Db.db.list.append(35)
                self.burger = ("VegMcPuff – Rs.35")
            elif(b2 == 3):
                Db.db.list.append(35)
                self.burger = ("McEgg – Rs.35")
            elif(b2 == 4):
                Db.db.list.append(45)
                self.burger = ("ChickenMcGrill – Rs.45")
            elif(b2 == 5):
                Db.db.list.append(50)
                self.burger = ("MasalaGrillVeg – Rs.50")
            elif(b2 == 6):
                Db.db.list.append(60)
                self.burger = ("MasalaGrillChicken – Rs.60")
            else:
                    print("No valid input")
                    pass
        elif (b1 == 0):
            pass
        else:
            print("No valid input")
            exit()
    def showburgerData(self):
        print(self.burger)








