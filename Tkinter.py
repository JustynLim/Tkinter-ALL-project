from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import ast

# create a Tkinter window
root = Tk()

#################---TRIAL (Removing window title)---##################

root.title("")
root.attributes('-topmost', False),('-alpha', 0.8),('-toolwindow', True),('-style', 'dialog')

######################################################################

# set the window title
#root.title('Login')

# set the window size
win_width = 925; win_height = 500                       #   remove semicolon if required
root.geometry(f'{win_width}x{win_height}+300+200')
root.configure(bg="#fff")
root.resizable(FALSE,FALSE)

### Font List ###
font_1 = 'Microsoft YaHei UI Light'


def signin():
    username=user.get(); password=pw.get()
    #password=pw.get()

    if username=='admin' and password=='admin':
        #print('Yamahahaha') *to verify auth works
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen,text='zao shang hao zhong guo', bg='#fff', font=('Calibri(Body)',50,'bold')).pack(expand=True)

        screen.mainloop()

    elif username!='admin' and password!='admin'or username!='admin'or password!='admin':
        messagebox.showerror("Invalid","Invalid Username/Password")
"""
    elif username!='admin':
        messagebox.showerror("Invalid","Invalid Username/Password")

    elif password!='admin':
        messagebox.showerror("Invalid","Invalid Username/Password")
"""
###################### TRIAL ########################################
def signup():
    username=user.get(); password=pw.get(); verify_password=password()
    
    if username=='' and password==''and verify_password==password :
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen,text='Registration successful', bg='#fff', font=('Calibri(Body)',50,'bold')).pack(expand=True)

        screen.mainloop()  
#####################################################################
#                                                                                           #Parvat version =PV
#   Load the EPS file using PIL                                                               # load the image
image = Image.open('C:/Users/Justyn Lim/Desktop/Python/vectorimg.eps')                        #image = PhotoImage(file='C:/Users/Justyn Lim/Desktop/Python/login.png')

#   Resize
new_width, new_height = 398,332
image = image.resize((new_width,new_height))

#   Convert .eps file to Tkinter-compatible format                                 
tk_image = ImageTk.PhotoImage(image=image)                                                  #file='C:/Users/Justyn Lim/Desktop/Python/vectorimg.eps'

#                                                                                           #PV
#   Create label for image                                                                    # create a label for the image
Label(root, image=tk_image,bg='White').place(x=50,y=50, width=400,height=400)                 # Label(root, image=image,bg='White').place(x=50,y=50)


#Login box frame (YT)
frame= Frame(root,width=350, height=350,bg='white')                                         #Don't '.place' here, shifts frame to the other side
frame.place(x=480,y=90)                                                                     #edited 70 -> 90

heading=Label(frame,text='Sign In',fg='#57a1f8',bg='white',font=(font_1,23,'bold'))
heading.place(x=100,y=5)

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
user.bind('<FocusIn>', on_enter) and ('<FocusOut>', on_leave)
#user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
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
#pw.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
##############################################################################

Button(frame,width=39,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0,command=signin ).place(x=35,y=240)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=(font_1,9)).place(x=75,y=300)
###label.place(x=75,y=270)

sign_up = Button(frame,width= 6,text='Sign up', border = 0, bg = 'white',cursor ='hand2', fg='#57a1f8',).place(x=225,y=300)
###sign_up.place(x=215,y=270)
"""""
# create a label for the username
username_label = Label(root, text="Username:")
username_label.pack()
username_label.place(x=520,y=180) #remove if unnecessary

# create an entry for the username
username_entry = Entry(root)
username_entry.pack()

# create a label for the password
password_label = Label(root, text="Password:")
password_label.pack()

# create an entry for the password
password_entry = Entry(root, show="*")
password_entry.pack()

# create a function to verify the credentials
def verify_credentials():
    # get the username and password from the entries
    username = username_entry.get()
    password = password_entry.get()
    
    # check if the credentials are valid
    if (username in str(username_entry) and password in str(password_entry)) == True:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Username/Password is invalid. Please try again.")

# create a button to submit the credentials
submit_button = Button(root, text="Login", command=verify_credentials)
submit_button.pack(pady=10)

# create a function to open the registration window
def open_registration_window():
    # create a new window for registration
    registration_window = Toplevel(root)
    registration_window.title("Registration Form")
    registration_window.geometry("400x400")
    
    # create a label for the username
    username_label = Label(registration_window, text="Username:")
    username_label.pack()

    # create an entry for the username
    username_entry = Entry(registration_window)
    username_entry.pack()

    # create a label for the password
    password_label = Label(registration_window, text="Password:")
    password_label.pack()

    # create an entry for the password
    password_entry = Entry(registration_window, show="*")
    password_entry.pack()

    # create a label for the confirm password
    confirm_password_label = Label(registration_window, text="Confirm Password:")
    confirm_password_label.pack()

    # create an entry for the confirm password
    confirm_password_entry = Entry(registration_window, show="*")
    confirm_password_entry.pack()

    # create a button to submit the registration form
    def submit_registration():
        # get the values from the entries
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        
        # check if the passwords match
        if password == confirm_password:
            messagebox.showinfo("Success", "Registration successful!")
            registration_window.destroy()
        else:
            messagebox.showerror("Error", "Passwords do not match. Please try again.")
    
    submit_button = Button(registration_window, text="Register", command=submit_registration)
    submit_button.pack(pady=10)

# create a button to open the registration window
registration_button = Button(root, text="Register", command=open_registration_window)
registration_button.pack(pady=10)
"""
# run the window
root.mainloop()
