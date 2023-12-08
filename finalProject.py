# IMPORTSs

from tkinter.ttk import *
import io
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sys
from tkinter import filedialog
import random
import sqlite3
import random
from datetime import datetime
import time
from datetime import timedelta
import sqlite3

###########
################################################################

# Create a new window using the Tkinter library.
# - Set the width of the window to 400 pixels.
# - Set the height of the window to 600 pixels.
# - Set the maximum size of the window to the specified width and height.
# - Set the minimum size of the window to the specified width and height.
# - Set the title of the window to 'SPARduct'.
# - Set the window to be displayed without the window manager decorations.

window = Tk()
WINDOW_WIDTH = 400
WINDOW_HEIGTH = 600
window.maxsize(WINDOW_WIDTH, WINDOW_HEIGTH)
window.minsize(WINDOW_WIDTH, WINDOW_HEIGTH)
window.title('SPARduct')
window.overrideredirect(True)
# window.wm_attributes("-transparentcolor", "#deb887")

accounts_list = []
################################################################

# The variable `tk_font` is set to the string "Calibre". This is likely used to specify the font to be used in a Tkinter application.
tk_font = "Calibre"
bgcolor = "#eeeeee"
text_color = "red"
user_index = 0
nums = 1
######################### LISTS
user_product_listsaction_list = []  # Create an empty list to store user product lists.
trans_code = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
num = 0
DATE = datetime.now().date().today()
_time = time.localtime(time.time())  # Get the current local time and store it in the variable `_time`.
prd_key = 0
product_list = []
transaction_list = []

position = 200
cart_position = 200
search_frame_pos = 200
search_types_id = []
carts_id = []
gap_val = (WINDOW_WIDTH - 340) // 3
gap_val += 20
x_position = gap_val + 20  # Calculate the x position by adding the value of `gap_val` to 20.

search_datas = []


class Constant_scroll_pos():
    Y_POSITION = 110
    GAP_VAL = (WINDOW_WIDTH - 340) // 3
    GAP_VAL += 65
    X_POSITION = GAP_VAL + 20  # Calculate the x Y_POSITION by adding the value of `GAP_VAL` to 20.
    CHECK_POS_X = 190 + X_POSITION
    SCROLL_Y_VAL_OF_PRDCTS = 200


history_id_list = []
product_pos = Constant_scroll_pos()  # constant for scroll Y_POSITION of products page
search_pos = Constant_scroll_pos()  # constant for scroll Y_POSITION of searched page
history_pos = Constant_scroll_pos()  # constant for scroll Y_POSITION of history page
history_pos.Y_POSITION = 90
history_pos.SCROLL_Y_VAL_OF_PRDCTS = 110
history_pos.X_POSITION = 200

trans_pos = Constant_scroll_pos()  # constant for scroll Y_POSITION of searched page
trans_pos.Y_POSITION = 90
trans_pos.SCROLL_Y_VAL_OF_PRDCTS = 110
trans_pos.X_POSITION = 200

admin_accs_pos = Constant_scroll_pos()  # constant for scroll Y_POSITION of searched page
admin_accs_pos.Y_POSITION = 40
admin_accs_pos.SCROLL_Y_VAL_OF_PRDCTS = 20
admin_accs_pos.X_POSITION = 200

admin_inven_pos = Constant_scroll_pos()  # constant for scroll Y_POSITION of searched page
admin_inven_pos.Y_POSITION = 35
admin_inven_pos.SCROLL_Y_VAL_OF_PRDCTS = 10
admin_inven_pos.X_POSITION = 200

admin_trans_pos = Constant_scroll_pos()  # constant for scroll Y_POSITION of searched page
admin_trans_pos.Y_POSITION = 70
admin_trans_pos.SCROLL_Y_VAL_OF_PRDCTS = 90
admin_trans_pos.X_POSITION = 200


################################################################
def size_check():
    """
    Check the size of the window and update the global variable `WINDOW_WIDTH` with the new width.

    """
    global WINDOW_WIDTH
    width = window.winfo_width()
    WINDOW_WIDTH = width
    window.update()


try:
    def open_id_image():
        """
        Open a file dialog to allow the user to select an image file for identification purposes.
        global id_picture - the path of the selected image file
        """
        global id_picture
        id_picture = filedialog.askopenfilename()
except:
    messagebox.showerror("Error", 'Please fill in all the required fields to create an account')


def upload_image_function():
    """
    This function allows the user to upload an image file. It opens a file dialog to select the image file and stores the file path in the global variable `product_img`.

    """
    try:
        global product_img
        product_img = filedialog.askopenfilename()
    except Exception as e:
        messagebox.showerror("Sign in error", "May kulang !\n Ayusin mo")


def on_mouse_wheel(event):
    """
    This function is called when a mouse wheel event occurs. It scrolls the view of a product frame by a certain number of units based on the direction and magnitude of the mouse wheel movement.
    event - the mouse wheel event

    """
    product_frame.yview_scroll(int(-1 * (event.delta / 120)), "units")


############ ACCOUNTS
class Accounts():
    """
    A class representing user accounts.
    """

    def __init__(self, id_pic, name, address, username, password):
        """
        Initialize a user object with the given attributes.
        id_pic - the ID picture of the user
        name - the name of the user
        address - the address of the user
        username - the username of the user
        password - the password of the user
        None
        """
        self.username = username
        self.password = password
        self.name = name
        self.address = address
        self.id_pic = id_pic
        self.user_product_list = []
        self.product_indx = 0
        self.transaction_list = []

        self.my_container_of_product = []

        self.date = datetime.now().date()  # create current date

        self.mytransaction_frame = Canvas(user_transaction_frame, width=WINDOW_WIDTH,
                                          height=400, scrollregion=(0, 0, 200, 200))  # frame for user transaction
        self.tran_background = Label(self.mytransaction_frame, image=user_frame_bg_img)
        self.tran_background.pack()

        self.my_products_frame = Canvas(my_product_container, width=WINDOW_WIDTH,
                                        height=WINDOW_HEIGTH,
                                        scrollregion=(0, 0, 200, 200))  # frame for user transaction
        self.myP_background = Label(self.my_products_frame, image=user_frame_bg_img)
        self.myP_background.pack()
        self.my_prod_pos = Constant_scroll_pos()  # constant for scroll Y_POSITION of my product page
        self.my_prod_pos.Y_POSITION = 90
        self.my_prod_pos.SCROLL_Y_VAL_OF_PRDCTS = 110
        self.my_prod_pos.X_POSITION = 200

        self.my_cart_frame = Canvas(cart_frame, width=WINDOW_WIDTH,
                                    height=500, bg='blue', scrollregion=(0, 0, 200, 200))  # frame for user transaction
        self.background = Label(self.my_cart_frame, image=user_frame_bg_img)
        self.background.pack()

        self.history_scroll = 100

    def unpack_view_Prof(self):
        for prod in self.user_product_list:
            prod.unview_profile()

    def hisroty_frame_wheel(self, event):
        self.my_cart_frame.yview_scroll(-1 * (event.delta // 120), "units")

    def trans_frame_wheel(self, event):
        self.mytransaction_frame.yview_scroll(-1 * (event.delta // 120), "units")

    def myP_frame_wheel(self, event):
        self.my_products_frame.yview_scroll(-1 * (event.delta // 120), "units")

    # Getter methods to retrieve specific user details
    def get_img(self):
        return self.id_pic

    def get_date(self):
        return self.date

    def get_user_name(self):
        return self.name

    def get_user_address(self):
        return self.address

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_id(self):
        return self.id_pic

    ##########
    def add_product(self, product_img, product_name, product_price, product_stock, seller_contact):
        """
        Add a new product to the database.
        product_img - the image of the product
        product_name - the name of the product
        product_price - the price of the product
        product_stock - the stock of the product
        seller_contact - the contact information of the seller

        """
        global prd_key
        global user_index
        conn = sqlite3.connect("Products.db")
        c = conn.cursor()
        c.execute("SELECT * FROM products")
        key = 0
        for x in c.fetchall():
            key = x[0]
        print("key = ", key)
        if key < prd_key:
            prd_key = key + 1
            print("prd key  change", prd_key)
        conn.commit()
        conn.close()
        print("prd before adding", prd_key)
        with open(product_img, 'rb') as image_file:
            product_img = image_file.read()
        product = Products(sqlite3.Binary(product_img), product_name, product_price, product_stock, seller_contact,
                           user_index, prd_key,
                           self.product_indx)
        product.display_to_myproduct_frame()
        product.show_profile_frame(self.id_pic, self.name, self.address)
        product.save()

        current_user().user_product_list.append(product)
        prd_key += 1
        print("prd after adding ", prd_key)
        window.update()
        self.product_indx += 1

    def unshow_my_products(self):
        """
        Hide all products in the user's product list.
        self - the instance of the class
        """
        for items in self.user_product_list:
            items.unshow()

    def show_user_products(self):
        """
        Display the products owned by the user.

        """
        global user_index
        for items in self.user_product_list:
            if items == None:
                pass
            else:
                items.show_my_product()
                window.update()

    def show_cart(self):
        """
        Display the cart for the current user and hide the carts for other users.
        """
        pass

    def unshow_cart(self):
        """
        Hide the cart items from the screen by using the `pack_forget()` method on each item in the `cart_list`.
        """
        pass

    def show_my_transaction(self):
        """
        Display the "mytransaction_frame" widget on the screen.
        """
        self.mytransaction_frame.pack(fill=BOTH)


class Products(Accounts):
    """
    This code defines a class named "Products" that inherits from a class named "Accounts".
    """

    def __init__(self, image_of_product, product_type, product_price, product_stock, seller_contact, product_index,
                 id_num,
                 prd_indx):
        # Initialize an instance of a product with the given attributes.
        # image_of_product - the image of the product
        # product_type - the type of the product
        # product_price - the price of the product
        # product_stock - the stock of the product
        # seller_contact - the contact information of the seller
        # product_index - the index of the product
        # id_num - the identification number of the product
        # prd_indx - the index of the product (same as product_index)
        # return None

        self.product_quan_f = None
        global user_index
        # global position_y
        global date
        global product_img
        global window
        global con_bg_img
        global background_of_prod_frame
        global product_frame

        # Initialize a new object of the current class by calling the superclass's constructor with the following parameters:
        super().__init__(current_user().get_id(),
                         # - The ID obtained from the `accounts_list` at the index `user_index`.
                         current_user().get_user_name(),
                         # - The user name obtained from the `accounts_list` at the index `user_index`.
                         current_user().get_user_address(),
                         # - The user address obtained from the `accounts_list` at the index `user_index`.
                         current_user().get_username(),
                         # - The username obtained from the `accounts_list` at the index `user_index`.
                         current_user().get_password())  # - The password obtained from the `accounts_list` at the index `user_index`.

        ###### quantinty value
        self.new_quan = StringVar()
        # products components
        self.prd_indx = prd_indx
        self.covert_to_img = Image.open(io.BytesIO(image_of_product))
        self.covert_to_img = self.covert_to_img.resize((130, 130))
        convert_to_img = create_img(io.BytesIO(image_of_product), 130, 130)
        self.product_image_self = create_img(io.BytesIO(image_of_product), 100, 100)
        self.product_image_His = create_img(io.BytesIO(image_of_product), 150, 150)

        # image for buy frame
        self.img = self.covert_to_img.resize((250, 250))
        self.img = ImageTk.PhotoImage(self.img)

        self.product_image = convert_to_img
        self.image_of_product = image_of_product
        self.id_num = id_num
        self.product_type = product_type
        self.product_price = int(product_price)
        self.product_stock = int(product_stock)
        self.seller_contact = seller_contact
        self.product_index = product_index

        # time
        self.local_t = time.localtime()
        self.date_posted = datetime.now().date()
        self.time_posted = time.strftime("%H:%M:%S", self.local_t)

        # ============================================================ products frame, labels and buttons
        gap_value = 0
        self.product_frame = None
        self.product_container = Canvas(product_frame,
                                        bg='#f3f3f3',
                                        scrollregion=(0, 0, 400, 400),
                                        highlightcolor="black",
                                        highlightbackground="black",
                                        highlightthickness=2
                                        )
        self.product_bg_image = None
        self.product_bg_image = self.product_container.create_image(85, 85, image=con_bg_img)  # display container image
        self.product_image_con = Label(self.product_container, image=self.product_image, highlightthickness=2,
                                       highlightcolor="black", highlightbackground='black')
        self.product_image_con.place(x=20, y=15)  # display product image
        self.price_txt = None
        # ============================================================ hOVER
        self.hover_label = Canvas(self.product_container)
        buy_btn = self.hover_label.create_image(85, 140, image=buy_img)
        self.price_txt = self.hover_label.create_text(85, 85, text=f"Price: PHP {self.product_price}",
                                                      font=("Arial Black", 9, "bold"), fill="black")
        self.hover_label.tag_bind(buy_btn, '<Button>', lambda event: self._add_tocart())
        self.product_container.bind('<Enter>', lambda event: self.hover_product())
        self.product_container.bind('<Leave>', lambda event: self.unhover_product())

        # ============================================================
        self.insert_to()  # insert to database Products
        # ============================================================ search products frame, labels and buttons
        search_gap_value = 0
        self.search_product_frame = None
        self.search_product_container = Canvas(search_frame_container, bg='#f3f3f3', scrollregion=(0, 0, 400, 400),
                                               highlightcolor='black', highlightbackground='black',
                                               highlightthickness=2)
        self.search_product_bg_image = None
        self.search_product_bg_image = self.search_product_container.create_image(85, 85,
                                                                                  image=con_bg_img)  # display container image
        self.search_product_image_con = Label(self.search_product_container, image=self.product_image,
                                              highlightthickness=2,
                                              highlightcolor="black", highlightbackground='black')
        self.search_product_image_con.place(x=20, y=15)  # display product image
        self.search_price_txt = None
        # ============================================================ hOVER
        self.search_hover_label = Canvas(self.search_product_container)
        search_buy_btn = self.search_hover_label.create_image(85, 140, image=buy_img)
        self.search_price_txt = self.search_hover_label.create_text(85, 85, text=f"Price: PHP {self.product_price}",
                                                                    font=("Arial Black", 9, "bold"), fill="black")
        self.search_hover_label.tag_bind(search_buy_btn, '<Button>', lambda event: self._add_tocart())
        self.search_product_container.bind('<Enter>', lambda event: self.hover_search_product())
        self.search_product_container.bind('<Leave>', lambda event: self.unhover_search_product())

        # ==============================================================
        self.cart_f = Canvas(current_user().my_cart_frame)
        # ==============================================================
        # transaction frame
        self.transaction_f = Canvas(accounts_list[self.product_index].mytransaction_frame)
        # trasaction history list
        # ============================================================ create seller profile frame
        self.frame = Canvas(user_frame)

        # self.button_exit_prof = Button(self.frame, command=self.profile_unview, text="X")

        # self.info_label = Label(self.frame,
        #                       text=f"Name:{self.get_user_name()}\nAge:{self.get_age()}\nAddress:{self.get_user_address()}")
        # self.label.pack()
        # self.info_label.pack()
        # self.button_exit_prof.pack()
        # ============================================================
        # myproducts frame
        self.myproduct_container = None
        # date delivever
        self.time_of_deliver = datetime.now().date().today() + timedelta(days=(int(_time.tm_wday) + 5))

    def hover_product(self):  # show this when enter the cursor to the products container
        """
        Create a hover effect for a product container.
        """
        self.crt_hover_bg = self.product_container.create_window(85, 85, window=self.hover_label, width=170, height=170)
        self.product_container.config(highlightbackground="red", highlightcolor="red", highlightthickness=3, bd=0)
        self.hover_label.bind("<Configure>",
                              lambda e: self.product_container.configure(
                                  scrollregion=self.product_container.bbox("all")))
        self.hover_label.bind_all("<MouseWheel>", self.on_mousewheel_prdcts_F)

    def unhover_product(self):  # Leave the cursor from the product
        """
        Remove the hover effect from a product container.
        """
        self.product_container.delete(self.crt_hover_bg)
        self.product_container.config(highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)

    def hover_search_product(self):  # show this when enter the cursor to the products container
        """
        Create a hover effect for a product container.
        """
        self.search_crt_hover_bg = self.search_product_container.create_window(85, 85, window=self.search_hover_label,
                                                                               width=170, height=170)
        self.search_product_container.config(highlightbackground="red", highlightcolor="red", highlightthickness=2,
                                             bd=0)

    def unhover_search_product(self):  # Leave the cursor from the product
        """
        Remove the hover effect from a product container.
        """
        self.search_product_container.delete(self.search_crt_hover_bg)
        self.search_product_container.config(highlightcolor='black', highlightbackground='black', highlightthickness=2,
                                             bd=0)

    def on_mousewheel_prdcts_SF(self, event):
        """
        This function is an event handler for the mousewheel event in a product frame. It scrolls the view of the product frame based on the delta value of the event.
        """
        search_frame_container.yview_scroll(-1 * (event.delta // 120), "units")

    def save(self):
        """
        Save the current product information to a SQLite database.
        """
        global user_index
        global product_img
        conn = sqlite3.connect("Products.db")
        c = conn.cursor()

        product = [self.image_of_product, self.product_type, self.product_price, self.product_stock,
                   self.seller_contact, self.product_index]
        c.executemany(
            "INSERT INTO  products (product_img,product_type,product_price,product_stock,seller_contact,product_index) VALUES (?,?,?,?,?,?)",
            (product,))

        conn.commit()
        conn.close()

    def get_index(self):
        """
        Return the product index of an object.
        """
        return self.product_index

    def show(self):
        """
        Display the product information and handle key events.
        """
        global product_frame
        product_frame.bind("<Key>", self.move)
        index = user_index
        conn = sqlite3.connect("Products.db")
        c = conn.cursor()
        if self.product_stock <= 0:
            """
            Check if the product stock is less than or equal to zero. If so, delete the product from the database, update the UI to indicate that the product is sold out, disable the buy button, and hide the product container. If the product stock is greater than zero, do nothing.
            """
            delete = f"DElETE FROM products WHERE id={self.id_num}"
            c.execute(delete)
            conn.commit()
            conn.close()
            self.my_Pinfo.config(text=f"SOLD OUT")
            self.product_container.pack_forget()
            self.myproduct_container.pack_forget()

        else:
            pass
        conn.commit()
        conn.close()

    def remove_product(self):
        print("prd remove", self.id_num)
        self.myproduct_container.pack_forget()
        conn = sqlite3.connect("Products.db")
        c = conn.cursor()
        delete = f"DElETE FROM products WHERE id={self.id_num}"
        c.execute(delete)
        remove_in_user_product_list(self.product_indx)

        conn.commit()
        conn.close()
        window.update()

    def show_profile_frame(self, image, username, address):
        # self.label = Label(self.frame, image=self.id_pic)
        self.con = Canvas(self.frame, highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=1,
                          width=280, height=350)
        self.con.create_image(200, 280, image=wel_bg)
        self.con.create_image(140, 100, image=image)
        self.back_to_btn = self.frame.create_image(20, 20, image=back_to_img)
        self.frame.tag_bind(self.back_to_btn, "<Button>", lambda event: self.profile_unview())  # back button
        self.con.create_text(140, 210, font=("Monoscape", 20, "bold"), text=f"{username}")
        self.con.create_text(170, 240, font=("Monoscape", 15, "bold"), text=f"{address}")
        self.con.place(x=60, y=100)

    def display_to_myproduct_frame(self):
        self.myproduct_container = Canvas(current_user().my_products_frame, width=WINDOW_WIDTH - 40)

        myproduct_img = Label(self.myproduct_container, image=self.product_image_self,
                              highlightcolor="black",
                              highlightthickness=2,
                              highlightbackground="black")
        myproduct_img.image = self.product_image_self

        # cart_user_frame.create_text(250,100,text="hahaha")

        text_label_MyP = Canvas(self.myproduct_container, width=175, height=200, highlightcolor="black",
                                highlightbackground="black", highlightthickness=2)
        text_label_MyP.create_image(88, 100, image=img_bg_txt)
        text_label_MyP.create_text(80, 50, font=('Times', 10),
                                   text=f"Type:{self.product_type}\nPrice:{self.product_price}\nStock:{self.product_stock}")
        text_label_MyP.pack(side='right')
        frame_id = current_user().my_products_frame.create_window(
            current_user().my_prod_pos.X_POSITION,
            current_user().my_prod_pos.Y_POSITION,
            width=WINDOW_WIDTH - 111,
            window=self.myproduct_container,
            height=100)
        history_id_list.append(frame_id)
        myproduct_img.pack(side='left')

        # create binding function for background
        self.myproduct_container.bind_all("<Configure>",
                                          lambda e: self.myproduct_container.configure(
                                              scrollregion=self.myproduct_container.bbox("all")))
        self.myproduct_container.bind("<MouseWheel>", current_user().myP_frame_wheel)
        text_label_MyP.bind_all("<Configure>",
                                lambda e: self.myproduct_container.configure(
                                    scrollregion=self.myproduct_container.bbox("all")))
        text_label_MyP.bind("<MouseWheel>", current_user().myP_frame_wheel)
        current_user().myP_background.bind_all("<Configure>",
                                               lambda e: self.myproduct_container.configure(
                                                   scrollregion=self.myproduct_container.bbox("all")))
        current_user().myP_background.bind("<MouseWheel>", current_user().myP_frame_wheel)
        myproduct_img.bind_all("<Configure>",
                               lambda e: self.myproduct_container.configure(
                                   scrollregion=self.myproduct_container.bbox("all")))
        myproduct_img.bind("<MouseWheel>", current_user().myP_frame_wheel)

        current_user().my_products_frame.bind_all("<Configure>",
                                                  lambda e: self.myproduct_container.configure(
                                                      scrollregion=self.myproduct_container.bbox("all")))
        current_user().my_products_frame.bind("<MouseWheel>", current_user().myP_frame_wheel)
        # add cart to user window
        current_user().my_prod_pos.SCROLL_Y_VAL_OF_PRDCTS += 120
        current_user().my_prod_pos.Y_POSITION += 120
        update_scroll_Y(current_user().my_products_frame,
                        current_user().my_prod_pos.SCROLL_Y_VAL_OF_PRDCTS)

    def display_to_search_frame(self):
        global product_pos
        # global SEARCH_X_POSITION, SEARCH_POSITION, SEARCH_GAP_VAL, SEARCH_SCROLL_Y_VAL_OF_PRDCTS

        self.search_product_frame = search_frame_container.create_window((search_pos.X_POSITION, search_pos.Y_POSITION),
                                                                         window=self.search_product_container,
                                                                         width=170, height=170)
        search_datas.append(self.search_product_frame)

        # create binding function for product container
        self.search_product_container.bind_all("<Configure>",
                                               lambda e: self.search_product_container.configure(
                                                   scrollregion=self.search_product_container.bbox("all")))
        self.search_product_container.bind_all("<MouseWheel>", self.on_mousewheel_prdcts_SF)

        check_position_of_searched_prodcuts()

        # self.product_container.config(width=WINDOW_WIDTH)

    def move(self, event):
        """
        Move the product container widget by changing its x and y coordinates.
        event - the event that triggered the move
        """
        self.product_container.place(x=200, y=self.product_container.winfo_y() + 10)
        window.update()

    def insert_to(self):
        """
        This method is used to insert a product frame into a container. It sets the position and size of the product frame, binds events for scrolling, and updates the position variables for the next insertion.
        """
        global con_bg_img
        global gap_val
        global product_frame
        global background_of_prod_frame
        self.product_frame = product_frame.create_window((product_pos.X_POSITION, product_pos.Y_POSITION),
                                                         window=self.product_container,
                                                         width=170, height=170)
        # create binding function for background
        background_of_PF.bind("<Configure>",
                              lambda e: self.product_container.configure(
                                  scrollregion=self.product_container.bbox("all")))
        background_of_PF.bind("<MouseWheel>", self.on_mousewheel_prdcts_F)
        # create binding function for product container
        self.product_container.bind("<Configure>",
                                    lambda e: self.product_container.configure(
                                        scrollregion=self.product_container.bbox("all")))
        self.product_container.bind("<MouseWheel>", self.on_mousewheel_prdcts_F)
        self.product_container.bind_all("<Configure>",
                                        lambda e: self.product_container.configure(
                                            scrollregion=self.product_container.bbox("all")))
        self.product_container.bind_all("<MouseWheel>", self.on_mousewheel_prdcts_F)

        check_position_of_prodcuts()

    def on_mousewheel_prdcts_F(self, event):
        """
        This function is an event handler for the mousewheel event in a product frame. It scrolls the view of the product frame based on the delta value of the event.
        """
        product_frame.yview_scroll(-1 * (event.delta // 120), "units")
        print("bindd")

    def unpack(self):
        """
        Hide the product container and the myproduct container by removing them from the display.
        """
        self.product_container.pack_forget()
        self.myproduct_container.pack_forget()

    def show_my_product(self):
        """
        Display the product information and image on the screen. If the product is out of stock, remove it from the database and disable the buy button. Otherwise, display the product image, information, and remove button.
        """
        if self.product_stock <= 0:
            conn = sqlite3.connect("Products.db")
            c = conn.cursor()
            delete = f"DElETE FROM products WHERE id={self.id_num}"
            c.execute(delete)
            conn.commit()
            conn.close()
            conn.commit()
            conn.close()
        else:
            self.myproduct_image_f.pack()
            self.my_Pinfo.pack()
            self.myproduct_container.pack()
            self.remove_button.pack()

    def _add_tocart(self):
        """
        This method is used to add a product to the user's shopping cart. It updates the GUI to display the product information and allows the user to select the quantity and payment method for the transaction.
        """
        global cart_position
        # global list_p
        global user_index
        unpack_all_frame_in_userframe()

        buy_frame.place(x=10, y=10)

        buy_frame.itemconfig(product_info_BF,
                             text=f"\nPrice: PHP{self.product_price}\nType: {self.product_type}\nStock: {self.product_stock}")
        product_picture.config(image=self.img)
        buy_frame.itemconfig(payment_txt, text=f"Payment: 0")

        buy_frame.tag_bind(view_profile_button, "<Button>", lambda event: self.profile_view())
        # amount.config(text=str('PHP' + str(self.product_price)))
        quan_menu.config(textvariable=self.new_quan, from_=0, to=self.product_stock)
        buy_frame.tag_bind(buy_button, "<Button>",
                           lambda event: self.transaction_method(
                               self.product_stock - int(quan_menu.get())))  # create command for buy button
        self.change_payment()

    def change_payment(self):
        """
        This method is used to update the payment amount based on the quantity entered by the user. It handles different scenarios such as when the quantity is greater than the available stock, when the quantity is zero, and when the quantity is a valid number.
        """
        try:
            """
            Try to perform the following operations:
            - Check if the value entered in `self.new_quan` is greater than the available stock (`self.product_stock`). If it is, display a message indicating that the stock is out of range.
            - Check if the value entered in `self.new_quan` is equal to 0. If it is, display a message indicating that the payment is PHP 0.
            - If neither of the above conditions are met, calculate the payment by multiplying the value entered in `self.new_quan` by `self.product_price` and display it as "Payment: PHP {payment}".
            - If any of the above operations result in a `ValueError`, display a message indicating that the payment is PHP 0
            """
            if int(self.new_quan.get()) > self.product_stock:
                buy_frame.after(100, lambda: self.change_payment())
                buy_frame.itemconfig(payment_txt, text=f"Payment: Stock out of range")
            elif int(self.new_quan.get()) == 0:
                buy_frame.after(100, lambda: self.change_payment())
                buy_frame.itemconfig(payment_txt, text=f"Payment: PHP 0")
            else:
                buy_frame.itemconfig(payment_txt, text=f"Payment: PHP {int(self.new_quan.get()) * self.product_price}")
                buy_frame.after(100, lambda: self.change_payment())

        except ValueError:
            buy_frame.after(100, lambda: self.change_payment())
            buy_frame.itemconfig(payment_txt, text=f"Payment: PHP 0")

    def transaction_method(self, new_quantity):
        global carts_id
        global cart_position
        global trans_code
        conn = sqlite3.connect("Products.db")
        conn2 = sqlite3.connect("Transaction.db")
        tran = conn2.cursor()
        c = conn.cursor()
        ask = messagebox.askyesno("info", "are you sure to buy this product?")
        if ask:

            code = ''
            quan = self.product_stock

            for i in range(10):
                code += str(trans_code[random.randint(0, 61)])

            change = f"UPDATE products SET product_stock={new_quantity} WHERE id={self.id_num}"
            c.execute(change)
            conn.commit()
            # self.product_quan_f.config(text=str(self.product_stock))

            print(self.product_stock)
            window.update()
            if self.product_stock <= 0:
                delete = f"DElETE FROM products WHERE id={self.id_num}"
                c.execute(delete)
                product_frame.delete(self.product_frame)
                conn.commit()

            # save to the cart
            price = int(self.get_price())
            payment = new_quantity * price
            print("payment", payment)

            product_p_c = Label(self.cart_f, image=self.product_image,
                                highlightcolor="black",
                                highlightthickness=2,
                                highlightbackground="black")
            product_p_c.image = self.product_image

            # cart_user_frame.create_text(250,100,text="hahaha")

            text_label = Canvas(self.cart_f, width=175, height=200, highlightcolor="black",
                                highlightbackground="black", highlightthickness=2)
            text_label.create_image(88, 100, image=img_bg_txt)
            text_label.create_text(80, 80, font=('Times', 10),
                                   text=f"Seller: {self.get_user_name()}\n\nType: {self.product_type}\n\nPayment: {payment}\n\nDate of deliver: {self.time_of_deliver}\n\nTrans Code: {code}")
            text_label.pack(side='right')
            frame_id = current_user().my_cart_frame.create_window(history_pos.X_POSITION,
                                                                  history_pos.Y_POSITION,
                                                                  window=self.cart_f,
                                                                  width=WINDOW_WIDTH - 40,
                                                                  height=170)
            history_id_list.append(frame_id)
            product_p_c.place(x=11, y=6)

            # create binding function for background
            self.cart_f.bind_all("<Configure>",
                                 lambda e: self.cart_f.configure(
                                     scrollregion=self.cart_f.bbox("all")))
            self.cart_f.bind("<MouseWheel>", current_user().hisroty_frame_wheel)
            text_label.bind_all("<Configure>",
                                lambda e: self.cart_f.configure(
                                    scrollregion=self.cart_f.bbox("all")))
            text_label.bind("<MouseWheel>", current_user().hisroty_frame_wheel)
            current_user().background.bind_all("<Configure>",
                                               lambda e: self.cart_f.configure(
                                                   scrollregion=self.cart_f.bbox("all")))
            current_user().background.bind("<MouseWheel>", current_user().hisroty_frame_wheel)
            product_p_c.bind_all("<Configure>",
                                 lambda e: self.cart_f.configure(
                                     scrollregion=self.cart_f.bbox("all")))
            product_p_c.bind("<MouseWheel>", current_user().hisroty_frame_wheel)

            current_user().my_cart_frame.bind_all("<Configure>",
                                                  lambda e: self.cart_f.configure(
                                                      scrollregion=self.cart_f.bbox("all")))
            current_user().my_cart_frame.bind("<MouseWheel>", current_user().hisroty_frame_wheel)
            # add cart to user window
            history_pos.SCROLL_Y_VAL_OF_PRDCTS += 160
            history_pos.Y_POSITION += 170
            update_scroll_Y(current_user().my_cart_frame, history_pos.SCROLL_Y_VAL_OF_PRDCTS)

            # =========================================================================================================================================

            # save the transaction
            transaction_container = Canvas(accounts_list[self.product_index].mytransaction_frame)
            product_p_c = Label(transaction_container, image=self.product_image,
                                highlightcolor="black",
                                highlightthickness=2,
                                highlightbackground="black")
            product_p_c.image = self.product_image

            text_label = Canvas(transaction_container, width=175, height=200, highlightcolor="black",
                                highlightbackground="black", highlightthickness=2)
            text_label.create_image(88, 100, image=img_bg_txt)
            text_label.create_text(80, 80, font=('Times', 10),
                                   text=f"Buyer: {current_user().get_user_name()}\n\nType: {self.product_type}\n\nPayment: {payment}\n\nDate of deliver: {self.time_of_deliver}\n\nTrans Code: {code}")
            text_label.pack(side='right')

            product_p_c.pack(side='left')
            frame_id = accounts_list[self.product_index].mytransaction_frame.create_window(trans_pos.X_POSITION,
                                                                                trans_pos.Y_POSITION,
                                                                                window=transaction_container,
                                                                                width=WINDOW_WIDTH - 40,
                                                                                height=170)
            history_id_list.append(frame_id)

            # create binding function for background
            transaction_container.bind_all("<Configure>",
                                           lambda e: transaction_container.configure(
                                               scrollregion=transaction_container.bbox("all")))
            transaction_container.bind("<MouseWheel>", accounts_list[self.product_index].trans_frame_wheel)
            text_label.bind_all("<Configure>",
                                lambda e: transaction_container.configure(
                                    scrollregion=transaction_container.bbox("all")))
            text_label.bind("<MouseWheel>", accounts_list[self.product_index].trans_frame_wheel)
            accounts_list[self.product_index].tran_background.bind_all("<Configure>",
                                                            lambda e: transaction_container.configure(
                                                                scrollregion=transaction_container.bbox("all")))
            accounts_list[self.product_index].tran_background.bind("<MouseWheel>", accounts_list[self.product_index].trans_frame_wheel)
            product_p_c.bind_all("<Configure>",
                                 lambda e: transaction_container.configure(
                                     scrollregion=transaction_container.bbox("all")))
            product_p_c.bind("<MouseWheel>", accounts_list[self.product_index].trans_frame_wheel)

            accounts_list[self.product_index].mytransaction_frame.bind_all("<Configure>",
                                                                lambda e: transaction_container.configure(
                                                                    scrollregion=transaction_container.bbox("all")))
            accounts_list[self.product_index].mytransaction_frame.bind("<MouseWheel>",
                                                            accounts_list[self.product_index].trans_frame_wheel)
            # add cart to user window
            trans_pos.SCROLL_Y_VAL_OF_PRDCTS += 180
            trans_pos.Y_POSITION += 190
            update_scroll_Y(accounts_list[self.product_index].mytransaction_frame, trans_pos.SCROLL_Y_VAL_OF_PRDCTS)
            print('gwrtygwhg')
            # ============================================================================================================
            show_trans_to_admin(self.product_image,self.get_user_name(), current_user().get_user_name(), self.product_type,payment,self.time_of_deliver,code)
            #========================================================================================================================================

            # send transaction to the admin
            insert_transaction_to_tb = [self.image_of_product, self.get_user_name(),
                                        current_user().get_user_name(), self.product_type, payment,
                                        self.time_of_deliver, code, int(self.product_index), int(user_index)]
            tran.executemany(
                "INSERT INTO transactions (product_img,seller_name,buyer_name,product_type,payment_amount,day_of_deliver,transaction_code,config_user_id,buyer_index) VALUES (?,?,?,?,?,?,?,?,?)",
                (insert_transaction_to_tb,))
            conn2.commit()
            transaction_list.append(
                str(f"Product:{self.product_type} | Seller:{self.get_user_name()} | Price:{self.product_price} >> Buyer:{current_user().get_user_name()} | Payment:{payment} | TRANSACTION CODE:{code}"))
        else:
            pass
        conn.commit()
        conn.close()
        conn2.commit()
        conn2.close()

    def unview_profile(self):
        return self.frame.pack_forget()

    def profile_view(self):
        unpack_all_frame_in_userframe()
        self.frame.pack(expand=True, fill=BOTH)

    def profile_unview(self):
        self.frame.pack_forget()
        # product_frame.pack(expand=True, fill=BOTH)
        buy_frame.place(x=10, y=10)

    # Getter methods to retrieve specific user details
    def payment_frame(self):
        pass

    def get_name(self):
        return self.product_type

    def get_pro_date(self):
        return f"{self.date_posted}| {self.time_posted}"

    def get_image(self):
        return self.product_image

    def get_price(self):
        return self.product_price

    def get_address(self):
        return self.address

    def get_contact(self):
        return self.seller_contact

    def get_quan(self):
        return self.product_stock


################################################################

def scoll_wheel_of_user_histo(event, frame):
    return frame.yview_scroll(-1 * (event.delta // 120), "units")


def check_position_of_searched_prodcuts():
    if search_pos.X_POSITION == search_pos.CHECK_POS_X:

        print("eatwyr")
        search_pos.X_POSITION = search_pos.GAP_VAL + 20
        search_pos.Y_POSITION += 190
        search_pos.SCROLL_Y_VAL_OF_PRDCTS += 190
        update_scroll_Y(search_frame_container, search_pos.SCROLL_Y_VAL_OF_PRDCTS)
    else:
        search_pos.X_POSITION += 190


def check_position_of_prodcuts():
    if product_pos.X_POSITION == product_pos.CHECK_POS_X:
        print("eatwyr")
        product_pos.X_POSITION = product_pos.GAP_VAL + 20
        product_pos.Y_POSITION += 190
        product_pos.SCROLL_Y_VAL_OF_PRDCTS += 190
        update_scroll_Y(product_frame, product_pos.SCROLL_Y_VAL_OF_PRDCTS)
        print("succesfully save")

    else:
        product_pos.X_POSITION += 190
        print("add")


def update_scroll_Y(frame, pos_y):
    print("succesfully done")
    return frame.config(scrollregion=(0, 0, pos_y, pos_y))


def refresh_scroll_Y():
    for searched in search_datas:
        search_frame_container.delete(searched)
        search_pos.X_POSITION = 110
        search_pos.Y_POSITION = search_pos.GAP_VAL + 20
        search_pos.SCROLL_Y_VAL_OF_PRDCTS = 200
        update_scroll_Y(search_frame_container, search_pos.SCROLL_Y_VAL_OF_PRDCTS)
    search_datas.clear()


def current_user():
    return accounts_list[user_index]


def show_user_content_window(user_window):
    return current_user().user_window.pack(fill=BOTH, expand=True)


def pack_window(windo):
    return windo.pack(fill=BOTH, expand=True)


def unpack_window(windo):
    return windo.pack_forget()


def save_product(product_imagee, product_name, product_price, product_quan, seller_contact):
    global product_frame
    global num
    global product_img
    global product_list
    if (
            product_validation(product_imagee, product_name, product_price, product_quan, seller_contact)):
        img = Image.open(product_img)
        img = img.resize((40, 40))
        img = ImageTk.PhotoImage(img)
        current_user().add_product(product_imagee,
                                   product_name,
                                   product_price,
                                   product_quan,
                                   seller_contact,
                                   )

        prd = Label(inven_frame, image=img,
                    text=f"Seller:{current_user().get_user_name()} Type:{product_name} Price:{product_price} Stock:{product_quan}",
                    compound="left")
        prd.image = img
        product_list.append(prd)
        num += 1
        types.delete(0, END)
        upload_price.delete(0, END)
        upload_stock.delete(0, END)
        upload_contact.delete(0, END)

    else:
        return messagebox.showerror('error', 'Please provide all required details to post your product for sale')


def product_validation(product_img, product_type, product_price, product_stock, seller_con):
    if product_img == None or product_type == "" or product_price == '' or product_stock == '' or seller_con == '' or check_number(
            seller_con) or check_price(product_price) or check_stock(product_stock):
        return False
    else:
        return True


def check_number(contact):
    if len(contact) == 11 and contact.startswith('09') and contact.isdigit():
        return True
    elif contact.isdigit():
        messagebox.showerror("Invalid", "Contact number should start with '09' and have 11 digits")
        return False
    else:
        messagebox.showerror("Invalid",
                             "Invalid contact number format. Please enter a valid 11-digit number starting with '09'")
        return False


def check_price(price):
    if price.isdigit():
        return True
    else:
        messagebox.showerror("Invalid", "Invalid Price")
        return False
def check_stock(stock):
    if stock.isdigit():
        return True
    else:
        messagebox.showerror("Invalid", "Invalid Stock")
        return False
def remove_in_user_product_list(indexx):
    print("remove index", indexx)

    current_user().user_product_list.remove(current_user().user_product_list[indexx])
    for item in current_user().user_product_list:
        if len(current_user().user_product_list) == 0:
            pass
        else:
            item.product_indx -= 1
    print("new len of list", len(current_user().user_product_list))
    window.update()

#######################  SAVE ACCOUNT
def save_account(id_pic, name, address, username, password):
    global sign_in_username
    global accounts_list
    # global age
    try:
        if sign_in_validation(id_pic, name, address, username, password):
            conn = sqlite3.connect('Accounts.db')
            c = conn.cursor()

            img = create_img(id_pic, 62, 80)
            account = Accounts(id_pic, name, address, username, password)
            show_acc_to_admin(img, name, address)
            accounts_list.append(account)
            with open(id_pic, 'rb') as image_file:
                id_picture = image_file.read()
                c.execute("INSERT INTO accounts (id_pic,name,address,username,password) VALUES (?,?,?,?,?)",
                          (sqlite3.Binary(id_picture), name, address, username, password))
            conn.commit()
            conn.close()
            sign_in_username.delete(0, END)
            sign_user_address.delete(0, END)
            sign_in_password.delete(0, END)
            confirm_pass.delete(0, END)
            show_log_in_frame()
        else:
            show_sign_in_frame()
    except Exception as e:
        messagebox.showerror("Error", f"Please fill in all the required fields to create an \naccount!")

def sign_in():
    global id_picture
    try:
        save_account(id_picture, sign_user_name.get(), sign_user_address.get(),
                     sign_in_username.get(), sign_in_password.get())
    except NameError as e:
        messagebox.showerror("Error", f"Please fill in all the required fields to create an \naccount!")


def sign_in_validation(id_pic, name, address, username, password):
    valid = []
    conn = sqlite3.connect("Accounts.db")
    c = conn.cursor()
    c.execute("SELECT username FROM accounts")
    for username in c.fetchall():
        valid.append(username)
        print(username)
    conn.commit()
    conn.close()
    if not (
            id_pic == None or name == '' or address == '' or username == ''):

        if username not in valid:
            if password == confirm_pass.get():
                return True
        else:
            messagebox.showerror("Invalid", 'Error: Username already exists. Please choose a different username')
            return False
    else:
        messagebox.showerror("Invalid", 'Please fill in all the required fields to create an \naccount!')
        return False


def hover_menu(key):
    if key == 0:
        menu_box.itemconfig(log_out, image=log_out_img2)
        menu_box.itemconfig(txt1, fill='red')
    elif key == 1:
        menu_box.itemconfig(show_transaction_btn, image=trans_image2)
        menu_box.itemconfig(txt2, fill='red')
    elif key == 2:
        menu_box.itemconfig(show_products_btn, image=mypd_img2)
        menu_box.itemconfig(txt3, fill='red')
    elif key == 3:
        menu_box.itemconfig(cart_button_c, image=cart_logo2)
        menu_box.itemconfig(txt4, fill='red')
def unhover_menu(key):
    if key == 0:
        menu_box.itemconfig(log_out, image=log_out_img)
        menu_box.itemconfig(txt1, fill='black')
    elif key == 1:
        menu_box.itemconfig(show_transaction_btn, image=trans_image)
        menu_box.itemconfig(txt2, fill='black')
    elif key == 2:
        menu_box.itemconfig(show_products_btn, image=mypd_img)
        menu_box.itemconfig(txt3, fill='black')
    elif key == 3:
        menu_box.itemconfig(cart_button_c, image=cart_logo)
        menu_box.itemconfig(txt4, fill='black')
#######################  ADMIN
# ==============================================================================================================================
def show_acc_to_admin(id_pic, name, address):
    """
    Display information about a user in a graphical user interface.
    """
    acc_frame_con = Canvas(users_table, bg='black')
    id_img = Label(acc_frame_con, image=id_pic, width=60, height=80, highlightcolor='black', highlightthickness=1,
                   highlightbackground='black', relief='flat')
    id_img.image = id_pic
    id_img.pack(side='left')
    name_con = Label(acc_frame_con, text=name, width=25, height=80, highlightcolor='black', highlightthickness=1,
                     highlightbackground='black', relief='flat')
    name_con.pack(side='left')
    address_con = Label(acc_frame_con, text=address, width=20, height=80, highlightcolor='black', highlightthickness=1,
                        highlightbackground='black', relief='flat')
    address_con.pack(side='left')

    users_table.create_window(admin_accs_pos.X_POSITION, admin_accs_pos.Y_POSITION, window=acc_frame_con, width=400,
                              height=80)

    acc_frame_con.bind_all("<Configure>",
                           lambda e: acc_frame_con.configure(
                               scrollregion=acc_frame_con.bbox("all")))
    acc_frame_con.bind("<MouseWheel>", accounts_frame_wheel)
    address_con.bind_all("<Configure>",
                         lambda e: acc_frame_con.configure(
                             scrollregion=acc_frame_con.bbox("all")))
    address_con.bind("<MouseWheel>", accounts_frame_wheel)
    name_con.bind_all("<Configure>",
                      lambda e: acc_frame_con.configure(
                          scrollregion=acc_frame_con.bbox("all")))
    name_con.bind("<MouseWheel>", accounts_frame_wheel)
    id_img.bind_all("<Configure>",
                    lambda e: acc_frame_con.configure(
                        scrollregion=acc_frame_con.bbox("all")))
    id_img.bind("<MouseWheel>", accounts_frame_wheel)

    users_bg.bind_all("<Configure>", lambda e: acc_frame_con.configure(
        scrollregion=acc_frame_con.bbox("all")))
    users_bg.bind("<MouseWheel>", accounts_frame_wheel)
    admin_accs_pos.SCROLL_Y_VAL_OF_PRDCTS += 100
    admin_accs_pos.Y_POSITION += 80

    update_scroll_Y(users_table, admin_accs_pos.SCROLL_Y_VAL_OF_PRDCTS)

def accounts_frame_wheel(event):
    users_table.yview_scroll(-1 * (event.delta // 120), "units")


# ================================================================================================================================
def show_inven_to_admin(product_img, product_type, product_price, product_stock):
    """
    Display information about a user in a graphical user interface.
    """
    print("jlqevfu2rogfuo3tgyivcit4q3guwo5gto")
    inven_frame_con = Canvas(inven_table, highlightcolor='black', highlightthickness=1, highlightbackground='black',
                             relief='flat')
    prd_img = Label(inven_frame_con, image=product_img, width=75, highlightcolor='black', highlightthickness=1,
                    highlightbackground='black', relief='flat')
    prd_img.image = product_img
    prd_img.pack(side='left')
    prd_typ = Label(inven_frame_con, text=product_type, width=18, highlightcolor='black', highlightthickness=1,
                    highlightbackground='black', relief='flat')
    prd_typ.pack(side='left', fill=Y)
    prd_prc = Label(inven_frame_con, text=product_price, width=12, highlightcolor='black', highlightthickness=1,
                    highlightbackground='black', relief='flat')
    prd_prc.pack(side='left', fill=Y)
    prd_stk = Label(inven_frame_con, text=product_stock, width=12, highlightcolor='black', highlightthickness=1,
                    highlightbackground='black', relief='flat')
    prd_stk.pack(side='left', fill=Y)

    inven_table.create_window(admin_inven_pos.X_POSITION, admin_inven_pos.Y_POSITION, window=inven_frame_con, width=400,
                              height=80)
    prd_img.bind_all("<Configure>",
                     lambda e: inven_frame_con.configure(
                         scrollregion=inven_frame_con.bbox("all")))
    prd_img.bind("<MouseWheel>", inven_frame_wheel)
    prd_stk.bind_all("<Configure>",
                     lambda e: inven_frame_con.configure(
                         scrollregion=inven_frame_con.bbox("all")))
    prd_stk.bind("<MouseWheel>", inven_frame_wheel)
    prd_prc.bind_all("<Configure>",
                     lambda e: inven_frame_con.configure(
                         scrollregion=inven_frame_con.bbox("all")))
    prd_prc.bind("<MouseWheel>", inven_frame_wheel)
    prd_typ.bind_all("<Configure>",
                     lambda e: inven_frame_con.configure(
                         scrollregion=inven_frame_con.bbox("all")))
    prd_typ.bind("<MouseWheel>", inven_frame_wheel)

    inven_frame_con.bind_all("<Configure>",
                             lambda e: inven_frame_con.configure(
                                 scrollregion=inven_frame_con.bbox("all")))
    inven_frame_bg.bind("<MouseWheel>", inven_frame_wheel)

    inven_frame_bg.bind_all("<Configure>", lambda e: inven_frame_con.configure(
        scrollregion=inven_frame_con.bbox("all")))
    inven_frame.bind("<MouseWheel>", inven_frame_wheel)
    admin_inven_pos.SCROLL_Y_VAL_OF_PRDCTS += 80
    admin_inven_pos.Y_POSITION += 80

    update_scroll_Y(inven_table, admin_inven_pos.SCROLL_Y_VAL_OF_PRDCTS)

def inven_frame_wheel(event):
    inven_table.yview_scroll(-1 * (event.delta // 120), "units")

# ================================================================================================================================
def show_trans_to_admin(product_img, seller, buyer, type, payment, dod, code):
    """
    Display information about a user in a graphical user interface.
    """

    trans_frame_con = Canvas(tran_table, bg='red', highlightcolor='black', highlightthickness=1,
                             highlightbackground='black', relief='flat')
    product_img_L = Label(trans_frame_con, image=product_img, width=110, highlightcolor='black', highlightthickness=1,
                          highlightbackground='black', relief='flat')
    product_img_L.pack(side='left', fill=Y)
    product_img_L.image = product_img
    product_text = Canvas(trans_frame_con, width=263,
                          highlightcolor='black', highlightthickness=1,
                          highlightbackground='black', relief='flat')
    product_text.create_image(130, 62, image=con_txt_img)
    product_text.create_text(130, 20, text=f"Seller: {seller}")
    product_text.create_text(130, 35, text=f"Buyer: {buyer}")
    product_text.create_text(130, 50, text=f"Type: {type}")
    product_text.create_text(130, 65, text=f"Payment: {payment}")
    product_text.create_text(130, 80, text=f"Date: {dod}")
    product_text.create_text(130, 95, text=f"Code: {code}")

    product_text.pack(side='left', fill=Y)
    tran_table.create_window(admin_trans_pos.X_POSITION, admin_trans_pos.Y_POSITION, window=trans_frame_con, width=380,
                             height=120)

    product_text.bind_all("<Configure>",
                          lambda e: trans_frame_con.configure(
                              scrollregion=trans_frame_con.bbox("all")))
    product_text.bind("<MouseWheel>", trans_frame_wheel)
    product_img_L.bind_all("<Configure>",
                           lambda e: trans_frame_con.configure(
                               scrollregion=trans_frame_con.bbox("all")))
    product_img_L.bind("<MouseWheel>", trans_frame_wheel)
    trans_frame_con.bind_all("<Configure>",
                             lambda e: trans_frame_con.configure(
                                 scrollregion=trans_frame_con.bbox("all")))
    trans_frame_con.bind("<MouseWheel>", trans_frame_wheel)

    tran_frame_bg.bind_all("<Configure>", lambda e: trans_frame_con.configure(
        scrollregion=trans_frame_con.bbox("all")))
    tran_frame_bg.bind("<MouseWheel>", trans_frame_wheel)

    admin_trans_pos.SCROLL_Y_VAL_OF_PRDCTS += 125
    admin_trans_pos.Y_POSITION += 125

    update_scroll_Y(tran_table, admin_trans_pos.SCROLL_Y_VAL_OF_PRDCTS)

def trans_frame_wheel(event):
    tran_table.yview_scroll(-1 * (event.delta // 120), "units")

# ================================================================================================================================
def admin():
    size_check()
    global product_list

    unpack_window(log_in_canvas)
    pack_window(admin_frame)

def unpack_admin_windows():
    admin_menu_frame.pack_forget()
    inven_frame.pack_forget()
    admin_tran_frame.pack_forget()
    users_frame.pack_forget()
    navigataion_frame.pack_forget()
def users(event):
    unpack_admin_windows()
    pack_window(users_frame)
    log_out_admin.config(command=back_to_admin_home, text='Back')
def inventory(event):
    unpack_admin_windows()
    pack_window(inven_frame)
    log_out_admin.config(command=back_to_admin_home, text='Back')
def admin_log_out():
    unpack_window(admin_frame)
    welcome()
def back_to_admin_home():
    unpack_admin_windows()
    pack_window(admin_frame)
    pack_window(navigataion_frame)
    log_out_admin.config(command=admin_log_out, text="Log out")

def admin_menu(event):
    unpack_admin_windows()
    pack_window(admin_menu_frame)
    log_out_admin.config(command=back_to_admin_home, text='Back')

def admin_tran(event):
    unpack_admin_windows()
    pack_window(admin_tran_frame)
    log_out_admin.config(command=back_to_admin_home, text='Back')

#######################   USERS
def hover_bar(key):
    if key == 0:
        bottom_can_bar.itemconfig(menu_button_c, image=menu_logo2)
    elif key == 1:
        bottom_can_bar.itemconfig(prof_button_c, image=user_logo2)
    elif key == 2:
        bottom_can_bar.itemconfig(add_button_c, image=add_logo2)
    elif key == 3:
        bottom_can_bar.itemconfig(search_button_c, image=search_logo2)
    elif key == 4:
        bottom_can_bar.itemconfig(home_button_c, image=home_logo2)


def unhover_bar(key):
    if key == 0:
        bottom_can_bar.itemconfig(menu_button_c, image=menu_logo)
    elif key == 1:
        bottom_can_bar.itemconfig(prof_button_c, image=user_logo)
    elif key == 2:
        bottom_can_bar.itemconfig(add_button_c, image=add_logo)
    elif key == 3:
        bottom_can_bar.itemconfig(search_button_c, image=search_logo)
    elif key == 4:
        bottom_can_bar.itemconfig(home_button_c, image=home_logo)


def user():
    size_check()
    window.update()


def home():
    global product_main_frame
    global cart_position
    global carts_id
    global search_frame_pos
    global search_frame
    size_check()
    unpack_window(log_in_canvas)
    unpack_all_frame_in_userframe()
    pack_window(user_frame)

    current_user().mytransaction_frame.pack(fill=X, side='bottom')  # show user transaction
    current_user().my_cart_frame.pack(fill=BOTH, expand=True, side='bottom')  # show user transaction
    current_user().my_products_frame.pack(fill=BOTH, expand=True, side='bottom')  # show user transaction

    pack_window(product_main_frame)

    for types in search_types_id:
        search_frame.delete(str(types))
    search_frame_pos = 200


def unpack_all_frame_in_userframe():
    sell_frame.pack_forget()
    cart_main_frame.pack_forget()
    profile_frame.pack_forget()
    menu_frame.pack_forget()
    buy_frame.pack_forget()

    user_products_frame.pack_forget()
    user_transaction_frame.pack_forget()
    search_frame.pack_forget()
    product_main_frame.pack_forget()
    for acc in accounts_list:
        acc.unpack_view_Prof()


def show_products(event):
    global search_frame_pos
    global products
    size_check()
    unpack_all_frame_in_userframe()
    pack_window(product_main_frame)
    for types in search_types_id:
        search_frame.delete(str(types))
    search_frame_pos = 200


def mysearch(event):
    global search_frame_pos
    size_check()
    unpack_all_frame_in_userframe()

    pack_window(search_frame)

    for types in search_types_id:
        search_frame.delete(str(types))
    search_frame_pos = 200


def myproducts(event):
    global search_frame_pos

    size_check()
    unpack_all_frame_in_userframe()
    current_user().my_products_frame.pack(fill=BOTH, expand=True, side='bottom')  # show user transaction
    pack_window(user_products_frame)

    for types in search_types_id:
        search_frame.delete(str(types))
    search_frame_pos = 200


def mytransaction(event):
    global search_frame_pos
    size_check()
    unpack_all_frame_in_userframe()

    for item in current_user().user_product_list:
        item.show_my_transaction()

    pack_window(user_transaction_frame)
    for types in search_types_id:
        search_frame.delete(str(types))
    search_frame_pos = 200


def back_to_log_com():
    global search_frame_pos
    size_check()
    unpack_window(sign_in_canvas)
    pack_window(log_in_canvas)

    for types in search_types_id:
        search_frame.delete(str(types))
    search_frame_pos = 200


def add_product(event):
    global search_frame_pos
    size_check()
    unpack_all_frame_in_userframe()
    pack_window(sell_frame)

    for types in search_types_id:
        search_frame.delete(str(types))
    search_frame_pos = 200


def menu(event):
    global search_frame_pos
    size_check()
    unpack_all_frame_in_userframe()

    pack_window(menu_frame)
    show_menu_transition()

    for types in search_types_id:
        search_frame.delete(str(types))
    search_frame_pos = 200


def show_menu_transition(wid=0):
    if wid == 100:
        pass
    else:
        menu_box.config(width=wid)
        menu_frame.after(5, lambda: show_menu_transition(wid))
        wid += 1


def cart(event):
    global search_frame_pos
    global cart_position
    size_check()
    unpack_all_frame_in_userframe()
    current_user().my_cart_frame.pack(fill=BOTH, expand=True, side='bottom')  # show user transaction
    pack_window(cart_main_frame)

    for types in search_types_id:
        search_frame.delete(str(types))
    search_frame_pos = 200


def profile(event):
    global search_frame_pos
    global user_index
    global accounts_list
    size_check()
    unpack_all_frame_in_userframe()

    pack_window(profile_frame)
    profile_pic.config(image=current_user().get_id())
    profile_frame.itemconfig(user_information, text=f"{current_user().get_user_name()}")
    profile_frame.itemconfig(user_address,
                             text=f"{current_user().get_user_address()}")

    for types in search_types_id:
        search_frame.delete(str(types))
    search_frame_pos = 200

# scroll the products
    """
    Scroll the cart frame vertically in response to a mouse wheel event.
    @param event - the mouse wheel event
    @return None
    """
def on_mousewheel_carts_F(event):
    cart_frame.yview_scroll(-1 * (event.delta // 120), "units")

def change_bg_color():
    """
    Change the background color of the log_in_canvas to a light color and update the image of the switch to moon_img when the switch is clicked.
    @return None
    """
    log_in_canvas.itemconfig(switch, image=moon_img)
    log_in_canvas.config(bg='#414a4c')

    log_in_canvas.tag_bind(switch, "<Button>", lambda event: change_to_light())

def change_to_light():
    """
    Change the appearance of the canvas to a light theme by updating the image of a switch, the background color, and binding a button event to a function that changes the background color.
    @return None
    """
    log_in_canvas.itemconfig(switch, image=sun_img)
    log_in_canvas.config(bg=bgcolor)
    log_in_canvas.tag_bind(switch, "<Button>", lambda event: change_bg_color())

def user_log_out(event):
    """
    Log out the user from the system.
    @param event - the event that triggers the log out
    @return None
    """
    global carts_id
    global cart_frame
    global cart_position
    unpack_all_frame_in_userframe()
    unpack_window(user_frame)
    cart_position = 200
    for ids in carts_id:
        cart_main_frame.delete(str(ids))
    for acc in accounts_list:
        acc.my_cart_frame.pack_forget()
        acc.my_products_frame.pack_forget()
    welcome()


def about():
    pass

################################################################
# center the window
def center_window(window, width, height, ):
    """
    Center a window on the screen by calculating the appropriate x and y coordinates based on the screen width and height, as well as the desired width and height of the window.
    @param window - the window to center
    @param width - the desired width of the window
    @param height - the desired height of the window
    """
    screen_width = window.winfo_screenwidth()
    screen_heigth = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_heigth - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

################################################################
def restore_db_to_list():
    """
    Restore the database to a list of accounts and products.
    """
    global accounts_list
    global num
    global prd_key
    global product_list

    products_list = []

    conn = sqlite3.connect("Accounts.db")
    conn2 = sqlite3.connect("Products.db")
    conn3 = sqlite3.connect("Transaction.db")

    c = conn.cursor()

    c2 = conn2.cursor()
    c3 = conn3.cursor()
    # c2.execute("CREATE TABLE IF NOT EXISTS products (product_img BLOB,product_type text,product_price INTEGER,product_stock INTEGER,product_index INTEGER)")
    c.execute("SELECT * FROM accounts")
    c2.execute("SELECT * FROM products")

    index = 0
    # RESTORE ACCOUNTS FROM THE DATABASE ACCOUNTS TO LIST OF ACCOUNTS
    for acc in c.fetchall():
        """
        Retrieve account information from a database and create Account objects for each entry. 
        c - the cursor object for executing SQL queries
        accounts_list - a list of Account objects
        """

        img = create_img(io.BytesIO(acc[1]), 180, 260)
        img2 = create_img(io.BytesIO(acc[1]), 62, 80)

        account = Accounts(img, acc[2], acc[3], acc[4], acc[5])
        accounts_list.append(account)
        print("name user:", accounts_list[index].get_user_name())
        show_acc_to_admin(img2, acc[2], acc[3])
        index += 1
    print("account len is ", len(accounts_list))

    products_restore = c2.fetchall()
    # RESTORE PRODUCTS FROM DATABASE PRODUCTS TO ITS OWNERS
    for acc_index in range(len(accounts_list)):
        """
        Iterate over the accounts list and for each account, iterate over the products restore list. If the account index matches the index in the product, create a new product object and add it to the product list. Also, update the user's product list and increment the product index. Finally, commit the changes to the database.
        accounts_list - the list of accounts
        products_restore - the list of products to restore
        """
        print("len(", acc_index, ")")
        for prod in products_restore:
            print("prod[6]", int(prod[6]), "=", acc_index)
            if prod[6] == acc_index:
                print("prod[6]", int(prod[6]))
                img = create_img(io.BytesIO(prod[1]), 100, 100)
                img2 = create_img(io.BytesIO(prod[1]), 75, 75)
                product = Products(prod[1], prod[2], prod[3], prod[4], prod[5], acc_index, prod[0],
                                   accounts_list[acc_index].product_indx)
                product.show_profile_frame(accounts_list[acc_index].id_pic, accounts_list[acc_index].get_user_name(),
                                           accounts_list[acc_index].get_user_address())
                # prd = Label(inven_frame, image=img,
                #           text=f"Seller:{accounts_list[acc_index].get_user_name()} Type:{prod[2]} Price:{prod[3]} Stock:{prod[4]}",
                #          compound="left")
                # prd.image = img

                # product_list.append(prd)
                # print(prod[0])

                accounts_list[acc_index].user_product_list.append(product)
                #
                accounts_list[acc_index].product_indx += 1
                print("prd number before", prd_key)
                if prod[0] > prd_key:
                    prd_key = prod[0]
                    print("prd number after", prd_key)
                # ---------------------------------------------------------------------------------------------------------
                user_product_frame = Canvas(accounts_list[acc_index].my_products_frame, bg="white",
                                            highlightcolor="black",
                                            highlightbackground="black", highlightthickness=2, width=WINDOW_WIDTH - 40)

                myproduct_img = Label(user_product_frame, image=img,
                                      highlightcolor="black",
                                      highlightthickness=2,
                                      highlightbackground="black")
                myproduct_img.image = img

                # cart_user_frame.create_text(250,100,text="hahaha")

                text_label_MyP = Canvas(user_product_frame, width=175, height=200, highlightcolor="black",
                                        highlightbackground="black", highlightthickness=2)
                text_label_MyP.create_image(88, 100, image=img_bg_txt)
                text_label_MyP.create_text(80, 50, font=('Times', 10),
                                           text=f"Type:{prod[2]}\nPrice:{prod[3]}\nStock:{prod[4]}")
                text_label_MyP.pack(side='right')
                frame_id = accounts_list[acc_index].my_products_frame.create_window(
                    accounts_list[acc_index].my_prod_pos.X_POSITION,
                    accounts_list[acc_index].my_prod_pos.Y_POSITION,
                    width=WINDOW_WIDTH - 40,
                    window=user_product_frame,
                    height=100)
                history_id_list.append(frame_id)
                myproduct_img.pack(side='left')

                # create binding function for background
                user_product_frame.bind_all("<Configure>",
                                            lambda e: user_product_frame.configure(
                                                scrollregion=user_product_frame.bbox("all")))
                user_product_frame.bind("<MouseWheel>", accounts_list[acc_index].myP_frame_wheel)
                text_label_MyP.bind_all("<Configure>",
                                        lambda e: user_product_frame.configure(
                                            scrollregion=user_product_frame.bbox("all")))
                text_label_MyP.bind("<MouseWheel>", accounts_list[acc_index].myP_frame_wheel)
                accounts_list[acc_index].myP_background.bind_all("<Configure>",
                                                                 lambda e: user_product_frame.configure(
                                                                     scrollregion=user_product_frame.bbox("all")))
                accounts_list[acc_index].myP_background.bind("<MouseWheel>", accounts_list[acc_index].myP_frame_wheel)
                myproduct_img.bind_all("<Configure>",
                                       lambda e: user_product_frame.configure(
                                           scrollregion=user_product_frame.bbox("all")))
                myproduct_img.bind("<MouseWheel>", accounts_list[acc_index].myP_frame_wheel)

                accounts_list[acc_index].my_products_frame.bind_all("<Configure>",
                                                                    lambda e: user_product_frame.configure(
                                                                        scrollregion=user_product_frame.bbox("all")))
                accounts_list[acc_index].my_products_frame.bind("<MouseWheel>",
                                                                accounts_list[acc_index].myP_frame_wheel)
                # add cart to user window
                accounts_list[acc_index].my_prod_pos.SCROLL_Y_VAL_OF_PRDCTS += 120
                accounts_list[acc_index].my_prod_pos.Y_POSITION += 120
                update_scroll_Y(accounts_list[acc_index].my_products_frame,
                                accounts_list[acc_index].my_prod_pos.SCROLL_Y_VAL_OF_PRDCTS)
                # ==========================================================================================================================
                show_inven_to_admin(img2, prod[2], prod[3], prod[4])
                # ==========================================================================================================================

            conn.commit()
    prd_key += 1
    print("prd last ", prd_key)

    # RESTORE TRANSACTION LIST
    for user_id in range(len(accounts_list)):
        """
        Iterate over the range of the length of the accounts_list.
        accounts_list - the list of user accounts
        """
        c3.execute("SELECT * FROM transactions")
        for _tran in c3.fetchall():
            """
            Iterate over the results fetched from the database query and assign each result to the variable `_tran`.
            """
            if str(DATE) < str(_tran[6]):
                delete = f"DELETE FROM transactions WHERE id={_tran[0]}"
                c3.execute(delete)
            if _tran[8] == user_id:
                """
                If the 8th element of the `_tran` list is equal to `user_id`, perform the following actions:
                - Print the value of `_tran[8]`, followed by `'tran'` and `user_index`.
                - Create a `LabelFrame` called `transaction_container` within the `mytransaction_frame` of the `accounts_list` at the index `user_id`.
                - Open the image stored in `_tran[1]` as `tran_img`, resize it to 40x40 pixels, and convert it to a `PhotoImage` object.
                - Create a `Label` called `product_p_t` within `transaction_container` and set its image to `tran_img`.
                - Create a `Label` called `product
                """
                print(_tran[8], 'tran', user_index)
                transaction_container = Canvas(accounts_list[user_id].mytransaction_frame)
                tran_img = Image.open(io.BytesIO(_tran[1]))
                tran_img = tran_img.resize((150, 150))
                tran_img = ImageTk.PhotoImage(tran_img)
                tran_img2 = create_img(io.BytesIO(_tran[1]), 110, 110)
                product_p_c = Label(transaction_container, image=tran_img,
                                    highlightcolor="black",
                                    highlightthickness=2,
                                    highlightbackground="black")
                product_p_c.image = tran_img

                text_label = Canvas(transaction_container, width=175, height=200, highlightcolor="black",
                                    highlightbackground="black", highlightthickness=2)
                text_label.create_image(88, 100, image=img_bg_txt)
                text_label.create_text(80, 80, font=('Times', 10),
                                       text=f"Buyer: {_tran[3]}\n\nType: {_tran[4]}\n\nPayment: {_tran[5]}\n\nDate of deliver: {_tran[6]}\n\nTrans Code: {_tran[7]}")
                text_label.pack(side='right')

                product_p_c.pack(side='left')
                frame_id = accounts_list[user_id].mytransaction_frame.create_window(trans_pos.X_POSITION,
                                                                                    trans_pos.Y_POSITION,
                                                                                    window=transaction_container,
                                                                                    width=WINDOW_WIDTH - 40,
                                                                                    height=170)
                history_id_list.append(frame_id)

                # create binding function for background
                transaction_container.bind_all("<Configure>",
                                               lambda e: transaction_container.configure(
                                                   scrollregion=transaction_container.bbox("all")))
                transaction_container.bind("<MouseWheel>", accounts_list[user_id].trans_frame_wheel)
                text_label.bind_all("<Configure>",
                                    lambda e: transaction_container.configure(
                                        scrollregion=transaction_container.bbox("all")))
                text_label.bind("<MouseWheel>", accounts_list[user_id].trans_frame_wheel)
                accounts_list[user_id].tran_background.bind_all("<Configure>",
                                                                lambda e: transaction_container.configure(
                                                                    scrollregion=transaction_container.bbox("all")))
                accounts_list[user_id].tran_background.bind("<MouseWheel>", accounts_list[user_id].trans_frame_wheel)
                product_p_c.bind_all("<Configure>",
                                     lambda e: transaction_container.configure(
                                         scrollregion=transaction_container.bbox("all")))
                product_p_c.bind("<MouseWheel>", accounts_list[user_id].hisroty_frame_wheel)

                accounts_list[user_id].mytransaction_frame.bind_all("<Configure>",
                                                                    lambda e: transaction_container.configure(
                                                                        scrollregion=transaction_container.bbox("all")))
                accounts_list[user_id].mytransaction_frame.bind("<MouseWheel>",
                                                                accounts_list[user_id].trans_frame_wheel)
                # add cart to user window
                trans_pos.SCROLL_Y_VAL_OF_PRDCTS += 180
                trans_pos.Y_POSITION += 190
                update_scroll_Y(accounts_list[user_id].mytransaction_frame, trans_pos.SCROLL_Y_VAL_OF_PRDCTS)
                print('gwrtygwhg')
                # ============================================================================================================
                show_trans_to_admin(tran_img2, _tran[2], _tran[3], _tran[4], _tran[5], _tran[6], _tran[7])

    conn2.close()
    conn3.close()
    conn.close()
def restore_carts():
    """
    Restore the user's shopping carts from a SQLite database.
    @return None
    """
    conn = sqlite3.connect("Transaction.db")
    c3 = conn.cursor()
    # RESTORE USER CART FROM DB
    for user_id in range(len(accounts_list)):
      
        c3.execute("SELECT * FROM transactions")
        for _tran in c3.fetchall():
            
            if _tran[9] == user_id:
               
                print("9:", _tran[9], "user_id = ", user_id)

                cart_img = create_img(io.BytesIO(_tran[1]), 150, 150)

                cart_user_frame = Canvas(accounts_list[user_id].my_cart_frame, bg="white", highlightcolor="black",
                                         highlightbackground="black", highlightthickness=2)

                product_p_c = Label(cart_user_frame, image=cart_img,
                                    highlightcolor="black",
                                    highlightthickness=2,
                                    highlightbackground="black")
                product_p_c.image = cart_img

                # cart_user_frame.create_text(250,100,text="hahaha")

                text_label = Canvas(cart_user_frame, width=175, height=200, highlightcolor="black",
                                    highlightbackground="black", highlightthickness=2)
                text_label.create_image(88, 100, image=img_bg_txt)
                text_label.create_text(80, 80, font=('Times', 10),
                                       text=f"Seller: {_tran[2]}\n\nType: {_tran[4]}\n\nPayment: {_tran[5]}\n\nDate of deliver: {_tran[6]}\n\nTrans Code: {_tran[7]}")
                text_label.pack(side='right')
                frame_id = accounts_list[user_id].my_cart_frame.create_window(history_pos.X_POSITION,
                                                                              history_pos.Y_POSITION,
                                                                              window=cart_user_frame,
                                                                              width=WINDOW_WIDTH - 40,
                                                                              height=170)
                history_id_list.append(frame_id)
                product_p_c.place(x=11, y=6)

                # create binding function for background
                cart_user_frame.bind_all("<Configure>",
                                         lambda e: cart_user_frame.configure(
                                             scrollregion=cart_user_frame.bbox("all")))
                cart_user_frame.bind("<MouseWheel>", current_user().hisroty_frame_wheel)
                text_label.bind_all("<Configure>",
                                    lambda e: cart_user_frame.configure(
                                        scrollregion=cart_user_frame.bbox("all")))
                text_label.bind("<MouseWheel>", current_user().hisroty_frame_wheel)
                accounts_list[user_id].background.bind_all("<Configure>",
                                                           lambda e: cart_user_frame.configure(
                                                               scrollregion=cart_user_frame.bbox("all")))
                accounts_list[user_id].background.bind("<MouseWheel>", current_user().hisroty_frame_wheel)
                product_p_c.bind_all("<Configure>",
                                     lambda e: cart_user_frame.configure(
                                         scrollregion=cart_user_frame.bbox("all")))
                product_p_c.bind("<MouseWheel>", current_user().hisroty_frame_wheel)

                accounts_list[user_id].my_cart_frame.bind_all("<Configure>",
                                                              lambda e: cart_user_frame.configure(
                                                                  scrollregion=cart_user_frame.bbox("all")))
                accounts_list[user_id].my_cart_frame.bind("<MouseWheel>", accounts_list[user_id].hisroty_frame_wheel)
                # add cart to user window
                history_pos.SCROLL_Y_VAL_OF_PRDCTS += 180
                history_pos.Y_POSITION += 190
                update_scroll_Y(accounts_list[user_id].my_cart_frame, history_pos.SCROLL_Y_VAL_OF_PRDCTS)
                print("name", _tran[9])
    conn.commit()
    conn.close()
def welcome():
    """
    This function is responsible for initializing the application by calling two other functions: `size_check()` and `pack_window(home_canvas)`.
    """

    size_check()
    pack_window(home_canvas)

###############################################################
################################################################
def log_in_validation():
    """
    Validate the login credentials entered by the user.
    @return None
    """
    isExist = False
    global user_index
    conn = sqlite3.connect('Accounts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM accounts")
    if log_in_username.get() == "" and log_in_password.get() == "":
        messagebox.showerror("Error", "Please enter your username and password")

    elif log_in_username.get() == "":
        messagebox.showerror("Error", "Please enter a Username")

    elif log_in_password.get() == "":
        messagebox.showerror("Error", "Please enter a Password")

    elif log_in_username.get() == "admin" and log_in_password.get() == 'admin':
        log_in_password.delete(0, END)
        log_in_username.delete(0, END)
        admin()

    else:
        for acc in c.fetchall():
            if log_in_username.get() == acc[4] and log_in_password.get() == acc[5]:
                user_index = acc[0] - 1
                log_in_password.delete(0, END)
                log_in_username.delete(0, END)
                isExist = True
                home()
                break
        if isExist:
            pass
        else:
            messagebox.showerror("Invalid",
                                 "The provided username amd password does not exist. \nPlease check your username or \nsign up for a new account")
            show_log_in_frame()
    conn.commit()
    conn.close()

###############################################################
def write_text(index):
    """
    Write a text on a canvas gradually by updating the text with each iteration.
    index - the current index of the text to be written
    """
    if index <= len(tagline):
        partial_text = tagline[:index]
        home_canvas.itemconfig(bsu_tagline, text=partial_text)

        home_canvas.after(40, write_text, index + 1)


def enter_txt_U():
    """
    This function is used to enter text in a user interface. It updates the appearance of the username line in the UI, updates the window, and prints a message.
    @return None
    """
    log_in_canvas.itemconfig(usr_name_line, fill="black", width=1)
    window.update()

    log_in_canvas.itemconfig(usr_p_line, fill="#F3F2ED", width=1)
    window.update()

    print('wrht')


def enter_txt_P():
    """
    This function is used to update the appearance of a login form in a graphical user interface. It changes the color and width of the username line and password line in the form.
    @return None
    """
    log_in_canvas.itemconfig(usr_name_line, fill="#F3F2ED", width=1)
    window.update()

    log_in_canvas.itemconfig(usr_p_line, fill="black", width=1)
    window.update()


################################################################
def show_password():
    """
    This function is used to show the password in a login form. It performs the following actions:
    1. Prints "aeg" to the console.
    2. Sets the show attribute of the log_in_password widget to an empty string, making the password visible.
    3. Changes the image of the pass_btn_config widget to hide_pass_img.
    4. Unbinds the "<Button>" event from the pass_btn_config widget.
    5. Binds the "<Button>" event to the hide_password() function.
    6. Updates the window to reflect the changes.
    """
    print("aeg")
    log_in_password.config(show='')
    log_in_password.show = ""
    log_in_canvas.itemconfig(pass_btn_config, image=hide_pass_img)
    log_in_canvas.tag_unbind(pass_btn_config, "<Button>")
    log_in_canvas.tag_bind(pass_btn_config, "<Button>", lambda event: hide_password())
    window.update()
################################################################
def hide_password():
    """
    Hide the password by configuring the log_in_password widget to show asterisks instead of the actual characters. Also, update the image of the pass_btn_config widget to show a "show password" icon. Bind the button to the show_password() function when clicked.
    @return None
    """
    log_in_password.config(show='*')
    log_in_password.show = "*"
    log_in_canvas.itemconfig(pass_btn_config, image=show_pass_img)
    log_in_canvas.tag_unbind(pass_btn_config, "<Button>")
    log_in_canvas.tag_bind(pass_btn_config, "<Button>", lambda event: show_password())
    window.update()

################################################################
def show_log_in_frame():
    """
    This function is responsible for displaying the log in frame in a graphical user interface (GUI) application.
    It unpacks the sign in canvas and home canvas, and then packs the log in canvas.
    @return None
    """
    unpack_window(sign_in_canvas)
    unpack_window(home_canvas)
    pack_window(log_in_canvas)


################################################################

def show_sign_in_frame():
    """
    This function is used to display the sign-in frame in a graphical user interface (GUI).
    It unpacks the log-in canvas and packs the sign-in canvas to make it visible.
    No parameters are required.
    No return value.
    """
    unpack_window(log_in_canvas)
    sign_in_canvas.pack(expand=True, fill=BOTH)


################################################################
# search method
def search_type():
    """
    This function is used to search for products in a GUI application. It takes no arguments.
    It retrieves the search value from an entry widget and refreshes the scroll bar. It then initializes a counter variable `NUMBER_OF_SEARCH` to 0.
    It iterates over each account in `accounts_list` and for each account, it iterates over the `user_product_list` of that account.
    It checks if the search value matches the name or price of the product, or if the search value without spaces matches the name or the concatenation of the name and price of the product.
    If any of these conditions are met, it calls the `display_to_search_frame` method of the product and increments the `NUMBER_OF_SEARCH` counter.
    If the
    """
    search_val = srch_entry.get()
    refresh_scroll_Y()
    NUMBER_OF_SEARCH = 0
    for acc in accounts_list:
        for prds in acc.user_product_list:
            if ((search_val.upper() == prds.get_name().upper() or
                 str(search_val).upper() == str(prds.get_price()).upper()) or
                    str(search_val).upper().replace(" ", "") == str(prds.get_name()).upper().replace(" ", "") or
                    str(search_val).upper().replace(" ", "") == str(
                        str(prds.get_name()) + str(prds.get_price())).upper().replace(" ", "")):

                # search_frame.create_window((220, Y_POSITION), window=type_W,width=350,height=300)
                prds.display_to_search_frame()
                NUMBER_OF_SEARCH += 1
            elif (search_val).upper() in str(prds.get_name()).upper():
                # search_frame.create_window((220, Y_POSITION), window=type_W,width=350,height=300)
                prds.display_to_search_frame()
                NUMBER_OF_SEARCH += 1
    search_frame.itemconfig(search_count_label, text=f"Item: {NUMBER_OF_SEARCH}")
    if NUMBER_OF_SEARCH == 0:
        messagebox.showerror("Products", f"0 Item : {srch_entry.get()}")
        srch_entry.delete(0, END)


def create_img(path, width, heigth):
    """
    Create an image from a given file path and resize it to the specified width and height.
    @param path - The file path of the image.
    @param width - The desired width of the image.
    @param height - The desired height of the image.
    @return The resized image.
    """
    img = Image.open(path)
    img = img.resize((width, heigth))
    img = ImageTk.PhotoImage(img)
    return img


############ center the window
center_window(window, WINDOW_WIDTH, WINDOW_HEIGTH)
########################## BSU LOGO
logo_big = create_img('images/logobsu.png', 100, 100)

logo_big_super = create_img('images/logobsu.png', 200, 200)

logo_med = create_img('images/logobsu.png', 80, 80)

logo_small = create_img('images/logobsu.png', 50, 50)

user_logo = create_img('donwloadimages/user (1).png', 25, 20)
user_logo2 = create_img('donwloadimages/user (2).png', 25, 25)

add_logo = create_img('donwloadimages/plus (2).png', 25, 20)
add_logo2 = create_img('donwloadimages/plus (3).png', 25, 25)

search_logo = create_img('donwloadimages/magnifying-glass.png', 25, 20)
search_logo2 = create_img('donwloadimages/magnifying-glass (1).png', 25, 25)

menu_logo = create_img('donwloadimages/categories.png', 25, 20)
menu_logo2 = create_img('donwloadimages/apps (1).png', 25, 25)

product_logo = create_img('images/shopping-cart (1).png', 25, 25)

home_logo = create_img('donwloadimages/home (1).png', 25, 20)
home_logo2 = create_img('donwloadimages/home (2).png', 25, 25)

sign_outl = create_img('images/sign-out.png', 25, 20)

line_logo = create_img('images/line.png', 25, 1)

bg_img = create_img('images/back_1000.jpg', WINDOW_WIDTH, 700)

con_img2 = create_img('images/image_2000.jpg', 380, 400)

bg_2 = create_img('images/bg2.png', WINDOW_WIDTH, 700)

img_bg_txt = create_img('donwloadimages/bg17.jpg', 175, 200)

con_txt_img = create_img('images/bg17.jpg', 263, 120)

# BACKGROUND IMAGE
user_frame_bg_img = create_img('donwloadimages/white_bg.jpg', WINDOW_WIDTH, 540)

admin_frame_bg_img = create_img('images/bg16.jpeg', WINDOW_WIDTH, 540)

########################## ADMIN WINDOW
inven_img_btn = create_img('donwloadimages/product.png', 60, 60)
users_img_btn = create_img('donwloadimages/multiple-users-silhouette (1).png', 55, 55)
tran_img_btn = create_img('donwloadimages/transaction (1).png', 55, 55)
admin_back = create_img('images/back-arrow.png', 20, 20)

admin_frame = Canvas(window)
############
admin_label = Label(admin_frame, text="Admin", font=('Times', 15, "bold"), bg=bgcolor, height=10, pady=1)
admin_label.pack(fill=X)
log_out_admin = Button(admin_label, image=admin_back, text="Log out", command=admin_log_out, relief='flat',
                       compound='left')
log_out_admin.pack(side='left')

navigataion_frame = Canvas(admin_frame, width=WINDOW_WIDTH, height=WINDOW_HEIGTH)
pack_window(navigataion_frame)
navigataion_frame.create_image(200, 280, image=admin_frame_bg_img)

inven_btn = navigataion_frame.create_image(115, 200, image=inven_img_btn)
navigataion_frame.create_text(115, 240, text="Inventory", font=("Helvetica", 8, "bold"))
navigataion_frame.tag_bind(inven_btn, "<Button>", inventory)

tran_btn = navigataion_frame.create_image(280, 208, image=tran_img_btn)
navigataion_frame.create_text(280, 245, text="Transaction", font=("Helvetica", 8, "bold"))
navigataion_frame.tag_bind(tran_btn, "<Button>", admin_tran)

users_btn = navigataion_frame.create_image(200, 310, image=users_img_btn)
navigataion_frame.create_text(200, 345, text="Users", font=("Helvetica", 8, "bold"))
navigataion_frame.tag_bind(users_btn, "<Button>", users)
########################## INVENTORY WINDOW FRAME

inven_frame = Canvas(admin_frame, bg='red')
Label(inven_frame, text="Inventory", highlightcolor='black', highlightthickness=1, highlightbackground='black',
      relief='flat').pack(side=TOP, fill=X)
top_bar_inven = Label(inven_frame, width=400, highlightcolor='black', highlightthickness=1, highlightbackground='black',
                      relief='flat')
top_bar_inven.pack(side='top')
prd_img_l = Label(top_bar_inven, text="Image", width=10, highlightcolor='black', highlightthickness=1,
                  highlightbackground='black', relief='flat')
prd_img_l.pack(side='left')
prd_typ_l = Label(top_bar_inven, text='product_type', width=18, highlightcolor='black', highlightthickness=1,
                  highlightbackground='black', relief='flat')
prd_typ_l.pack(side='left', fill=Y)
prd_prc_l = Label(top_bar_inven, text='product_price', width=12, highlightcolor='black', highlightthickness=1,
                  highlightbackground='black', relief='flat')
prd_prc_l.pack(side='left', fill=Y)
prd_stk_l = Label(top_bar_inven, text='product_stock', width=12, highlightcolor='black', highlightthickness=1,
                  highlightbackground='black', relief='flat')
prd_stk_l.pack(side='left', fill=Y)

inven_table = Canvas(inven_frame, width=400, highlightcolor='black', highlightthickness=2, highlightbackground='black',
                     relief='flat')
inven_frame_bg = Label(inven_table, image=admin_frame_bg_img)
inven_frame_bg.pack()
inven_table.pack(side='top', expand=True)
########################## USERS WINDOW FRAME

users_frame = Canvas(admin_frame, bg='blue')
Label(users_frame, text="Users", highlightcolor='black', highlightthickness=1, highlightbackground='black',
      relief='flat').pack(side=TOP, fill=X)
top_bar = Label(users_frame, width=400)
top_bar.pack(side='top')
Label(top_bar, width=8, text='Id Picture', highlightcolor='black', highlightthickness=1, highlightbackground='black',
      relief='flat').pack(side='left')
Label(top_bar, width=25, text='name', highlightcolor='black', highlightthickness=1, highlightbackground='black',
      relief='flat').pack(side='left')
Label(top_bar, width=23, text="Address", highlightcolor='black', highlightthickness=1, highlightbackground='black',
      relief='flat').pack(side='left')

users_table = Canvas(users_frame, width=400, highlightcolor='black', highlightthickness=1, highlightbackground='black',
                     relief='flat')
users_bg = Label(users_table, image=admin_frame_bg_img)
users_bg.pack()
users_table.pack(side='top', expand=True)
########################## ADMIN MENU WINDOW FRAME

admin_menu_frame = Canvas(admin_frame, bg='green')

########################### ADMIN TRANSACTION WINDOW FRAME

admin_tran_frame = Canvas(admin_frame, bg='black')
# admin_tran_frame_bg = Label(admin_tran_frame,image=admin_frame_bg_img)
# admin_tran_frame_bg.pack()
# ======================+===============================================================================
Label(admin_tran_frame, text="Transaction", highlightcolor='black', highlightthickness=1, highlightbackground='black',
      relief='flat').pack(side=TOP, fill=X)

tran_table = Canvas(admin_tran_frame, width=400, highlightcolor='black', highlightthickness=2,
                    highlightbackground='black', relief='flat')
tran_frame_bg = Label(tran_table, image=admin_frame_bg_img)

tran_frame_bg.pack()

tran_table.pack(side='top', expand=True)

###################################################################################### USER WINDOW FRAME

user_frame = Canvas(window)

bottom_can_bar = Canvas(user_frame, width=WINDOW_WIDTH, height=35, bg='white')
bottom_can_bar.pack(side="bottom")
################################################################

user_bg_img = create_img('images/log-in-bg.png', WINDOW_WIDTH, WINDOW_HEIGTH)
# sign_in_canvas.create_image(250, 250, image=bg_img)
user_frame_bg = create_img('images/bg_products_F.jpg', WINDOW_WIDTH, 540)

user_frame.create_image(200, 250, image=user_frame_bg)
####################################

bottom_bar_img = create_img('images/bottom-bar.png', WINDOW_WIDTH, 40)

user_frame.create_image(227, WINDOW_HEIGTH - 20, image=bottom_bar_img)

####################################
gap_value = (WINDOW_WIDTH - (menu_logo.width() + user_logo.width() + product_logo.width() + home_logo.width())) / 7

menu_button_c = bottom_can_bar.create_image(WINDOW_WIDTH - (menu_logo.width() + gap_value), 18, image=menu_logo)
bottom_can_bar.tag_bind(menu_button_c, "<Button>", menu)
bottom_can_bar.tag_bind(menu_button_c, "<Enter>", lambda event: hover_bar(0))
bottom_can_bar.tag_bind(menu_button_c, "<Leave>", lambda event: unhover_bar(0))
#############
#############
prof_button_c = bottom_can_bar.create_image(WINDOW_WIDTH - (menu_logo.width() + user_logo.width() + (gap_value * 2)),
                                            18, image=user_logo)
bottom_can_bar.tag_bind(prof_button_c, "<Button>", profile)
bottom_can_bar.tag_bind(prof_button_c, "<Enter>", lambda event: hover_bar(1))
bottom_can_bar.tag_bind(prof_button_c, "<Leave>", lambda event: unhover_bar(1))

add_button_c = bottom_can_bar.create_image(
    WINDOW_WIDTH - (menu_logo.width() + user_logo.width() + product_logo.width() + (gap_value * 3)), 18,
    image=add_logo)
bottom_can_bar.tag_bind(add_button_c, "<Button>", add_product)
bottom_can_bar.tag_bind(add_button_c, "<Enter>", lambda event: hover_bar(2))
bottom_can_bar.tag_bind(add_button_c, "<Leave>", lambda event: unhover_bar(2))

search_button_c = bottom_can_bar.create_image(WINDOW_WIDTH - (
        menu_logo.width() + user_logo.width() + product_logo.width() + search_logo.width() + (gap_value * 4)), 18,
                                              image=search_logo)
bottom_can_bar.tag_bind(search_button_c, "<Button>", mysearch)
bottom_can_bar.tag_bind(search_button_c, "<Enter>", lambda event: hover_bar(3))
bottom_can_bar.tag_bind(search_button_c, "<Leave>", lambda event: unhover_bar(3))

home_button_c = bottom_can_bar.create_image(WINDOW_WIDTH - (
        menu_logo.width() + user_logo.width() + product_logo.width() + search_logo.width() + home_logo.width() + (
        gap_value * 5)), 18, image=home_logo)
bottom_can_bar.tag_bind(home_button_c, "<Button>", show_products)
bottom_can_bar.tag_bind(home_button_c, "<Enter>", lambda event: hover_bar(4))
bottom_can_bar.tag_bind(home_button_c, "<Leave>", lambda event: unhover_bar(4))

# =================================================================== buy frame

buy_frame = Canvas(user_frame, highlightbackground="black",
                   highlightcolor="black",
                   highlightthickness=2,
                   height=500,
                   bg="white"
                   )
# label = Label(buy_frame, text='BUY')
# label.pack(side=TOP)
# product_image_BF = None

##############
buy_frame_bg_img = create_img('images/bgnanaman.jpg', 390, 510)
# buy_frame.create_image(190,255,image=buy_frame_bg_img) #create background image of buyframe
###############
quan_menu_img = create_img('images/txt-box.png', 190, 190)
# buy_frame.create_image(270,270,image=quan_menu_img)

product_info_BF = buy_frame.create_text(110, 310, text="", font=("Calibre", 10, "bold"),
                                        fill="black")  # create text information
##############
buy_btn_img = create_img('images/buy.png', 70, 55)  # image for buy button

buy_button = buy_frame.create_image(290, 470, image=buy_btn_img)  # create button
##############
prof_btn_img = create_img('images/user.png', 20, 20)  # image for buy button

view_profile_button = buy_frame.create_image(280, 310, image=prof_btn_img)  # create button
buy_frame.create_text(280, 330, text="Profile", font=("Calibre", 6, "bold"),
                      fill="black")  # create text 'profile' label
##############
product_picture = Label(buy_frame, highlightbackground="black", highlightcolor="black",
                        highlightthickness=2)  # Product image container
buy_frame.create_window(190, 140, window=product_picture, width=250, height=250)
buy_frame.create_line(10, 280, 370, 280, width=2, fill="black")

# amount = Label(buy_frame)
# amount.pack(side=LEFT)
############

new_quan = IntVar()
quan_menu = Spinbox(buy_frame, width=15)
quan_menu.place(x=170, y=400)

############ payment text
payment_txt = buy_frame.create_text(40, 470, text="Payment: 0")
# buy_button.pack(side=BOTTOM)

########################## MENU WINDOW FRAME
log_out_img = create_img('donwloadimages/logout (1).png', 25, 25)
trans_image = create_img('donwloadimages/transaction (1).png', 25, 25)
mypd_img = create_img('donwloadimages/product.png', 25, 25)
cart_logo = create_img('images/shopping-cart (1).png', 25, 25)

log_out_img2 = create_img('donwloadimages/logout (3).png', 27, 27)
trans_image2 = create_img('donwloadimages/transaction.png', 27, 27)
mypd_img2 = create_img('donwloadimages/product (1).png', 27, 27)
cart_logo2 = create_img('donwloadimages/shopping-cart (1).png', 27, 27)

menu_frame = Canvas(user_frame, bg='black')
menu_frame.create_image(200, 270, image=user_frame_bg_img)
menu_frame.create_image(200, 280, image=logo_big_super)

menu_box = Canvas(menu_frame, bg='white',
                  height=580)
menu_box.pack(side='right')

txt1 = menu_box.create_text(69, 25, text="Log out")
log_out = menu_box.create_image(30, 25, image=log_out_img)
menu_box.tag_bind(log_out, '<Button>', user_log_out)
menu_box.tag_bind(log_out, "<Enter>", lambda event: hover_menu(0))
menu_box.tag_bind(log_out, "<Leave>", lambda event: unhover_menu(0))
menu_box.tag_bind(txt1, '<Button>', user_log_out)
menu_box.tag_bind(txt1, "<Enter>", lambda event: hover_menu(0))
menu_box.tag_bind(txt1, "<Leave>", lambda event: unhover_menu(0))

txt2 = menu_box.create_text(69, 76, text="Transact")
show_transaction_btn = menu_box.create_image(30, 75, image=trans_image)
menu_box.tag_bind(show_transaction_btn, '<Button>', mytransaction)
menu_box.tag_bind(show_transaction_btn, "<Enter>", lambda event: hover_menu(1))
menu_box.tag_bind(show_transaction_btn, "<Leave>", lambda event: unhover_menu(1))
menu_box.tag_bind(txt2, '<Button>', mytransaction)
menu_box.tag_bind(txt2, "<Enter>", lambda event: hover_menu(1))
menu_box.tag_bind(txt2, "<Leave>", lambda event: unhover_menu(1))

txt3 = menu_box.create_text(69, 127, text="Products")
show_products_btn = menu_box.create_image(30, 125, image=mypd_img)
menu_box.tag_bind(show_products_btn, '<Button>', myproducts)
menu_box.tag_bind(show_products_btn, "<Enter>", lambda event: hover_menu(2))
menu_box.tag_bind(show_products_btn, "<Leave>", lambda event: unhover_menu(2))
menu_box.tag_bind(txt3, '<Button>', myproducts)
menu_box.tag_bind(txt3, "<Enter>", lambda event: hover_menu(2))
menu_box.tag_bind(txt3, "<Leave>", lambda event: unhover_menu(2))

######## cart button
txt4 = menu_box.create_text(62, 175, text="Cart")
cart_button_c = menu_box.create_image(30, 175, image=cart_logo)
menu_box.tag_bind(cart_button_c, "<Button>", cart)
menu_box.tag_bind(cart_button_c, "<Enter>", lambda event: hover_menu(3))
menu_box.tag_bind(cart_button_c, "<Leave>", lambda event: unhover_menu(3))
menu_box.tag_bind(txt4, "<Button>", cart)
menu_box.tag_bind(txt4, "<Enter>", lambda event: hover_menu(3))
menu_box.tag_bind(txt4, "<Leave>", lambda event: unhover_menu(3))

########################## ADD PRODUCT WINDOW FRAME

sell_frame = Canvas(user_frame, bg='yellow')
sell_frame.create_image(200, 260, image=user_frame_bg_img)

open_img_btn = create_img('donwloadimages/picture (4).png', 20, 20)
txt_box_Add = create_img('images/txt-box.png', 100, 50)

conatainer_2 = LabelFrame(sell_frame, width=300, height=400, relief='flat')

sell_frame.create_window(200, 250, window=conatainer_2, width=380, height=400)

sell_container = Canvas(conatainer_2, highlightcolor='black', highlightbackground='black', highlightthickness=2,
                        relief='flat')
sell_container.create_image(190, 200, image=con_img2)

upload_image = Button(sell_container, command=lambda: upload_image_function(),
                      text="Product image",
                      image=open_img_btn,
                      relief='flat')
upload_image.place(x=185, y=75)

upload_name_of_product = StringVar()
type_of_product = ['School Supply', 'School Uniform']
style = ttk.Style()
style.theme_use('clam')
style.configure('info.TCombobox', fielbackground='white', background='white')
types = ttk.Combobox(sell_container, textvariable=upload_name_of_product,
                     values=type_of_product,
                     width=15,
                     state="readonly",
                     background="#F3F2ED",
                     font=("Times", 10),
                     style='info.TCombobox',
                     )
types.place(x=185, y=120)
# upload_name_of_product = Entry(sell_frame)
# upload_name_of_product.pack()

upload_price = Entry(sell_container,
                     bd=0,
                     highlightthickness=0,
                     bg="#F3F2ED",
                     )
upload_price.place(x=185, y=160)

upload_stock = Entry(sell_container,
                     bd=0,
                     highlightthickness=0,
                     bg="#F3F2ED",
                     )
upload_stock.place(x=185, y=200)

upload_contact = Entry(sell_container,
                       bd=0,
                       highlightthickness=0,
                       bg="#F3F2ED",
                       )
upload_contact.place(x=185, y=240)

POS_OF_TXT_BOX = 182
for txt_bx in range(0, 3):
    sell_container.create_line(185, POS_OF_TXT_BOX, 310, POS_OF_TXT_BOX, width=2)
    POS_OF_TXT_BOX += 39

labels = ['Contact Number:', 'Stock:', 'Price:', 'Type:', 'Image:']
POS_OF_TXT_LABELS = 50
for label in reversed(labels):
    POS_OF_TXT_LABELS += 40
    sell_container.create_text(88, POS_OF_TXT_LABELS, text=label, font=("Times", 9))

upload_product = Button(sell_container,
                        command=lambda: save_product(product_img, types.get(), upload_price.get(),
                                                     upload_stock.get(), upload_contact.get()),
                        text="Uplaod",
                        relief='flat'

                        )
upload_product.place(x=165, y=300)
sell_container.pack(expand=True, fill=BOTH)
# conatainer_2.pack(expand=True)

# ==================================================================================  CART WINDOW FRAME

cart_frame_bg = create_img('images/bgnanaman.jpg', 470, 610)

cart_main_frame = Canvas(user_frame)

cart_bg = Label(cart_main_frame, image=user_frame_bg_img, width=WINDOW_WIDTH, height=30)
cart_bg.pack()

cart_frame = Canvas(cart_main_frame, width=WINDOW_WIDTH, height=500, scrollregion=(0, 0, 200, 200))
pack_window(cart_frame)

# cart_bg.bind("<Configure>", lambda e: cart_frame.configure(scrollregion=cart_frame.bbox("all")))
# cart_bg.bind("<MouseWheel>", on_mousewheel_carts_F)

# ====================================================================================== SEARCH WINDOW FRAME

search_frame_bg = create_img('images/bgnanaman.jpg', 470, 610)

search_frame = Canvas(user_frame, bg='red')
search_frame.create_image(200, 270, image=user_frame_bg_img)

search_frame_container = Canvas(search_frame,
                                width=WINDOW_WIDTH - 10,
                                height=480,
                                scrollregion=(0, 0, 200, 200),
                                highlightthickness=1,
                                bd=1,
                                highlightbackground='black',
                                highlightcolor='black')

search_frame_container.pack(side='bottom')

Label(search_frame_container, width=WINDOW_WIDTH, height=490, image=user_frame_bg_img, anchor='s').pack(fill=BOTH,
                                                                                                        expand=True)

srch_entry = Entry(search_frame, width=25,
                   font=('Times', 12),
                   relief='flat',
                   highlightcolor="black",
                   highlightthickness=1,
                   highlightbackground='black')
srch_entry.place(x=60, y=20)
search_count_label = search_frame.create_text(23, 460, text="Item : 0", fill="white")
search_img_2 = create_img('images/search logo.png', 15, 10)
srch_btn = Button(search_frame, text="Search", command=search_type, relief='flat', image=search_img_2, compound='left',
                  bg='white')
srch_btn.place(x=270, y=20)
# ========================================================================================= PROFILE WINDOW FRAME

profile_frame = Canvas(user_frame,
                       bg=bgcolor,

                       )

prof_background_img = create_img('images/profbg.jpg', 470, 610)

profile_frame.create_image(205, 256, image=user_frame_bg_img)
# bg_prof = Label(profile_frame, image=bg_2)
# bg_prof.pack()
profile_frame.create_line(50, 50, 350, 250, width=2)
profile_pic = Label(profile_frame, width=150, height=175,
                    highlightcolor='black',
                    highlightthickness=2,
                    highlightbackground='black',
                    )
profile_pic.place(x=125, y=70)

user_information = profile_frame.create_text(205, 320, text='', font=("Times", 30, 'bold'))
user_address = profile_frame.create_text(205, 350, text='', font=("Times", 20, 'bold'), fill="#100C08")

# ========================================================================================= PRODUCTS WINDOW FRAME

# container image
con_bg_img = create_img('images/productcont.jpg', 170, 170)

buy_img = create_img('images/buy (2).png', 50, 33)

product_main_frame = Canvas(user_frame, bg="red")

product_frame = Canvas(product_main_frame, bg='#deb887', scrollregion=(0, 0, 200, 200), width=WINDOW_WIDTH,
                       height=550)
product_frame.pack(fill=X, side="bottom")

background_of_PF = Label(product_frame, width=WINDOW_WIDTH, height=480, image=user_frame_bg_img, anchor='s')
background_of_PF.pack(fill=BOTH, expand=True)

# product_frame.create_image(220,256 , image = product_frame_bg)
background_of_prod_frame = Canvas(product_main_frame, width=WINDOW_WIDTH, bd=0, height=50, highlightthickness=0,
                                  highlightcolor="black", highlightbackground='black')
background_of_prod_frame.pack(fill=BOTH, expand=True)

# create image bacakground for home
background_of_prod_frame.create_image(200, 258, image=user_frame_bg_img)

########
background_of_prod_frame.create_text(200, 20, text="SPAR Shop", font=('Times', 20), fill="black")

##========================================================================================= USER PRODUCTS WINDOW FRAME

user_products_frame = Canvas(user_frame, bg='orange')

user_products_frame.create_image(200, 275, image=user_frame_bg_img)
my_product_container = Canvas(user_products_frame, width=400, height=500)

my_product_container.pack(side='bottom')
########################## USER transaction WINDOW FRAME
user_transaction_frame = Image.open('images/bg15.jpeg')
user_transaction_frame_bg = user_transaction_frame.resize((470, 610))
user_transaction_frame_bg = ImageTk.PhotoImage(user_transaction_frame_bg)

user_transaction_frame = Canvas(user_frame)

user_transaction_frame.create_image(220, 256, image=user_transaction_frame_bg)

########################## SIGN UP WINDOW FRAME

sign_in_canvas = Canvas(window, bg=bgcolor)
######### gaps value

#########

sign_txt_bx = create_img('images/txt-box.png', 300, 70)

sign_img_bx = create_img('images/txt-box.png', 100, 50)

back_to_img = create_img('images/back-arrow.png', 30, 30)

sign_to_img = create_img('images/sign-in.png', 160, 80)

sign_bg_img = create_img('images/new-.jpg', WINDOW_WIDTH, WINDOW_HEIGTH)

sign_out_img = create_img('images/sign-out.png', 725, 616)

# sign_in_canvas.create_image(250, 250, image=bg_img)

sign_in_canvas.create_image(WINDOW_WIDTH - (sign_bg_img.width() // 2), 300, image=sign_bg_img)

back_to_log = sign_in_canvas.create_image(20, 20, image=back_to_img)
sign_in_canvas.tag_bind(back_to_log, "<Button>", lambda event: back_to_log_com())
######## gaps value

sign_txt_box_gap = (WINDOW_WIDTH - sign_txt_bx.width()) // 2
########

# outline = sign_in_canvas.create_image(230,300,image=sign_out_img)
#############

######## create logo in log in box and gap value
sign_login_gap_W = (WINDOW_WIDTH - logo_med.width()) // 2
sign_in_canvas.create_image(sign_login_gap_W + (logo_med.width() // 2), 90, image=logo_med)

######## create log in text
sign_in_canvas.create_text(sign_login_gap_W + (logo_med.width() // 2), 155, text="Sign up",
                           font=("Segoe UI Black", 24, "bold"))

######## create username label
sign_in_canvas.create_text(120, 210, text="Name", font=("Calibre", 8, "bold"))
######## create username label
sign_in_canvas.create_text(130, 260, text="Address", font=("Calibre", 8, "bold"))
######## create username label
sign_in_canvas.create_text(130, 310, text="Username", font=("Calibre", 8, "bold"))
######## create username label
sign_in_canvas.create_text(130, 360, text="Password", font=("Calibre", 8, "bold"))
######## create username label
sign_in_canvas.create_text(155, 410, text="Confirm Password", font=("Calibre", 8, "bold"))

#############

name_txt_box = sign_in_canvas.create_image(sign_txt_box_gap + (sign_txt_bx.width() // 2), 220, image=sign_txt_bx)

address_txt_box = sign_in_canvas.create_image(sign_txt_box_gap + (sign_txt_bx.width() // 2), 270, image=sign_txt_bx)

username_txt_box = sign_in_canvas.create_image(sign_txt_box_gap + (sign_txt_bx.width() // 2), 320, image=sign_txt_bx)

password_txt_box = sign_in_canvas.create_image(sign_txt_box_gap + (sign_txt_bx.width() // 2), 370, image=sign_txt_bx)

confirm_txt_box = sign_in_canvas.create_image(sign_txt_box_gap + (sign_txt_bx.width() // 2), 420, image=sign_txt_bx)

# button to open id picture
img_box = sign_in_canvas.create_image((sign_txt_box_gap + ((sign_txt_bx.width() // 2) - 80)), 460, image=sign_img_bx)
sign_in_canvas.tag_bind(img_box, "<Button>", lambda event: open_id_image())

############
# logo
# sign_in_canvas.create_image(220,50,image=logo_med)

# sign label
# sign_in_canvas.create_text(220,90,text="Sign in",font=(tk_font,20,"bold"))

# insert user profile

insert_id = Button(sign_in_canvas, text="Upload id",
                   bg='red',
                   font=(tk_font, 8),
                   command=lambda: open_id_image())
# insert_id.place(x=80,y=150)


######## create name entry
sign_user_name = Entry(sign_in_canvas,
                       width=33,
                       font=(tk_font, 10),
                       bg="#F3F2ED",
                       bd=0)
######## display the name entry
sign_user_name.place(x=(sign_txt_box_gap + ((sign_txt_bx.width() // 2) - 80)) - 29, y=227)

######## bind the username entry,this binding appear the line inside of entry box if the cursor enter
# sign_user_name_label.bind("<Enter>",lambda event:enter_txt_U())

######## create line inside of entry box
usr_name_line_S = sign_in_canvas.create_line((sign_txt_box_gap + ((sign_txt_bx.width() // 2) - 80)) - 29, 246,
                                             ((sign_txt_box_gap + ((sign_txt_bx.width() // 2) - 80)) - 29) + 230, 246,
                                             fill="black", width=1)

######## bind the username entry,this binding appear the line inside of entry box if the cursor enter
# sign_user_name_label.bind("<Enter>",lambda event:enter_txt_U())

# create sign address entry
sign_user_address = Entry(sign_in_canvas,
                          width=33,
                          font=(tk_font, 10),
                          bg="#F3F2ED",
                          bd=0)
sign_user_address.place(x=(sign_txt_box_gap + ((sign_txt_bx.width() // 2) - 80)) - 29, y=276)

######## create line inside of entry box
address_line_S = sign_in_canvas.create_line((sign_txt_box_gap + ((sign_txt_bx.width() // 2) - 80)) - 29, 295,
                                            ((sign_txt_box_gap + ((sign_txt_bx.width() // 2) - 80)) - 29) + 230, 295,
                                            fill="black", width=1)

######## create sign user username entry
sign_in_username = Entry(sign_in_canvas,
                         width=33,
                         font=(tk_font, 10),
                         bg="#F3F2ED",
                         bd=0)
sign_in_username.place(x=(sign_txt_box_gap + ((sign_txt_bx.width() // 2) - 80)) - 29, y=327)

######## create line inside of entry box
username_line_S = sign_in_canvas.create_line((sign_txt_box_gap + ((sign_txt_bx.width() // 2) - 80)) - 29, 346,
                                             ((sign_txt_box_gap + ((sign_txt_bx.width() // 2) - 80)) - 29) + 230, 346,
                                             fill="black", width=1)

####### create sign user password entry
sign_in_password = Entry(sign_in_canvas,
                         width=33,
                         font=(tk_font, 10),
                         bg="#F3F2ED",
                         bd=0)
sign_in_password.place(x=(sign_txt_box_gap + ((sign_txt_bx.width() // 2) - 80)) - 29, y=376)

######## create line inside of entry box
pass_line_S = sign_in_canvas.create_line((sign_txt_box_gap + ((sign_txt_bx.width() // 2) - 80)) - 29, 395,
                                         ((sign_txt_box_gap + ((sign_txt_bx.width() // 2) - 80)) - 29) + 230, 395,
                                         fill="black", width=1)

# confirm pass word label / input

# sign confirm password entry
confirm_pass = Entry(sign_in_canvas,
                     width=33,
                     font=(tk_font, 10),
                     bg="#F3F2ED",
                     bd=0,
                     show="*")
confirm_pass.place(x=(sign_txt_box_gap + ((sign_txt_bx.width() // 2) - 80)) - 29, y=427)

######## create line inside of entry box
confirm_line_S = sign_in_canvas.create_line((sign_txt_box_gap + ((sign_txt_bx.width() // 2) - 80)) - 29, 446,
                                            ((sign_txt_box_gap + ((sign_txt_bx.width() // 2) - 80)) - 29) + 230, 446,
                                            fill="black", width=1)

# create sign in button
sign_btn_gap = (WINDOW_WIDTH - sign_to_img.width()) // 2
sign_in_button = sign_in_canvas.create_image(sign_btn_gap + (sign_to_img.width() // 2), 530, image=sign_to_img)
try:
    sign_in_canvas.tag_bind(sign_in_button, "<Button>",
                            lambda event: sign_in())
except NameError as e:
    messagebox.showerror("Error", 'Please fill in all the required fields to create an account')
########################## LOG IN  PRODUCT WINDOW FRAME
# create window for log in
log_in_canvas = Canvas(window)
#########
crt_acc_btn = create_img('images/crt_acc.png', 230, 60)

log_outl = create_img('images/log_out.png', 430, 460)

txt_bx = create_img('images/txt-box.png', 300, 70)

log_btn = create_img('images/log-in.png', 170, 70)

log_in_b = create_img('images/log in.png', 60, 20)

sign_in_b = create_img('images/signin.png', 60, 20)

moon_img = create_img('images/switch (1).png', 40, 40)

sun_img = create_img('images/switch.png', 40, 40)

log_bg_img = create_img('images/new-.jpg', WINDOW_WIDTH, WINDOW_HEIGTH)

show_pass_img = create_img('images/eye2.png', 20, 15)

hide_pass_img = create_img('images/eye2.png', 20, 15)

####### gap values
log0_login_gap_W = (WINDOW_WIDTH - logo_med.width()) // 2
txt_box_gap = (WINDOW_WIDTH - txt_bx.width()) // 2
log_btn_gap = (WINDOW_WIDTH - log_btn.width()) // 2
crt_btn_gap = (WINDOW_WIDTH - crt_acc_btn.width()) // 2

######## background
log_in_canvas.create_image(WINDOW_WIDTH - (log_bg_img.width() // 2), 300, image=log_bg_img)
###########
######## password show config
pass_btn_config = log_in_canvas.create_image(txt_box_gap + (txt_bx.width() // 2) + 150, 325, image=show_pass_img)

log_in_canvas.tag_bind(pass_btn_config, "<Button>", lambda event: show_password())

switch = log_in_canvas.create_image(25, 25, image=sun_img)

log_in_canvas.tag_bind(switch, "<Button>", lambda event: change_bg_color())

######## log in box background
# log_in_canvas.create_image(227,300,image=log_outl)

######## create logo in log in box
log_in_canvas.create_image((log0_login_gap_W + (logo_med.width() // 2)), 120, image=logo_med)

######## create log in text
log_in_canvas.create_text((log0_login_gap_W + (logo_med.width() // 2)), 185, text="Log in",
                          font=("Segoe UI Black", 24, "bold"))

######## create entry box
txt_boxU = log_in_canvas.create_image(txt_box_gap + (txt_bx.width() // 2), 260, image=txt_bx)
txt_boxP = log_in_canvas.create_image(txt_box_gap + (txt_bx.width() // 2), 310, image=txt_bx)

######## create username label
username_txt = log_in_canvas.create_text(txt_box_gap + ((txt_bx.width() // 2) - 80), 250, text="Username",
                                         font=("Calibre", 8, "bold"))
######## create password label
password_txt = log_in_canvas.create_text(txt_box_gap + ((txt_bx.width() // 2) - 80), 300, text="Password",
                                         font=("Calibre", 8, "bold"))

######## create button for log in
btn_log_in = log_in_canvas.create_image(log_btn_gap + (log_btn.width() // 2), 390, image=log_btn)
log_in_canvas.tag_bind(btn_log_in, "<Button>", lambda event: log_in_validation())

######## create button for create account
log_in_canvas.create_text(crt_btn_gap + (crt_acc_btn.width() // 2), 430, text="Don't have an account?")
btn_crt_acc = log_in_canvas.create_image((log_btn_gap + (log_btn.width())) - 76, 470, image=crt_acc_btn)
log_in_canvas.tag_bind(btn_crt_acc, "<Button>", lambda event: show_sign_in_frame())

############
######## create username entry
log_in_username = Entry(log_in_canvas,
                        width=33,

                        font=(tk_font, 10),
                        bg="#F3F2ED",
                        bd=0)
######## display the username entry
log_usernmae_gap_val = (WINDOW_WIDTH - log_in_username.winfo_width()) // 5

log_in_username.place(x=(txt_box_gap + ((txt_bx.width() // 2) - 80)) - 29, y=267)
######## create show and hide password button
######## bind the username entry,this binding appear the line inside of entry box if the cursor enter
log_in_username.bind("<Enter>", lambda event: enter_txt_U())

######## create line inside of entry box
usr_name_line = log_in_canvas.create_line((txt_box_gap + ((txt_bx.width() // 2) - 80)) - 29, 286,
                                          ((txt_box_gap + ((txt_bx.width() // 2) - 80)) - 29) + 230, 286,
                                          fill="#F3F2ED", width=1)

######### create password entry
log_in_password = Entry(log_in_canvas,
                        width=33,
                        show="*",
                        bg="#F3F2ED",
                        font=(tk_font, 10),
                        bd=0)

######## display the password entry
log_password_gap_val = (WINDOW_WIDTH - log_in_password.winfo_width()) // 2
log_in_password.place(x=(txt_box_gap + ((txt_bx.width() // 2) - 80)) - 29, y=315)

######## create line inside of entry box
usr_p_line = log_in_canvas.create_line((txt_box_gap + ((txt_bx.width() // 2) - 80)) - 29, 336,
                                       ((txt_box_gap + ((txt_bx.width() // 2) - 80)) - 29) + 230, 336, fill="#F3F2ED",
                                       width=1)

######## bind the password entry,this binding appear the line inside of entry box if the cursor enter
log_in_password.bind("<Enter>", lambda event: enter_txt_P())

########################## WELCOCME HOME WINDOW FRAME

con = Image.open('images/icons8-log-in-50.png')
con = ImageTk.PhotoImage(con)

logo_spar = create_img('images/logo_spar.png', 400, 380)

get_start_img = create_img('images/getstartedbtn.png', 120, 60)

wel_bg = create_img('images/new-.jpg', WINDOW_WIDTH, WINDOW_HEIGTH)

myLogo = create_img('images/sa.png', 170, 170)

spar_logo = create_img('images/spartan.png', 80, 80)
#########

home_canvas = Canvas(window, bg=bgcolor)
# gap value
gap_button_start_val = (WINDOW_WIDTH - get_start_img.width()) // 2
gap_logo_val = (WINDOW_WIDTH - myLogo.width()) // 2

# welcome background
home_canvas.create_image(WINDOW_WIDTH - (wel_bg.width() // 2), WINDOW_HEIGTH - (wel_bg.height() // 2), image=wel_bg)

home_canvas.create_image(gap_logo_val + (myLogo.width() // 2), 190, image=myLogo)
# home_canvas.create_image(220,100,image=spar_logo)

tagline = f"           Empowering Spartans – A \nBatStateU - NEU Marketplace for School Supplies\n\t\tand Uniforms"
gap_tagline_val = (WINDOW_WIDTH - len(tagline)) // 2
bsu_tagline = home_canvas.create_text(gap_tagline_val + (len(tagline) // 2), 330, text="",
                                      font=("Bahnschrift Light Condensed", 15), fill="black")
write_text(1)
home_canvas.create_image(30, 30,
                         image=logo_small)

get_started_button = home_canvas.create_image(gap_button_start_val + (get_start_img.width() // 2), 495,
                                              image=get_start_img)

home_canvas.tag_bind(get_started_button, "<Button>", lambda event: show_log_in_frame())
################################################################

qt = Label(window, height=10, bg='white')
qt.pack(side=TOP, fill=X)
btn_quit = Button(qt, command=lambda: window.quit(), text="X", fg='black', bg='white', font=("monosacpe", 10, 'bold'),
                  relief=FLAT)
btn_quit.pack(side='right', anchor=SW)

if __name__ == '__main__':
    size_check()
    s = ttk.Style()
    s.theme_use('clam')
    restore_db_to_list()
    restore_carts()
    welcome()
    print(product_pos.X_POSITION)
# Activate the main window
window.mainloop()
