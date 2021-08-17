# TODO:
# Edit Product
# Remove Product
# Get Sum Of All Products

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

inv = Inventory() #  This is the global inventory

def CreateProduct():
    name = input("Name: ")
    price = input("Price: ")
    p = Product(inv.idIndex, name, price, inv)
    inv.idIndex += 1

CreateProduct()
inv.LookupProduct()