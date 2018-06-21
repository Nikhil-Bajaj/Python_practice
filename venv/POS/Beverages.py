from POS import Db
class beverages:
    def __init__(self,bevName):
        self.bevName = bevName
    def getbevName(self):
        b1 = int(input("Do you want to add any beverages?Enter 1 for yes and 0 for No"))
        if (b1==1):
            b2 = int(input('''Which Beverage would you like to order fromt the following(Enter Number)-
            1.CokeSmall(250ml)- Rs.30
            2.CokeMedium(450 ml) - Rs. 50
            3.CokeLarge(650 ml)- Rs. 70
            4.SpriteSmall(250ml)- Rs.30
            5.SpriteMedium(450 ml) - Rs. 50
            6.SpriteLarge(650 ml)- Rs. 70
            7. McFloat(Small) - Rs. 40
            8. McFloat(Large) - Rs 65
            press 0 for none '''
            ))
            if (b2 == 1):
                Db.db.list.append(30)
                self.bevName = ('Coke Small-Rs.30')
            elif(b2 == 2):
                Db.db.list.append(50)
                self.bevName = ("Coke Medium-Rs.50")
            elif(b2 == 3):
                Db.db.list.append(70)
                self.bevName = ("Coke Large-Rs.70")
            elif(b2 == 4):
                Db.db.list.append(30)
                self.bevName = ("Sprite Small-Rs.30")
            elif(b2 == 5):
                Db.db.list.append(50)
                self.bevName = ("Sprite Medium-Rs.50")
            elif (b2 == 6):
                Db.db.list.append(70)
                self.bevName = ("Sprite Large-Rs.70")
            elif (b2 == 7):
                Db.db.list.append(40)
                self.bevName = ("McFloat-Rs.40")
            elif (b2 == 8):
                Db.db.list.append(65)
                self.bevName = ("McFloat-Rs.65")
            else:
                print("No valid input")
                pass
        elif (b1 == 0):
            pass
        else:
            print("No valid input")
            exit()
    def showbevData(self):
        print(self.bevName)








