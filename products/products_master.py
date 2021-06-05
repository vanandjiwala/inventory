from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from functools import partial
from pandastable import Table
from vendors.vendors_master import VendorMaster
import pandas as pd

class ProductsMaster:

    def get_products(self):
        print("Product delete")

    def delete_product(self):
        print("Product delete")

    def update_product(self):
        print("Product Edit")

    def add_product(self, product_dict, conn, vendor_df, window, master):
        name = product_dict['name'].get()
        desc = product_dict['desc'].get()
        vendor = product_dict['vendor'].get()
        price = product_dict['price'].get()

        id = vendor_df[vendor_df['vendorname'] == vendor].iloc[0]['id']
        query = """INSERT INTO Products('productname', 'productdesc', 'unitprice', 'vendorid') VALUES('{}', '{}', {},{});""".format(name,desc,price,id)
        print(query)
        try:
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
        except:
            print("Something went wrong inserting the data. Please try again")

        messagebox.showinfo("showinfo", "Information")
        window.destroy()
        ProductsMaster.product_window(window,master,conn)





    def product_window(self,master,conn):
        product_name = StringVar()
        product_desc = StringVar()
        product_price = DoubleVar()
        vendor_val = StringVar()

        df = pd.read_sql("select * from Vendors",con=conn)
        df1 = pd.read_sql("select p.id,productname,productdesc,unitprice,vendorname from Products p left join Vendors v on p.vendorid = v.id",con=conn)
        vendors = df['vendorname'].tolist()
        print(vendors)

        newWindow = Toplevel(master)
        # sets the title of the
        # Toplevel widget
        newWindow.title("Products")
        # sets the geometry of toplevel
        newWindow.geometry("730x600")
        form_frame = LabelFrame(newWindow)
        form_frame.grid(row=0, columnspan=18, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

        prod_name_label = Label(form_frame, text="Product Name: ")
        prod_name_label.grid(row=1, column=2, padx = 5 , pady = 5)
        prod_name_input = Entry(form_frame, textvariable= product_name)
        prod_name_input.grid(row=1, column=3, padx = 5 , pady = 5)

        prod_desc_label = Label(form_frame, text="Product Description: ")
        prod_desc_label.grid(row=1, column=4, padx = 5 , pady = 5)
        prod_desc_input = Entry(form_frame, textvariable= product_desc, width=50)
        prod_desc_input.grid(row=1, column=5, padx = 5 , pady = 5)

        vendor_name_label = Label(form_frame, text="Vendor Name: ")
        vendor_name_label.grid(row=2, column=2, padx = 5 , pady = 5)
        vendor_name_dd = OptionMenu( form_frame , vendor_val ,vendors[0], *vendors )
        vendor_name_dd.grid(row=2, column=3, padx = 5 , pady = 5)

        prod_price_label = Label(form_frame, text="Product Price: ")
        prod_price_label.grid(row=2, column=4, padx = 5 , pady = 5)
        prod_price_input = Entry(form_frame, textvariable= product_price)
        prod_price_input.grid(row=2, column=5, padx = 5 , pady = 5)

        # prod_button = Button(form_frame, text="Add Vendor", width=20,command=partial(VendorMaster.vendor_window,self,master,conn))
        # prod_button.grid(row=3, column=1, columnspan=3, padx=30)




        product_info = {
            'name': product_name,
            'desc': product_desc,
            'vendor': vendor_val,
            'price': product_price
        }

        # cur = conn.cursor()
        # cur.execute("""select sql from sqlite_master where type = 'table'""")
        # print(cur.fetchall())

        button_frame = LabelFrame(newWindow)
        button_frame.grid(row=4, columnspan=18, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

        prod_button = Button(button_frame, text="Add", width=20,
                             command=partial(ProductsMaster.add_product, self, product_info, conn, df, newWindow, master))
        prod_button.grid(row=5, column=1, columnspan=3, padx=30)

        # prod_update_button = Button(button_frame, text="Update", width=20,command=partial(ProductsMaster.update_product,self))
        # prod_update_button.grid(row=5, column=4, columnspan=3, padx=30)
        #
        # prod_delete_button = Button(button_frame, text="Delete", width=20,command=partial(ProductsMaster.delete_product,self))
        # prod_delete_button.grid(row=5, column=8, columnspan=3, padx=30)

        products_frame = LabelFrame(newWindow)
        products_frame.grid(row=6, columnspan=18, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

        # data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        #         'Age': [20, 21, 19, 18]}
        #
        # # Create DataFrame
        # df = pd.DataFrame(data)

        pt = Table(products_frame,showstatusbar=True)
        pt.model.df = df1
        pt.autoResizeColumns()
        pt.show()

        def handle_left_click(event):
            """Handle left click"""
            rowclicked_single = pt.get_row_clicked(event)
            print(rowclicked_single)
            pt.setSelectedRow(rowclicked_single)
            pt.redraw()

        pt.rowheader.bind('<Button-1>', handle_left_click)


