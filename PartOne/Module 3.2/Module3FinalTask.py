class stock:
#Definig variables
    def __init__(self, var):
        self.fullStock =  737
        self.minimumOrder = 5
        self.unitPrice = 7.37
        self.var = int(var) #making value that is provided a integer

#function to check and do actions
    def isInStock(self):
        if self.var > self.fullStock:
            print("You want too much my friend")
        elif self.var < self.minimumOrder:
            print("We dot sell our wonderful chease in so small portions")
        else:
            print("Yes, Ok, so " + str(self.var) + " kg of cheese would cost " + str(self.var * self.unitPrice) + ".")

#take the amount of cheese that is needed
print("Kiek nori surio zmogau?")
kiekNori = input()
#assign class to a variable and call the class function.
var = stock(kiekNori)
var.isInStock()
