import Db
class Extras:
    def __init__(self,extras):
        self.extras = extras
    def getExtras(self):
        e1 = int(input("Do you want to add any extras?Enter 1 for yes and 0 for No"))
        if (e1==1):
            e2 = int(input("""Which extras would you like to order from the following(Enter Number)-
            1.SmallFries: Rs.60
            2.MediumFries: Rs.75
            3.LargeFries: Rs.95
            4.McAlooWrapwith Chipotle Sauce – Rs.50
            5.Egg Wrap with Chipotle Sauce – Rs.50
            6.Grill Chicken Wrap with Chipotle Sauce – Rs.60
            7.Veg Pizza McPuff – Rs.25
            press 0 for none """
            ))
            if (e2 == 1):
                Db.db.list.append(60)
                self.extras = ('Small Fries-Rs.60')
            elif(e2 == 2):
                Db.db.list.append(75)
                self.extras = ("Fries Medium-Rs.75")
            elif(e2 == 3):
                Db.db.list.append(95)
                self.extras = ("Fries Large-Rs.90")
            elif(b2 == 4):
                Db.db.list.append(50)
                self.extras = ("McAlooWrapwith Chipotle Sauce-Rs.50")
            elif(b2 == 5):
                Db.db.list.append(50)
                self.extras = ("Egg Wrap with Chipotle Sauce-Rs.50")
            elif (b2 == 6):
                Db.db.list.append(60)
                self.extras = ("Grill Chicken Wrap with Chipotle Sauce-Rs.70")
            elif (b2 == 7):
                Db.db.list.append(25)
                self.extras = ("Veg Pizza McPuff – Rs.25")

            else:
                print("No valid input")
                pass
        elif (e1 == 0):
            pass
        else:
            print("No valid input")
            exit()
    def showExtras(self):
        print(self.extras)








