# TODO:
# Edit Product
# Get Sum Of All Products
# Menu

class Product:
    def __init__(self, _id, _name, _price, _inven):
        self.id = _id
        self.name = _name
        self.price = _price
        _inven.AddProduct(self)
    def PrintInformation(self):
        print("ID: " + str(self.id) + "\nName: " + self.name + "\nPrice: $" + str(self.price))

class Inventory:
    def __init__(self):
        self.invenList = []
        self.idIndex = 1
    def AddProduct(self, p):
        self.invenList.append(p)
    def PrintInventory(self):
        for p in self.invenList:
            print("ID: " + str(p.id))
            print("Name: " + p.name + "\nPrice: $" + str(p.price))
            print("-----------------------------------")
    def LookupProduct(self):
        idLook = input("ID to lookup: ")
        for p in self.invenList:
            if p.id == int(idLook):
                print(p.PrintInformation())
    def RemoveProduct(self):
        choice = input("What is the ID of the product you want to remove? ")
        for p in self.invenList:
            if p.id == int(choice):
                self.invenList.remove(p)
                removed = True
            else:
                removed = False
        if removed == True:
            print("The product with the ID of " + choice + " has been removed.")
        elif removed == False:
            print("Product with the ID of " + choice + " cannot be found.")
    def GetSum(self):
        sum = 0
        for p in self.invenList:
            sum += p.price
        return sum
        

inv = Inventory() #  This is the global inventory

def CreateProduct():
    name = input("Name: ")
    price = input("Price: ")
    p = Product(inv.idIndex, name, price, inv)
    inv.idIndex += 1

a = Product(1, "test", 25, inv)
b = Product(2, "test", 25, inv)
x = Product(3, "test", 25, inv)
y = Product(4, "test", 25, inv)
inv.RemoveProduct()
inv.PrintInventory()
print("Sum: " + str(inv.GetSum()))