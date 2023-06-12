from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import ast; import sqlite3; import hashlib; import uuid; import os

# create a Tkinter window
root = Tk()

#################---TRIAL (Removing window title)---##################
root.title("")
root.attributes('-topmost', False),('-alpha', 0.8),('-toolwindow', True),('-style', 'dialog')

# set the window size
win_width = 925; win_height = 500                       #   remove semicolon if required
root.geometry(f'{win_width}x{win_height}+300+200')
root.configure(bg="#fff")
root.resizable(FALSE,FALSE)

### Global variable ###
font_1          = 'Microsoft YaHei UI Light'
global_path     = os.path.dirname(__file__)
resources_path  = os.path.join(global_path, "resources")
db_path         = os.path.join(global_path, "db")
form_type       = 1

### Button config ###
theme_button_mode               = True
password_button1_mode           = True             # True = show password, False = hide password
password_button2_mode           = True
confirm_password_button_mode    = True

path_show_password_button = os.path.join(resources_path, "show_password.png")
show_password_button = PhotoImage(file=path_show_password_button)                                             ## Locate image ##

path_hide_password_button = os.path.join(resources_path, "hide_password.png")
hide_password_button = PhotoImage(file=path_hide_password_button)

### Form config ###
username_input1          = '' 
password_input1         = ''
confirm_password_input  = ''

# Global variable declarations
user_table_definition = """
CREATE TABLE Users (USERNAME TEXT, PASSWORD_HASH TEXT,RECORD_ID TEXT)"""

# Connect to db. Create entity
path_db_file = os.path.join(db_path, "Accounts.db")
connection = sqlite3.connect(path_db_file)                  # sqlite3.connect(global_path+DB_NAME)                                                                 #   Insert global path
cursor_master = connection.cursor()
cursor_master.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Users'")
if cursor_master.fetchone() is None:
    cursor = connection.cursor()
    cursor.execute(user_table_definition)
    connection.commit()
    cursor.close()

cursor_master.close(); connection.close()



def login():
    global form_type
    form_type = 0
    def signin():
        #username=user.get(); password=pw.get()
        username = username_input1; password = password_input1

#   Login auth (version 1)
        if username is None or password is None:
            display_status(0)
        else:
            db_conn = sqlite3.connect(path_db_file)
            cursor_user = db_conn.cursor()
            cursor_user.execute("SELECT username,password_hash,record_id FROM Users WHERE username=?", (username,))
            row = cursor_user.fetchone()
        
        if row is not None:
            salt_db = row[2]
            password_hash_db = row[1]
            password_hash = encrypt_pw(salt_db,password)
            if password_hash_db != password_hash:
                display_status(0)

            else:
                screen=Toplevel(root)
                screen.title("App")
                screen.geometry('925x500+300+200')
                screen.config(bg='white')
                display_status(1)
                Label(screen,text='PASSED', bg='#fff', fg='green', font=('Calibri(Body)',50,'bold')).pack(expand=True)
                screen.mainloop()

        else:
            display_status(0)
            
    def encrypt_pw(salt,password):
        encrypt = hashlib.sha512((salt + password).encode("UTF-8")).hexdigest()
        return encrypt
    
    def display_status(status):
        if status == 0:
            login_status.config(text="Invalid username/password",fg='red',bg='white')
            
        else:
            login_status.config(text="Login successful", fg='green', bg='white')


###########################################################-REMOVE-###################################################################

    #####################################################################
    #   Load the vector file (.eps) using PIL //Parvat = PV
    path_login_logo = os.path.join(resources_path, "login.eps")
    image = Image.open (path_login_logo)                       

    #   Resize
    new_width, new_height = 398,332
    image = image.resize((new_width,new_height))

    #   Convert .eps file to Tkinter-compatible format                                 
    tk_image = ImageTk.PhotoImage(image=image)

    #   Create label for image
    Label(root, image=tk_image,bg='White').place(x=50,y=50, width=400,height=400)


    #Login box frame (PV)
    frame= Frame(root,width=350, height=350,bg='white')                                         #Don't '.place' here, shifts frame to the other side
    frame.place(x=480,y=90)                                                                     #edited 70 -> 90

    heading=Label(frame,text='Sign In',fg='#57a1f8',bg='white',font=(font_1,23,'bold'))
    heading.place(x=100,y=5)

### This part handles changing icon and sets global value ###
    def toggle_password():
        global password_button1_mode
        print("Here")

        if password_button1_mode:
            password_toggle_mode.config(image = show_password_button)
            #pw.config(show = '*')
            password_button1_mode = False
            password_mode()

        else:
            password_toggle_mode.config(image = hide_password_button)
            #pw.config(show = '')
            password_button1_mode = True
            password_mode()

### Shows/Hide password ###
    def password_mode():
        password = pw.get()                         # Password mode
        print("Leave password")
        print(password)
        if password != '' and password != ' Password':
            global password_input1
            password_input1 = password
        else:
            password_input1 = '' 
########################################################
        if password_input1 == '':
            pw.config(show = '')
            pw.delete(0,'end')
            pw.insert(0,' Password')
        
        elif password_button1_mode:
            pw.config(show = '')
            
        else:
            pw.config(show = '*')            

    def registrationX():
        global form_type
        form_type = 2
        root.quit()

    ### ### root.bind('<Return>',(lambda e, sign_in_button=sign_in_button: sign_in_button.invoke()))
    #####################---------------------------------------------------------
#    global username_input
    def on_enter_username(e):
        if  username_input1 == '':
            user.delete(0,'end')

    def on_leave_username(e):
        name = user.get()
        if name == '':
            global username_input1
            user.insert(0,' Username')
            #user.config(fg='gray')
            username_input1 = ''
        elif user.get() == ' Username':
            username_input1 = ''
        else:
            username_input1 = user.get()      

    user = Entry(frame,width = 25,fg = 'black',border = 0,bg = "white",font = (font_1,11)) # Cannot use: .place(x=30,y=80),causes error
    user.place(x = 30,y = 80)
    user.insert(0,' Username')
    user.bind('<FocusIn>', on_enter_username) and user.bind('<FocusOut>', on_leave_username)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107) #25,107
    #####################---------------------------------------------------------
    def on_enter_password(e):
        if  password_input1 == '':
            pw.delete(0,'end')
        
        if password_button1_mode:
            pw.config(show = '')
        
        else:
            pw.config(show = '*')

    def on_leave_password(e):

        """if password == '':
            global password_input
            pw.insert(0,'Password')
            pw.config(fg='gray')
            pw.config(show = '')
            password_input = ''
        elif password == 'Password':
            pw.config(show = '')
            password_input = ''

        else:
            password_input = password
            if password_button_mode:

                pw.config(show = '')
            
            else:
                pw.config(show = '*')
        """
        password_mode()

    pw = Entry(frame,width=25,fg='black',border=0,bg="White",font=(font_1,11)) # Cannot use: .place(x=30,y=150)
    pw.place(x=30,y=150)
    pw.bind('<FocusIn>', on_enter_password) and pw.bind('<FocusOut>', on_leave_password)
    # No need pw.config(show = '*')
    

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)  #Frame(frame,width=295,height=2,bg='black',placeholder_text = 'Test').place(x=25,y=177)
    ##############################################################################

    sign_in_button=Button(frame,width=39,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0,command=signin ).place(x=35,y=240)
    label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=(font_1,9)).place(x=75,y=300)

    sign_up = Button(frame,width= 6,text='Sign up', border = 0, bg = 'white',cursor ='hand2', fg='#57a1f8', command = registrationX).place(x=225,y=300)

    password_toggle_mode = Button(root, width=24,height = 24, pady=7, bd = 0, bg = 'white', command = toggle_password)            # No need (image = show_password_button,)
    password_toggle_mode.place(x=770,y=238)

    login_status = Label(frame,text="",fg='white',bg='white')     
    login_status.place(x=75,y=330)

    toggle_password()                           # Triggers function once, turns to false state

    # run the window
    root.mainloop()

    #return


def registration():
    global form_type
    form_type = 0
    def signup():
        #global user_table_definition, add_user_sql; global connection, cursor
        username=user.get(); password=pw.get(); verify_password=confirm_pw.get()
        
        if username is None:
            messagebox.showerror('Invalid','Username field cannot be blank')
            return

        if password is None or verify_password is None:
            messagebox.showerror('Invalid','Password field(s) cannot be blank') 
        
        if verify_password is None:
            messagebox.showerror
            
        elif password != verify_password:
            messagebox.showerror('Invalid','Passwords do not match')
        
        path_db_file = os.path.join(db_path, "Accounts.db")
        db_conn = sqlite3.connect(path_db_file)
        cursor_user = db_conn.cursor()
        cursor_user.execute("SELECT * FROM Users WHERE username=?", (username,))
        existing_user = cursor_user.fetchone()

        if existing_user is not None:
            messagebox.showerror('Error','Username already exist')
            return
        
        else:
            salt = uuid.uuid4().hex
            cursor_user.execute("INSERT INTO Users (USERNAME,PASSWORD_HASH,RECORD_ID) VALUES (?,?,?)", (username, encrypt_pw(salt,password),salt))
            db_conn.commit()
            messagebox.showinfo('Success', 'Registration is successful')

        cursor_user.close()
        db_conn.close()

    def encrypt_pw(salt,password):
        encrypt = hashlib.sha512((salt + password).encode("UTF-8")).hexdigest()
        return encrypt
    ##########################################################################################################################################3            
    #   Load vector file (.eps) using PIL
    path_register_logo = os.path.join(resources_path, "register.eps")
    image = Image.open(path_register_logo)

    #   Resize
    new_width, new_height = 300,320                                     # Old values = 398,332
    image = image.resize((new_width,new_height))

    #   Convert .eps file to Tkinter-compatible format
    tk_image = ImageTk.PhotoImage(image=image)

    #   Create label for image
    Label(root, image=tk_image,bg='White').place(x=50,y=50, width=400,height=400)

    #Login box frame (YT)
    frame= Frame(root,width=350, height=350,bg='white')
    frame.place(x=480,y=90)                                                                                     #   Edited y 70 -> 90

    heading=Label(frame,text='Sign Up',fg='#57a1f8',bg='white',font=(font_1,23,'bold'))
    heading.place(x=100,y=5)

        


    def loginX():
        global form_type
        form_type = 1
        root.quit()
    #####################---------------------------------------------------------
    def on_enter(e):
        user.delete(0,'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')

    user = Entry(frame,width=25,fg='black',border=0,bg="White",font=(font_1,11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter) and user.bind('<FocusOut>', on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    #####################---------------------------------------------------------
    def on_enter(e):
        pw.delete(0,'end')

    def on_leave(e):
        name=pw.get()
        if name=='':
            pw.insert(0,'Password')

    pw = Entry(frame,width=25,fg='black',border=0,bg="White",font=(font_1,11))
    pw.place(x=30,y=130)
    pw.insert(0,'Password')
    pw.bind('<FocusIn>', on_enter) and pw.bind('<FocusOut>', on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=157)
    ##############################################################################
    def on_enter(e):
        confirm_pw.delete(0,'end')

    def on_leave(e):
        name=confirm_pw.get()
        if name=='':
            confirm_pw.insert(0,'Confirm Password')

    confirm_pw = Entry(frame,width=25,fg='black',border=0,bg="White",font=(font_1,11))
    confirm_pw.place(x=30,y=180)
    confirm_pw.insert(0,'Confirm Password')
    confirm_pw.bind('<FocusIn>', on_enter) and confirm_pw.bind('<FocusOut>', on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=209) #207-209
    ##############################################################################

    Button(frame,width=39,pady=7,text='Sign Up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=240)                              #   y = 260 -> 230
    label=Label(frame,text="Already have an account?",fg='black',bg='white',font=(font_1,9)).place(x=75,y=300)

    sign_in = Button(frame,width= 6,text='Sign In', border = 0, bg = 'white',cursor ='hand2', fg='#57a1f8', command =loginX).place(x=225,y=300)                 #   x = 215 -> 225 y = 270 -> 300


    # run the window
    root.mainloop()


while True:
    if form_type == 1:
        login()
    elif form_type == 2:
        registration()
    else:
        break

#root.mainloop()