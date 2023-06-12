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
font_1 = 'Microsoft YaHei UI Light'
global_path = 'C:/Users/Justyn Lim/Desktop/Python/tkinter/'
global_path2 = 'C:/Users/Justyn INTI/Desktop/Python/Tkinter/'
global_path3 = 'C:/Users/jayvonoon/Desktop/Python/Tkinter-ALL-project-main/'
#global_path4 = 

#############################################- OPTIONS FOR REGISTRATION-################################################################

###################### TRIAL ########################################
"""def signup():
    username=user.get(); password=pw.get(); verify_password=confirm_pw.get()
    
    if not username or not password or not verify_password:
    #if username!='' and password!=''and verify_password==password :
    #if username=='' 
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen,text='Registration successful', bg='#fff', font=('Calibri(Body)',50,'bold')).pack(expand=True)

        screen.mainloop()
    
    elif username==''or password==''or verify_password=='':
        messagebox.showerror("Error","Field(s) cannot be blank")
    
    elif verify_password!=password:
        messagebox.showerror("Invalid","Passwords do not match")
"""  

#####################################################################

#def register():

"""def signup():
    username=user.get(); password=pw.get(); verify_password=confirm_pw.get()
    
    if not username or not password or not verify_password:
    #if username!='' and password!=''and verify_password==password :
    #if username=='' 
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen,text='Registration successful', bg='#fff', font=('Calibri(Body)',50,'bold')).pack(expand=True)

        screen.mainloop()
    
    elif username==''or password==''or verify_password=='':
        messagebox.showerror("Error","Field(s) cannot be blank")
    
    elif verify_password!=password:
        messagebox.showerror("Invalid","Passwords do not match")
"""
# Global variable declarations
user_table_definition = """
CREATE TABLE Users (USERNAME TEXT, PASSWORD_HASH TEXT,RECORD_ID TEXT)"""

# Connect to db. Create entity

connection = sqlite3.connect(global_path+'db/accounts.db')
cursor_master = connection.cursor()
cursor_master.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Users'")
if cursor_master.fetchone() is None:
    cursor = connection.cursor()
    cursor.execute(user_table_definition)
    connection.commit()
    cursor.close()

cursor_master.close(); connection.close()





#add_user_sql = "INSERT INTO Users VALUES ('{}','{}')"
##########-PARVAT-######################
def signup():
    #global user_table_definition, add_user_sql; global connection, cursor
    username=user.get(); password=pw.get(); verify_password=confirm_pw.get()
    
    if username is None:
        messagebox.showerror('Invalid','Username field cannot be blank')
        return 
        
    if password != verify_password:
        messagebox.showerror('Invalid','Passwords do not match')
    
    db_conn = sqlite3.connect(global_path+'db/accounts.db')
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


    
        
        
        
        
"""        try:
            # Connect to db. Create entity
            connection = sqlite3.connect(global_path+'db/accounts.db')
            cursor = connection.cursor()
            cursor.execute(user_table_definition)

            # Generate unique salt and hash password
            salt = uuid.uuid4().hex
            encrypt = hashlib.sha512((salt + password).encode("UTF-8")).hexdigest()

            # Insert user into db
            cursor.execute(add_user_sql.format(username, salt, encrypt))
            connection.commit

            messagebox.showinfo('Success', 'Registration is successful')
        
        except Exception as e:
            print("Error:", e)
            connection.rollback()
            messagebox.showerror('Invalid','Passwords do not match')

    

    if password == verify_password:
        try:                                    #if file is available, reads file and enters data
            file = open('C:/Users/Justyn Lim/Desktop/Python/tkinter/accounts.db','r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open('C:/Users/Justyn Lim/Desktop/Python/tkinter/accounts.db','w')
            w = file.write(str(r))

            messagebox.showinfo('Signup','Successfull sign up')

        except:
            file = open('C:/Users/Justyn Lim/Desktop/Python/tkinter/accounts.db','w')
            pp = str({'Username':'Password'})
            file.write(pp)
            file.close()
        
    else:
        messagebox.showerror('Invalid',"Passwords do not match")
"""







##########################################################################################################################################3            
#   Load the EPS file using PIL
image = Image.open(global_path+'resources/register.eps')


#   Resize
new_width, new_height = 300,320 #398,332
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

sign_in = Button(frame,width= 6,text='Sign In', border = 0, bg = 'white',cursor ='hand2', fg='#57a1f8',).place(x=225,y=300)                 #   x = 215 -> 225 y = 270 -> 300

# run the window
root.mainloop()