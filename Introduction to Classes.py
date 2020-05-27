###Introductiom to classes
##
###1
##class car:
##    speed=0
##    def acc(self):
##        self.speed= self.speed+1
##
##    def brake(self):
##        self.speed=self.speed-1
##
##    def display(self):
##        print("The speed of the car is",self.speed)
##
##red = car()
##
##red.acc()
##red.acc()
##red.display()
##red.brake()
##red.display()
##red.acc()
##red.acc()
##red.display()

#2

class shoppinglist:
    
    def  _init_(self):
        self.listdict={}


    def addItem(self, key, val):
        if key in self.listdict:
            self.listdict[key] = self.listdict[key] + 1
        else:
            self.listdict[key] = val

    def subtractItem(self, key, val):
        if key in self.listdict:
            self.listdict[key]=self.listdict[key] - val

    def removeItem(self, key):
        if key in self.listdict:
            del(self.listdict[key])

    def printlist(self):
        print(self.listdict)


sl1 = shoppinglist()

sl1._init_()

sl1.addItem("Banana",12)
sl1.addItem("Apple", 6)
sl1.printlist()
sl1.subtractItem("Banana",5)
sl1.printlist()
sl1.removeItem("apple")
sl1.printlist()


sl2 = shoppinglist()
sl2._init_()
sl2.addItem("notebook", 12)
sl2.printlist()
