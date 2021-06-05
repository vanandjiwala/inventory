from tkinter import *
from tkinter.ttk import *
from functools import partial
from pandastable import Table
import pandas as pd

class VendorMaster:

    def get_vendors(self):
        print("Vedndors Get")

    def delete_vendor(self):
        print("Vendors delete")

    def update_vendors(self):
        print("Vendor Edit")

    def add_vendor(self, vendor_dict):
        print(vendor_dict)


    def vendor_window(self,master,conn):
        vendor_name = StringVar()

        df = pd.read_sql("select * from Vendors",con=conn)

        newWindow = Toplevel(master)
        # sets the title of the
        # Toplevel widget
        newWindow.title("Vendors")
        # sets the geometry of toplevel
        newWindow.geometry("600x600")
        form_frame = LabelFrame(newWindow)
        form_frame.grid(row=0, columnspan=18, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

        vendor_name_label = Label(form_frame, text="Vendor Name: ")
        vendor_name_label.grid(row=1, column=2, padx = 5 , pady = 5)
        vendor_name_input = Entry(form_frame, textvariable= vendor_name)
        vendor_name_input.grid(row=1, column=3, padx = 5 , pady = 5)



        vendor_info = {
            'name': vendor_name
        }


        button_frame = LabelFrame(newWindow)
        button_frame.grid(row=3, columnspan=18, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

        prod_button = Button(button_frame, text="Add", width=20,command=partial(VendorMaster.add_vendor,self,vendor_info))
        prod_button.grid(row=4, column=1, columnspan=3, padx=30)

        # prod_update_button = Button(button_frame, text="Update", width=20,command=partial(ProductsMaster.update_product,self))
        # prod_update_button.grid(row=4, column=4, columnspan=3, padx=30)
        #
        # prod_delete_button = Button(button_frame, text="Delete", width=20,command=partial(ProductsMaster.delete_product,self))
        # prod_delete_button.grid(row=4, column=8, columnspan=3, padx=30)
        #
        vendors_frame = LabelFrame(newWindow)
        vendors_frame.grid(row=5, columnspan=18, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)


        pt = Table(vendors_frame)
        pt.model.df = df
        pt.show()


