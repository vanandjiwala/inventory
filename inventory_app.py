from functools import partial
from tkinter import *
from tkcalendar import Calendar, DateEntry
from utils.db_utils import DbUtils
from products.products_master import ProductsMaster
import pandas as pd

import tkinter as tk

##Resources
# https://www.youtube.com/watch?v=wLi4LNCDDw8&ab_channel=PK%3AAnExcelExpertPK%3AAnExcelExpert
# https://www.youtube.com/watch?v=sI1oX1hgLm0&t=499s
# https://www.erplain.com/en/make-barcodes-and-skus

class MainApplication(tk.Frame):

    conn = None

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title('Stock Management')

        prod_val = StringVar()
        txn_val = StringVar()
        qty_val = IntVar()
        price_val = DoubleVar()
        df = pd.read_sql("select productname from Products", con=conn)
        product_list = df['productname'].tolist()
        txn_list = ['Purchase','Sell']

        txn_frame = LabelFrame(self.parent)
        txn_frame.grid(row=0, columnspan=18, sticky='ew', padx=5, pady=5, ipadx=5, ipady=5)

        product_name_label = Label(txn_frame, text="Product Name: ")
        product_name_label.grid(row=1, column=2, padx = 5 , pady = 5)
        product_name_dd = OptionMenu(txn_frame , prod_val , *product_list )
        product_name_dd.config(width= 20)
        product_name_dd.grid(row=1, column=3, padx = 5 , pady = 5)

        txn_type_label = Label(txn_frame, text="Transaction Type: ")
        txn_type_label.grid(row=1, column=6, padx = 5 , pady = 5)
        txn_type_dd = OptionMenu(txn_frame , txn_val , *txn_list )
        txn_type_dd.config(width=15)
        txn_type_dd.grid(row=1, column=8, padx = 5 , pady = 5)

        qty_label = Label(txn_frame, text="Qty: ")
        qty_label.grid(row=2, column=2, padx = 5 , pady = 5)
        qty_input = Entry(txn_frame, textvariable= qty_val)
        qty_input.grid(row=2, column=3, padx = 5 , pady = 5)

        price_label = Label(txn_frame, text="Price: ")
        price_label.grid(row=2, column=6, padx = 5 , pady = 5)
        price_input = Entry(txn_frame, textvariable= price_val)
        price_input.grid(row=2, column=8, padx = 5 , pady = 5)

        cal_label = Label(txn_frame, text="Date (MM/DD/YY): ")
        cal_label.grid(row=3, column=2, padx = 5 , pady = 5)
        cal = DateEntry(txn_frame,width=30,bg="darkblue",fg="white",year=2010,day=22,month=3)
        cal.grid(row=3, column=3, padx=5, pady=5)

        add_button = Button(txn_frame, text="Add", width=30)
        add_button.grid(row=3, column=6, columnspan=3, padx=30)

        # prod_button = Button(btn_frame, text="Products", width=30,command=partial(ProductsMaster.product_window,self,self.parent,conn))
        # prod_button.grid(row=1, column=2, columnspan=3, padx=30)
        #
        # export_button = Button(btn_frame, text="Export", width=30)
        # export_button.grid(row=1, column=8, columnspan=3, padx=30)

        btn_frame = LabelFrame(self.parent, pady=20)
        btn_frame.grid(row=4, columnspan=18, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

        prod_button = Button(btn_frame, text="Products", width=30,command=partial(ProductsMaster.product_window,self,self.parent,conn))
        prod_button.grid(row=4, column=2, columnspan=3, padx=30)

        export_button = Button(btn_frame, text="Export", width=30)
        export_button.grid(row=4, column=8, columnspan=3, padx=30)


if __name__ == "__main__":

    #DB Connections
    dbutils = DbUtils()
    conn = dbutils.connect_db()
    root = tk.Tk()
    root.geometry("700x600")
    root.pack_propagate(0)
    app = MainApplication(root)
    app.conn = conn
    root.mainloop()