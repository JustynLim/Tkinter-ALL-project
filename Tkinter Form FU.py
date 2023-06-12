from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import ast; import sqlite3; import hashlib; import uuid; import os

# create a Tkinter window
root = Tk()

#################---(Removing window title)---##################
root.title("")
root.attributes('-topmost', False),('-alpha', 0.8),('-toolwindow', True),('-style', 'dialog')

# Set the window size
win_width = 925; win_height = 500
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
username_input1         = '' 
username_input2         = ''
password_input1         = ''
password_input2         = ''
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
    global password_button1_mode
    password_button1_mode = True
    
    global form_type
    form_type = 0

    def signin():
        global username_input1; global password_input1
        on_leave_username(None); on_leave_password(None)
        username = username_input1; password = password_input1

#   Login auth (version 1)
        if username is None or password is None:
            display_status(0)
            print("Hello1")
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
                print("Hello2")

            else:
                global form_type
                form_type = 3
                root.quit()

        else:
            display_status(0)
        print("Hello3")
        pw.focus_set()
        if pw.get() == " Password":
            pw.delete(0,'end')
            password_input1 = ''

    def encrypt_pw(salt,password):
        encrypt = hashlib.sha512((salt + password).encode("UTF-8")).hexdigest()
        return encrypt
    
    def display_status(status):
        if status == 0:
            login_status.config(text="Invalid username/password",fg='red',bg='white')
            
        else:
            login_status.config(text="Login successful", fg='green', bg='white')


#####################################################################
    #   Load the vector file (.eps) using PIL
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
            password_button1_mode = False

        else:
            password_toggle_mode.config(image = hide_password_button)
            password_button1_mode = True

        password_mode()

##########- Shows/Hide password -##########
    def password_mode():
        password = pw.get()
        print("password_mode() ->Leave password")
        print(password)
        if password != '' and password != ' Password':
            global password_input1
            password_input1 = password
        
        else:
            password_input1 = ''         

        if password_input1 == '':
            pw.config(show = '')
            pw.delete(0,'end')
            pw.insert(0,' Password')
        
        elif password_button1_mode:
            pw.config(show = '')
            
        else:
            pw.config(show = '*')            
###########################################
    def registrationX():
        global form_type
        form_type = 2
        root.quit()

###########################################
    def on_enter_username(e):
        if  username_input1 == '':
            user.delete(0,'end')

    def on_leave_username(e):
        name = user.get()
        print("On leave user")
        if name == '':
            global username_input1
            user.insert(0,' Username')
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
       if  password_input1 == ''or pw.get() == ' Password':
        pw.delete(0,'end')
        
        if password_button1_mode:                
            pw.config(show = '')
        
        else:
            pw.config(show = '*')        

    def on_leave_password(e):
        password_mode()

    pw = Entry(frame,width=25,fg='black',border=0,bg="White",font=(font_1,11)) # Cannot use: .place(x=30,y=150)
    pw.place(x=30,y=150)
    pw.bind('<FocusIn>', on_enter_password) and pw.bind('<FocusOut>', on_leave_password)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    ##############################################################################

    sign_in_button=Button(frame,width=39,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0,command=signin ).place(x=35,y=240)
    label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=(font_1,9)).place(x=75,y=300)

    sign_up = Button(frame,width= 6,text='Sign up', border = 0, bg = 'white',cursor ='hand2', fg='#57a1f8', command = registrationX).place(x=225,y=300)

    password_toggle_mode = Button(root, width=24,height = 24, pady=7, bd = 0, bg = 'white', command = toggle_password)
    password_toggle_mode.place(x=770,y=238)

    login_status = Label(frame,text="",fg='white',bg='white')     
    login_status.place(x=75,y=330)


    toggle_password()                           # Triggers function once, turns to false state

    # run the window
    root.mainloop()


def registration():
    global password_button2_mode; global confirm_password_button_mode
    password_button2_mode = True; confirm_password_button_mode = True
    
    global form_type
    form_type = 0

    def signup():

        global username_input2; global password_input2; global confirm_password_input

        on_leave_username(None); on_leave_password(None); on_leave_confirm_password(None)

        username=username_input2; password=password_input2; verify_password=confirm_password_input
        print (username_input2,password_input2,confirm_password_input)
        
        isError = False
        if username is None or username == '':
            display_status(0)
            isError = True
        

        elif password is None or verify_password is None or password == '' or verify_password == '':
            display_status(1)
            isError = True 
            
        elif password != verify_password:
            display_status(2)
            isError = True
        
        if isError:
            print("isError")
            confirm_pw.focus_set()
            if confirm_pw.get() == " Confirm Password":
                confirm_pw.delete(0,'end')
                confirm_password_input = ''
            return
        
        path_db_file = os.path.join(db_path, "Accounts.db")
        db_conn = sqlite3.connect(path_db_file)
        cursor_user = db_conn.cursor()
        cursor_user.execute("SELECT * FROM Users WHERE username=?", (username,))
        existing_user = cursor_user.fetchone()

        if existing_user is not None:
            display_status(3)
            confirm_pw.focus_set()
            if confirm_pw.get() == " Confirm Password":
                confirm_pw.delete(0,'end')
                confirm_password_input = ''

        
        else:
            salt = uuid.uuid4().hex
            cursor_user.execute("INSERT INTO Users (USERNAME,PASSWORD_HASH,RECORD_ID) VALUES (?,?,?)", (username, encrypt_pw(salt,password),salt))
            db_conn.commit()
            display_status(4)

        cursor_user.close()
        db_conn.close()

    def encrypt_pw(salt,password):
        encrypt = hashlib.sha512((salt + password).encode("UTF-8")).hexdigest()
        return encrypt
    
    def display_status(status):
        if status == 0:
            register_status.config(text="Username field cannot be blank", fg = 'red', bg = 'white')
        elif status == 1:
            register_status.config(text="Password field(s) cannot be blank", fg = 'red', bg = 'white')
        elif status == 2:
            register_status.config(text="Passwords do not match", fg = 'red', bg = 'white')
        elif status == 3:
            register_status.config(text="Username already exist", fg = 'red', bg = 'white')
        elif status == 4:
            register_status.config(text="Successful Registration", fg = 'green', bg = 'white')



    ##########################################################################################################################################3            
    #   Load vector file (.eps) using PIL
    path_register_logo = os.path.join(resources_path, "register.eps")
    image = Image.open(path_register_logo)

    #   Resize
    new_width, new_height = 300,320
    image = image.resize((new_width,new_height))

    #   Convert .eps file to Tkinter-compatible format
    tk_image = ImageTk.PhotoImage(image=image)

    #   Create label for image
    Label(root, image=tk_image,bg='White').place(x=50,y=50, width=400,height=400)

    #Login box frame (PV)
    frame= Frame(root,width=350, height=350,bg='white')
    frame.place(x=480,y=90)

    heading=Label(frame,text='Sign Up',fg='#57a1f8',bg='white',font=(font_1,23,'bold'))
    heading.place(x=100,y=5)

##########- This part handles changing icon and sets global value -##########
    def toggle_password():
        global password_button2_mode

        if password_button2_mode:
            password_toggle_mode.config(image = show_password_button)
            password_button2_mode = False

        else:
            password_toggle_mode.config(image = hide_password_button)
            password_button2_mode = True
            
        password_mode()
        
    def toggle_confirm_password():
        global confirm_password_button_mode

        if confirm_password_button_mode:
            confirm_password_toggle_mode.config(image = show_password_button)
            confirm_password_button_mode = False

        else:
            confirm_password_toggle_mode.config(image = hide_password_button)
            confirm_password_button_mode = True
        
        confirm_password_mode()
###############################################################################
##########- Shows/Hide password -##########
    def password_mode():
        password = pw.get()
        if password != '' and password != ' Password':
            global password_input2
            password_input2 = password
        else:
            password_input2 = ''


        if password_input2 == '':
            pw.config(show = '')
            pw.delete(0,'end')
            pw.insert(0,' Password')
        
        elif password_button2_mode:
            pw.config(show = '')
            
        else:
            pw.config(show = '*')
        
###########################################
    def confirm_password_mode():
        confirm_password = confirm_pw.get()
        if confirm_password != '' and confirm_password != ' Confirm Password':
            global confirm_password_input
            confirm_password_input = confirm_password
        else:
            confirm_password_input = ''


        if confirm_password_input == '':
            confirm_pw.config(show = '')
            confirm_pw.delete(0, 'end')
            confirm_pw.insert(0, ' Confirm Password')

        elif confirm_password_button_mode:
            confirm_pw.config(show = '')

        else:
            confirm_pw.config(show = '*')
###########################################
    def loginX():
        global form_type
        form_type = 1
        root.quit()
###########################################
    def on_enter_username(e):
        if  username_input2 == '':
            user.delete(0,'end')

    def on_leave_username(e):
        name = user.get()
        if name == '':
            global username_input2
            user.insert(0,' Username')
            username_input2 = ''

        elif user.get() == ' Username':
            username_input2 = ''

        else:
            username_input2 = user.get()

    user = Entry(frame,width=25,fg='black',border=0,bg="White",font=(font_1,11))
    user.place(x=30,y=80)
    user.insert(0,' Username')
    user.bind('<FocusIn>', on_enter_username) and user.bind('<FocusOut>', on_leave_username)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
##############################################################################
    def on_enter_password(e):
       if  password_input2 == '' or pw.get() == ' Password':
        pw.delete(0,'end')
        
        if password_button2_mode:                
            pw.config(show = '')
        
        else:
            pw.config(show = '*')        

    def on_leave_password(e): 
        password_mode()

    pw = Entry(frame,width=25,fg='black',border=0,bg="White",font=(font_1,11))
    pw.place(x=30,y=130)
    pw.bind('<FocusIn>', on_enter_password) and pw.bind('<FocusOut>', on_leave_password)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=157)
##############################################################################
    def on_enter_confirm_password(e):
       if  confirm_password_input == '' or pw.get() == ' Confirm Password':
        confirm_pw.delete(0,'end')
        
        if confirm_password_button_mode:                
            confirm_pw.config(show = '')
        
        else:
            confirm_pw.config(show = '*')        

    def on_leave_confirm_password(e):
        confirm_password_mode()

    confirm_pw = Entry(frame,width=25,fg='black',border=0,bg="White",font=(font_1,11))
    confirm_pw.place(x=30,y=180)
    confirm_pw.bind('<FocusIn>', on_enter_confirm_password) and confirm_pw.bind('<FocusOut>', on_leave_confirm_password)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=209)
##############################################################################

    sign_up_button=Button(frame,width=39,pady=7,text='Sign Up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=240)
    label=Label(frame,text="Already have an account?",fg='black',bg='white',font=(font_1,9)).place(x=75,y=300)

    sign_in = Button(frame,width= 6,text='Sign In', border = 0, bg = 'white',cursor ='hand2', fg='#57a1f8', command =loginX).place(x=225,y=300)

    password_toggle_mode = Button(root, width=24,height = 24, pady=7, bd = 0, bg = 'white', command = toggle_password)
    password_toggle_mode.place(x=770,y=220)
    
    confirm_password_toggle_mode = Button(root, width=24,height = 24, pady=7, bd = 0, bg = 'white', command = toggle_confirm_password)
    confirm_password_toggle_mode.place(x=770,y=270)

    register_status = Label(frame, text = "",fg = 'white',bg = 'white')
    register_status.place(x=75,y=330)


    toggle_password()
    toggle_confirm_password()

    # run the window
    root.mainloop()


while True:
    if form_type == 1:
        login()
    elif form_type == 2:
        registration()
    elif form_type == 3:
        form_type = 999
        print("Call ext lib")
        # Application_function_name()  / load_tasks()
    else:
        break

#root.mainloop()