import tkinter as tk
from tkinter.constants import TOP
from typing import Text

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
        self.idIndex = 1
    def AddProduct(self, p):
        self.invenList.append(p)
    def PrintInventory(self):
        for p in self.invenList:
            print("ID: " + str(p.id))
            print("Name: " + p.name + "\nPrice: $" + str(p.price))
            print("-----------------------------------")

inv = Inventory() #  This is the global inventory

def CreateProduct():
    name = input("Name: ")
    price = input("Price: ")
    p = Product(inv.idIndex, name, price,  inv)
    inv.idIndex += 1