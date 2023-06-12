from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import ast; import sqlite3; import hashlib; import uuid

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
global_path     = 'C:/Users/Justyn Lim/Desktop/Python/tkinter/'
global_path2    = 'C:/Users/Justyn INTI/Desktop/Python/Tkinter/'
global_path3    = 'C:/Users/jayvonoon/Desktop/Python/Tkinter-ALL-project-main/'
#global_path4   = 

### Button config ###
button_mode = True
button_on = PhotoImage(file=global_path3+"resources/light_mode.png")
button_off = PhotoImage(file=global_path3+"resources/dark_mode.png")
"""button_on_image = Image.open(button_on); button_off_image = Image.open(button_off)        #Test
    resized_button_on_image = button_on_image.resize((109, 44)); resized_button_off_image = button_off_image.resize((109, 44))
    new_button_on_image = ImageTk.PhotoImage(resized_button_on_image); new_button_off_image = ImageTk.PhotoImage(resized_button_off_image) """


# Global variable declarations
user_table_definition = """
CREATE TABLE Users (USERNAME TEXT, PASSWORD_HASH TEXT,RECORD_ID TEXT)"""

# Connect to db. Create entity

connection = sqlite3.connect(global_path3+'db/accounts.db') # sqlite3.connect(global_path+DB_NAME)                                                                 #   Insert global path
cursor_master = connection.cursor()
cursor_master.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Users'")
if cursor_master.fetchone() is None:
    cursor = connection.cursor()
    cursor.execute(user_table_definition)
    connection.commit()
    cursor.close()

cursor_master.close(); connection.close()


def login():

    def signin():
        username=user.get(); password=pw.get()

#   Login auth (version 1)
        if username is None or password is None:
            display_status(0)
        else:
            db_conn = sqlite3.connect(global_path3+'db/accounts.db')
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
    image = Image.open (global_path3+'resources/login.eps')                       

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


    def system_theme():
        global button_mode

        if button_mode:
            #messagebox.showerror('Dark',"Dark Mode")
            toggle_mode.config(image = button_off,bg = '#26242f',activebackground = "#26242f")
            root.config(bg = "#26242f"); frame.config(bg = "#26242f")
            button_mode = False

        else:
            #messagebox.showerror('Light',"Light Mode")
            toggle_mode.config(image = button_on, bg = "white", activebackground = "white")
            root.config(bg="white"); frame.config(bg = "white")
            button_mode = True
        

    ### ### root.bind('<Return>',(lambda e, sign_in_button=sign_in_button: sign_in_button.invoke()))
    #####################---------------------------------------------------------
    def on_enter(e):
        user.delete(0,'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')

    user = Entry(frame,width=25,fg='black',border=0,bg="White",font=(font_1,11)) # Cannot use: .place(x=30,y=80),causes error
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter) and user.bind('<FocusOut>', on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107) #25,107
    #####################---------------------------------------------------------
    def on_enter(e):
        pw.delete(0,'end')

    def on_leave(e):
        name=pw.get()
        if name=='':
            pw.insert(0,'Password')


    pw = Entry(frame,width=25,fg='black',border=0,bg="White",font=(font_1,11)) # Cannot use: .place(x=30,y=150)
    pw.place(x=30,y=150)
    pw.insert(0,'Password')
    pw.bind('<FocusIn>', on_enter) and pw.bind('<FocusOut>', on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)  #Frame(frame,width=295,height=2,bg='black',placeholder_text = 'Test').place(x=25,y=177)
    ##############################################################################

    sign_in_button=Button(frame,width=39,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0,command=signin ).place(x=35,y=240)
    label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=(font_1,9)).place(x=75,y=300)

    sign_up = Button(frame,width= 6,text='Sign up', border = 0, bg = 'white',cursor ='hand2', fg='#57a1f8', command = registration).place(x=225,y=300)

    toggle_mode = Button(root, width=173,height = 69, pady=7, image = button_on, bd=0, bg = "white", command = system_theme)
    toggle_mode.place(x=752,y=431)

    login_status = Label(frame,text="",fg='white',bg='white')     
    login_status.place(x=75,y=330)

    # run the window
    root.mainloop()



def registration():
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
        
        db_conn = sqlite3.connect(global_path3+'db/accounts.db')
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
    image = Image.open(global_path3+'resources/register.eps')

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

    sign_in = Button(frame,width= 6,text='Sign In', border = 0, bg = 'white',cursor ='hand2', fg='#57a1f8', command =login).place(x=225,y=300)                 #   x = 215 -> 225 y = 270 -> 300

    # run the window
    root.mainloop()

login()
registration()
root.mainloop()