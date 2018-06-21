import Db
class Meal:
    def __init__(self,meal):
        self.meal = meal

    def getMeal(self):
        m1 = int(input('''Which type of meal (Burger+Fries+Coke) do you want?Enter the number\n
        1. Veg
        2. VegEgg
        3. NonVeg Egg
        4. NonVeg
        Enter 0 for none!!'''
        ))
        if (m1 == 1):
            m2 = int(input('''Which meal would you like to order?Enter the number
            1. Medium Veg Rs 150
            2. Large Veg  Rs 190'''
            ))
            if (m2 == 1):
                Db.db.list.append(150)
                self.meal = ("Medium Veg Rs.150")
            elif (m2 == 2):
                Db.db.list.append(190)
                self.meal = ("Large Veg Rs.190")
            else:
                print("No valid input")
                pass
        elif (m1 == 2):
            m2 = int(input('''Which meal would you like to order?Enter the number
            1. Medium VegEgg Rs 160
            2. Large VegEgg  Rs 200'''
            ))
            if (m2 == 1):
                Db.db.list.append(160)
                self.meal = ("Medium VegEgg Rs.160")
            elif (m2 == 2):
                Db.db.list.append(200)
                self.meal = ("Large VegEgg Rs.200")
            else:
                print("No valid input")
                pass
        elif ( m1 == 3):
            m2 = int(input('''Which meal would you like to order?Enter the number
            1. Medium NonVeg Egg Rs 190
            2. Large NonVeg  Egg Rs 220'''
            ))
            if (m2 == 1):
                Db.db.list.append(190)
                self.meal = ("Medium NonVeg Egg Rs.190")
            elif (m2 == 2):
                Db.db.list.append(220)
                self.meal = ("Large NonVeg Egg Rs.220")
            else:
                print("No valid input")
                pass
        elif (m1 == 4):
            m2 = int(input('''Which meal would you like to order?Enter the number
            1. Medium NonVeg Rs 180
            2. Large NonVeg  Rs 210'''
            ))
            if (m2 == 1):
                Db.db.list.append(180)
                self.meal = ("Medium NonVeg Rs.180")
            elif (m2 == 2):
                Db.db.list.append(210)
                self.meal = ("Large NonVeg Rs.210")
            else:
                print("No valid input")
                pass
        else:
            print("No Valid Input")
            exit()

    def showMeal(self):
        print(self.meal)