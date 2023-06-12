def login():
        
        def signin():
             username=user.get(); password=pw.get()

#   Login auth (version 1)
        if username is None or password is None:
            label = Label(frame,text="Invalid username/password",fg='red',bg='white').place(x=75,y=380)
        else:
            db_conn = sqlite3.connect(global_path+'db/accounts.db')
            cursor_user = db_conn.cursor()
            cursor_user.execute("SELECT username,password_hash,record_id FROM Users WHERE username=?", (username,))
            row = cursor_user.fetchone()
        
        if row is not None:
            salt_db = row[2]
            password_hash_db = row[1]
            password_hash = encrypt_pw(salt_db,password)
            if password_hash_db != password_hash:
                label = Label(frame,text="Invalid username/password",fg='red',bg='white').place(x=75,y=380)
            else:
                screen=Toplevel(root)
                screen.title("App")
                screen.geometry('925x500+300+200')
                screen.config=(bg='white')
                Label(screen,text='PASSED', bg='#fff', font=('Calibri(Body)',50,'bold')).pack(expand=True)
                screen.mainloop()

        else:
            label = Label(frame,text="Invalid username/password",fg='red',bg='white').pack


#########################-Prototype for login-###########################################

#   need to edit signin func
        if username=='admin' and password=='admin':
            #print('Yamahahaha') *to verify auth works
            screen=Toplevel(root)
            screen.title("App")
            screen.geometry('925x500+300+200')
            screen.config(bg='white')

            Label(screen,text='zao shang hao zhong guo', bg='#fff', font=('Calibri(Body)',50,'bold')).pack(expand=True)

            screen.mainloop()
        
        elif username!='admin' and password !='admin' or username!='admin' or password!='admin':
            messagebox.showerror("Invalid","Invalid Username/Password")


