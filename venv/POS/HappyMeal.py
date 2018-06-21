import Objects

class HappyMeal:
    def __init__(self,name,burger,extras,deserts,meals,beverages,receiptNo):
        self.name = name
        self.burger = burger
        self.extras = extras
        self.deserts = deserts
        self.meals = meals
        self.beverages = beverages
        self.receiptNo = receiptNo


    def getData(self):
        self.name.getName()
        gm = int(input("Press 1 for Meal and 2 to create your order"))
        if (gm == 1):
            self.meals.getMeal()
        elif (gm == 2):
            self.burger.getburgerName()
            self.extras.getExtras()
            self.beverages.getbevName()
            self.deserts.getdesName()
        else:
            print("Invalid Input")
            pass
    def showData(self):
        print("-------------------------------------\n")

        self.name.showName()
        print("The receipt of your order is as follows:\n order No. is {}".format(self.receiptNo))
        print("Items you have ordered:\n")
        self.meals.showMeal()
        self.burger.showburgerData()
        self.extras.showExtras()
        self.deserts.showdesData()
        self.beverages.showbevData()
        SGST = sum(Objects.d1.list) * (2.5 / 100)
        CGST = sum(Objects.d1.list) * (2.5 / 100)
        print("\n  Sub Total = Rs.",sum(Objects.d1.list))
        print("\n SGST = ",SGST,"CGST= ",CGST,"\n")
        print("Total Amount = Rs.",int(sum(Objects.d1.list)+CGST+SGST))
        print("Please Visit Again ")
receiptNo = 1000
x = 4
list = []
while (x!=0):
    x = int (input("Hello!!!Do you wish to order something?Press 1 for yes and 0 for no"))
    if (x==1):

         receiptNo = receiptNo + 1
         hp = HappyMeal(Objects.d1, Objects.bu, Objects.ex, Objects.des, Objects.me, Objects.bev, receiptNo)
         hp.getData()
         hp.showData()
         list.append(hp)
    else:
        pass

y = int(input("Do u want to see all orders?Press 1 for yes and 0 for no"))
if (y==1):
    print("All orders are:")
    for i in list:
        print(i.showData())
else:
    print("Thank You")
    exit()




# objlist.append(hp)
# obj.Receipt.receipt.getRno()
"""objlist = []
for i in range(100,):
    hp = HappyMeal(obj.DB,obj.bu,obj.ex,obj.des,obj.me,obj.receipt)
    objlist.append(hp)
    obj.Receipt.receipt.getRno()
"""