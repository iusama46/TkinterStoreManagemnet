import os
import random
from tkinter import *
from tkinter import messagebox

from Utils import Grocery, Cosmetics, ColdDrinks, Customer


class BillApp:

    def __init__(self, MyWindow):
        self.MyWindow = MyWindow
        self.MyWindow.geometry("1350x700+0+0")
        self.MyWindow.title("Ussama")
        bg_color = "#46344E"
        title = Label(self.MyWindow, text="Billing Interface", bd=12, relief=GROOVE, bg=bg_color, fg="white",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        self.customer = Customer()
        self.grocery = Grocery()
        self.cosmetics = Cosmetics()
        self.coldDrink = ColdDrinks()

        self.billNum = StringVar()
        x = random.randint(1000, 9999)
        self.billNum.set(str(x))
        self.searchBill = StringVar()

        # Customer detail frame
        frm1 = LabelFrame(self.MyWindow, bd=10, relief=GROOVE, text="Customer Details",
                          font=("Times New Roman", 15, "bold"), fg="gold", bg=bg_color)
        frm1.place(x=0, y=80, relwidth=1)

        customerName_lbl = Label(frm1, text="Customer Name", bg=bg_color, fg="white",
                                 font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        customerName_text = Entry(frm1, width=15, textvariable=self.customer.custName, font="arial 15", bd=7,
                                  relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        customerPhone_lbl = Label(frm1, text="Phone No.", bg=bg_color, fg="white",
                                  font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        customerPhone_text = Entry(frm1, width=15, textvariable=self.customer.custPhone, font="arial 15", bd=7,
                                   relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        customerBill_lbl = Label(frm1, text="Customer Bill", bg=bg_color, fg="white",
                                 font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        customerBill_text = Entry(frm1, width=15, textvariable=self.searchBill, font="arial 15", bd=7,
                                  relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(frm1, text="Search", command=self.find_bill, width=10, bd=7, font="arial 12 bold").grid(row=0,
                                                                                                                  column=6,
                                                                                                                  padx=10,
                                                                                                                  pady=10)

        # Cosmetic Frame

        frm2 = LabelFrame(self.MyWindow, bd=10, relief=GROOVE, text="Cosmetics", font=("Times New Roman", 15, "bold"),
                          fg="gold", bg=bg_color)
        frm2.place(x=5, y=180, width=325, height=380)

        bath_label = Label(frm2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(frm2, width=10, textvariable=self.cosmetics.soap, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        faceCream_label = Label(frm2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color,
                                fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        faceCream_txt = Entry(frm2, width=10, textvariable=self.cosmetics.fcream, font=("times new roman", 16, "bold"),
                              bd=5,
                              relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        faceWash_label = Label(frm2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        faceWash_txt = Entry(frm2, width=10, textvariable=self.cosmetics.fwash, font=("times new roman", 16, "bold"),
                             bd=5,
                             relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        HairSpr_label = Label(frm2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color,
                              fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        HairSpr_txt = Entry(frm2, width=10, textvariable=self.cosmetics.spray, font=("times new roman", 16, "bold"),
                            bd=5,
                            relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        HairGel_label = Label(frm2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color,
                              fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        HairGel_txt = Entry(frm2, width=10, textvariable=self.cosmetics.gel, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        BodyLtn_label = Label(frm2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color,
                              fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        BodyLtn_txt = Entry(frm2, width=10, textvariable=self.cosmetics.ltn, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # Grocery Product

        frm3 = LabelFrame(self.MyWindow, bd=10, relief=GROOVE, text="Grocery", font=("Times New Roman", 15, "bold"),
                          fg="gold", bg=bg_color)
        frm3.place(x=340, y=180, width=325, height=380)

        rice_label = Label(frm3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        rice_txt = Entry(frm3, width=10, textvariable=self.grocery.rice, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        oil_label = Label(frm3, text="Oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        oil_txt = Entry(frm3, width=10, textvariable=self.grocery.oil, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        daal_label = Label(frm3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        daal_txt = Entry(frm3, width=10, textvariable=self.grocery.daal, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        wheat_label = Label(frm3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color,
                            fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        wheat_txt = Entry(frm3, width=10, textvariable=self.grocery.wheat, font=("times new roman", 16, "bold"), bd=5,
                          relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        sugar_label = Label(frm3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color,
                            fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        sugar_txt = Entry(frm3, width=10, textvariable=self.grocery.sugar, font=("times new roman", 16, "bold"), bd=5,
                          relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        tea_label = Label(frm3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        tea_txt = Entry(frm3, width=10, textvariable=self.grocery.tea, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ColdDrink Frame
        frm4 = LabelFrame(self.MyWindow, bd=10, relief=GROOVE, text="Cold Drinks", font=("Times New Roman", 15, "bold"),
                          fg="gold", bg=bg_color)
        frm4.place(x=670, y=180, width=325, height=380)

        cola_label = Label(frm4, text="Coca Cola", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        cola_txt = Entry(frm4, width=10, textvariable=self.coldDrink.cola, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        sprt_label = Label(frm4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        sprt_txt = Entry(frm4, width=10, textvariable=self.coldDrink.sprite, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        fant_label = Label(frm4, text="Fanta", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        fant_txt = Entry(frm4, width=10, textvariable=self.coldDrink.fanta, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        mint_label = Label(frm4, text="Mint Margareta", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        mint_txt = Entry(frm4, width=10, textvariable=self.coldDrink.mint, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        lichee_label = Label(frm4, text="Lichee", font=("times new roman", 16, "bold"), bg=bg_color,
                             fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        lichee_txt = Entry(frm4, width=10, textvariable=self.coldDrink.lichee, font=("times new roman", 16, "bold"),
                           bd=5,
                           relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        rooh_label = Label(frm4, text="Jam e Shireen", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        rooh_txt = Entry(frm4, width=10, textvariable=self.coldDrink.rooh, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # Bill Area Frame

        Frm5 = Frame(self.MyWindow, bd=10, relief=GROOVE)
        Frm5.place(x=1000, y=180, width=360, height=380)
        bill_title = Label(Frm5, text="Bill Area", font=("arial", 15, "bold"), bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(Frm5, orient=VERTICAL)
        self.txtarea = Text(Frm5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # Button Frame

        Frm6 = LabelFrame(self.MyWindow, bd=10, relief=GROOVE, text="Bill Menu", font=("Times New Roman", 15, "bold"),
                          fg="gold", bg=bg_color)
        Frm6.place(x=0, y=560, relwidth=1, height=140)
        cosmt_price = Label(Frm6, text="Total Cosmetic Price", bg=bg_color, fg="white",
                            font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        cosmt_txt = Entry(Frm6, width=18, textvariable=self.cosmetics.price, font="arial 10 bold", bd=7,
                          relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        grcry_price = Label(Frm6, text="Total Grocery Price", bg=bg_color, fg="white",
                            font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        grcry_txt = Entry(Frm6, width=18, textvariable=self.grocery.price, font="arial 10 bold", bd=7,
                          relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        cld_price = Label(Frm6, text="Total Cold Drink Price", bg=bg_color, fg="white",
                          font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        cld_txt = Entry(Frm6, width=18, textvariable=self.coldDrink.price, font="arial 10 bold", bd=7,
                        relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        cosmt_tax = Label(Frm6, text="Cosmetic Tax", bg=bg_color, fg="white",
                          font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        cosmt_txt = Entry(Frm6, width=18, textvariable=self.cosmetics.tax, font="arial 10 bold", bd=7,
                          relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        grcry_tax = Label(Frm6, text="Grocery Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=1, column=2, padx=20, pady=1, sticky="w")
        grcry_txt = Entry(Frm6, width=18, textvariable=self.grocery.tax, font="arial 10 bold", bd=7,
                          relief=SUNKEN).grid(
            row=1, column=3, padx=10, pady=1)

        cld_tax = Label(Frm6, text="Drink Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=2, column=2, padx=20, pady=1, sticky="w")
        cld_txt = Entry(Frm6, width=18, textvariable=self.coldDrink.tax, font="arial 10 bold", bd=7,
                        relief=SUNKEN).grid(
            row=2, column=3, padx=10, pady=1)

        btnFrm = Frame(Frm6, bd=7, relief=GROOVE)
        btnFrm.place(x=750, width=580, height=105)

        totalBtn = Button(btnFrm, text="Total", command=self.total, bg="#46344E", fg="white", bd=2, pady=15, width=10,
                          font="arial 14 bold").grid(row=0, column=0, padx=5, pady=5)
        genBillBtn = Button(btnFrm, text="Generate Bill", command=self.bill_area, bg="#46344E", fg="white", bd=2,
                            pady=15, width=10, font="arial 14 bold").grid(row=0, column=1, padx=5, pady=5)
        clrBtn = Button(btnFrm, text="Clear", command=self.clear_data, bg="#46344E", fg="white", bd=2, pady=15,
                        width=10,
                        font="arial 14 bold").grid(row=0, column=2, padx=5, pady=5)
        exitBtn = Button(btnFrm, text="Exit", command=self.exit, bg="#46344E", fg="white", bd=2, pady=15, width=10,
                         font="arial 14 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_to_bill()

    def total(self):
        self.cosm_sp_pr = self.cosmetics.soap.get() * 40
        self.cosm_fc_pr = self.cosmetics.fcream.get() * 120
        self.cosm_fw_pr = self.cosmetics.fwash.get() * 60
        self.cosm_spry_pr = self.cosmetics.spray.get() * 150
        self.cosm_gel_pr = self.cosmetics.gel.get() * 140
        self.cosm_ltn_pr = self.cosmetics.ltn.get() * 180
        self.total_cosmetic_price = float(
            self.cosm_sp_pr +
            self.cosm_fc_pr +
            self.cosm_fw_pr +
            self.cosm_spry_pr +
            self.cosm_gel_pr +
            self.cosm_ltn_pr
        )
        self.cosmetics.price.set("PKR " + str(self.total_cosmetic_price))
        self.cosm_tax = round((self.total_cosmetic_price * 0.17), 2)
        self.cosmetics.tax.set("Rs. " + str(self.cosm_tax))

        self.grc_rice_pr = self.grocery.rice.get() * 125
        self.grc_oil_pr = self.grocery.oil.get() * 220
        self.grc_daal_pr = self.grocery.daal.get() * 60
        self.grc_wheat_pr = self.grocery.wheat.get() * 75
        self.grc_sugar_pr = self.grocery.sugar.get() * 100
        self.grc_tea_pr = self.grocery.tea.get() * 160
        self.total_grocery_price = float(
            self.grc_rice_pr +
            self.grc_oil_pr +
            self.grc_daal_pr +
            self.grc_wheat_pr +
            self.grc_sugar_pr +
            self.grc_tea_pr
        )
        self.grocery.price.set("PKR " + str(self.total_grocery_price))
        self.grc_tax = round((self.total_grocery_price * 0.17), 2)
        self.grocery.tax.set("Rs. " + str(self.grc_tax))

        self.drnk_cola_pr = self.coldDrink.cola.get() * 100
        self.drnk_sprt_pr = self.coldDrink.sprite.get() * 100
        self.drnk_fnta_pr = self.coldDrink.fanta.get() * 100
        self.drnk_mint_pr = self.coldDrink.mint.get() * 80
        self.drnk_lich_pr = self.coldDrink.lichee.get() * 50
        self.drnk_rooh_pr = self.coldDrink.rooh.get() * 180
        self.total_coldDrink_price = float(
            self.drnk_cola_pr +
            self.drnk_sprt_pr +
            self.drnk_fnta_pr +
            self.drnk_mint_pr +
            self.drnk_lich_pr +
            self.drnk_rooh_pr
        )
        self.coldDrink.price.set("PKR " + str(self.total_coldDrink_price))
        self.cld_tax = round((self.total_coldDrink_price * 0.17), 2)
        self.coldDrink.tax.set("Rs. " + str(self.cld_tax))

        self.Total_bill = float(
            self.total_cosmetic_price + self.total_grocery_price + self.total_coldDrink_price + self.cosm_tax + self.grc_tax + self.cld_tax)

    def welcome_to_bill(self):
        self.txtarea.delete("1.0", END)
        self.txtarea.insert(END, "\t         Al Fateh \n")
        self.txtarea.insert(END, "\t     Thanks For Shopping\n")
        self.txtarea.insert(END, f"\n Bill Number: {self.billNum.get()}\n")
        self.txtarea.insert(END, f"\n Customer Name: {self.customer.custName.get()}\n")
        self.txtarea.insert(END, f"\n Phone Number: {self.customer.custPhone.get()}\n")
        self.txtarea.insert(END, "=======================================")
        self.txtarea.insert(END, "\n Products\t\tQTY\t\tPrice\n")
        self.txtarea.insert(END, "=======================================")

    def bill_area(self):
        if self.customer.custName.get() == "" or self.customer.custPhone.get() == "":
            messagebox.showerror("Error", "Customer Details Are Mandatory")
        elif self.cosmetics.price.get() == "PKR 0.0" and self.grocery.price.get() == "PKR 0.0" and self.coldDrink.price.get() == "PKR 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_to_bill()
            # cosmetic section
            if self.cosmetics.soap.get() != 0:
                self.txtarea.insert(END, f"\n Bath Soap\t\t{self.cosmetics.soap.get()}\t\t{self.cosm_sp_pr}")
            if self.cosmetics.fcream.get() != 0:
                self.txtarea.insert(END, f"\n Face Cream\t\t{self.cosmetics.fcream.get()}\t\t{self.cosm_fc_pr}")
            if self.cosmetics.fwash.get() != 0:
                self.txtarea.insert(END, f"\n Face Wash\t\t{self.cosmetics.fwash.get()}\t\t{self.cosm_fw_pr}")
            if self.cosmetics.spray.get() != 0:
                self.txtarea.insert(END, f"\n Hair Spray\t\t{self.cosmetics.spray.get()}\t\t{self.cosm_spry_pr}")
            if self.cosmetics.gel.get() != 0:
                self.txtarea.insert(END, f"\n Hair Gel\t\t{self.cosmetics.gel.get()}\t\t{self.cosm_gel_pr}")
            if self.cosmetics.ltn.get() != 0:
                self.txtarea.insert(END, f"\n Body Lotion\t\t{self.cosmetics.ltn.get()}\t\t{self.cosm_ltn_pr}")
            # grocery section
            if self.grocery.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.grocery.rice.get()}\t\t{self.grc_rice_pr}")
            if self.grocery.oil.get() != 0:
                self.txtarea.insert(END, f"\n Oil\t\t{self.grocery.oil.get()}\t\t{self.grc_oil_pr}")
            if self.grocery.daal.get() != 0:
                self.txtarea.insert(END, f"\n Daal\t\t{self.grocery.daal.get()}\t\t{self.grc_daal_pr}")
            if self.grocery.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat\t\t{self.grocery.wheat.get()}\t\t{self.grc_wheat_pr}")
            if self.grocery.sugar.get() != 0:
                self.txtarea.insert(END, f"\n Sugar\t\t{self.grocery.sugar.get()}\t\t{self.grc_sugar_pr}")
            if self.grocery.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.grocery.tea.get()}\t\t{self.grc_tea_pr}")
            # cold drink section
            if self.coldDrink.cola.get() != 0:
                self.txtarea.insert(END, f"\n Coca Cola\t\t{self.coldDrink.cola.get()}\t\t{self.drnk_cola_pr}")
            if self.coldDrink.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.coldDrink.sprite.get()}\t\t{self.drnk_sprt_pr}")
            if self.coldDrink.fanta.get() != 0:
                self.txtarea.insert(END, f"\n Fanta\t\t{self.coldDrink.fanta.get()}\t\t{self.drnk_fnta_pr}")
            if self.coldDrink.mint.get() != 0:
                self.txtarea.insert(END, f"\n Margareta\t\t{self.coldDrink.mint.get()}\t\t{self.drnk_mint_pr}")
            if self.coldDrink.lichee.get() != 0:
                self.txtarea.insert(END, f"\n Lichee\t\t{self.coldDrink.lichee.get()}\t\t{self.drnk_lich_pr}")
            if self.coldDrink.rooh.get() != 0:
                self.txtarea.insert(END, f"\n Jam e Shireen\t\t{self.coldDrink.rooh.get()}\t\t{self.drnk_rooh_pr}")

            self.txtarea.insert(END, f"\n---------------------------------------")
            if self.cosmetics.tax.get() != "Rs 0.0 ":
                self.txtarea.insert(END, f"\nCosmetics Tax \t\t\t    {self.cosmetics.tax.get()} ")

            if self.grocery.tax.get() != "Rs 0.0 ":
                self.txtarea.insert(END, f"\nGrocery Tax \t\t\t    {self.grocery.tax.get()} ")

            if self.coldDrink.tax.get() != "Rs 0.0 ":
                self.txtarea.insert(END, f"\nCold Drinks Tax \t\t\t    {self.coldDrink.tax.get()} ")

            self.txtarea.insert(END, f"\nTotal \t\t\t    Rs. {self.Total_bill}")
            self.txtarea.insert(END, f"\n---------------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill")
        if op > 0:
            self.bill_data = self.txtarea.get("1.0", END)
            my_file = open("Bills/" + str(self.billNum.get()) + ".txt", "w")
            my_file.write(self.bill_data)
            my_file.close()
            messagebox.showinfo("Saved", f"Bill No. :{self.billNum.get()} saved successfully")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0] == self.searchBill.get():
                my_file = open(f"Bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in my_file:
                    self.txtarea.insert(END, d)
                my_file.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear")
        if op > 0:
            # Variables
            # cosmetics
            self.cosmetics.soap.set(0)
            self.cosmetics.fcream.set(0)
            self.cosmetics.fwash.set(0)
            self.cosmetics.spray.set(0)
            self.cosmetics.gel.set(0)
            self.cosmetics.ltn.set(0)
            # grocery
            self.grocery.rice.set(0)
            self.grocery.oil.set(0)
            self.grocery.daal.set(0)
            self.grocery.wheat.set(0)
            self.grocery.sugar.set(0)
            self.grocery.tea.set(0)
            # colddrink
            self.coldDrink.cola.set(0)
            self.coldDrink.sprite.set(0)
            self.coldDrink.fanta.set(0)
            self.coldDrink.mint.set(0)
            self.coldDrink.lichee.set(0)
            self.coldDrink.rooh.set(0)
            # total product and tax variables
            self.cosmetics.price.set("")
            self.grocery.price.set("")
            self.coldDrink.price.set("")

            self.cosmetics.tax.set("")
            self.grocery.tax.set("")
            self.coldDrink.tax.set("")
            # customer
            self.customer.custName.set("")
            self.customer.custPhone.set("")
            self.billNum.set("")
            x = random.randint(1000, 9999)
            self.billNum.set(str(x))
            self.searchBill.set("")
            self.welcome_to_bill()

    def exit(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.MyWindow.destroy()


MyWindow = Tk()
obj = BillApp(MyWindow)
MyWindow.mainloop()
