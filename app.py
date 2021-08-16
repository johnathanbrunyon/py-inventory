# TODO:
# Create a list to store products
# Create a product 'class'
# Create an Inventory class

class Product:
    def __init__(self, _id, _name, _price, _inven):
        self.id = _id
        self.name = _name
        self.price = _price
        _inven.AddProduct(self)

class Inventory:
    def __init__(self):
        self.invenList = []
    def AddProduct(self, p):
        self.invenList.append(p)
    def PrintInventory(self):
        print("ID\t\t\t\tName\t\t\t\tPrice")
        print("---------------------------------------------------------------------------------")
        for p in self.invenList:
            print(str(p.id) + "\t\t\t\t" + p.name + "\t\t\t$" + str(p.price))
