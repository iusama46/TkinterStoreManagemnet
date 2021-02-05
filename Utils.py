from tkinter import IntVar, StringVar


class Customer:
    custName = ''
    custPhone = ''

    def __init__(self):
        self.custName = StringVar()
        self.custPhone = StringVar()


class Product:
    price = ''
    tax = ''

    def __init__(self):
        self.price = StringVar()
        self.tax = StringVar()


class Cosmetics(Product):
    soap = ''
    fcream = ''
    fwash = ''
    ltn = ''
    spray = ''
    gel = ''

    def __init__(self):
        super().__init__()
        self.soap = IntVar()
        self.fcream = IntVar()
        self.fwash = IntVar()
        self.spray = IntVar()
        self.gel = IntVar()
        self.ltn = IntVar()


class ColdDrinks(Product):
    sprite = ''
    fanta = ''
    mint = ''
    lichee = ''
    cola = ''
    rooh = ''

    def __init__(self):
        super().__init__()
        self.sprite = IntVar()
        self.fanta = IntVar()
        self.mint = IntVar()
        self.lichee = IntVar()
        self.cola = IntVar()
        self.rooh = IntVar()


class Grocery(Product):
    rice = ''
    oil = ''
    daal = ''
    wheat = ''
    sugar = ''
    tea = ''

    def __init__(self):
        super().__init__()
        self.rice = IntVar()
        self.oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.rice = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
