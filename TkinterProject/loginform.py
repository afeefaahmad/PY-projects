import sqlite3
import tkinter as tk
from tkinter import ttk,messagebox
 
conn = sqlite3.connect('user_data.db')
 
c=conn.cursor()
 
c.execute('''CREATE TABLE IF NOT EXISTS users(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          email TEXT,
          phone TEXT,
          password TEXT)''')
 
conn.commit()
 
def add_user():
    email=email_entry.get()
    phone = Phone_entry.get()
    password=password_entry.get()
 
    if email and phone and password:
        c.execute("INSERT INTO users(email, phone, password) VALUES(?,?,?)",(email, phone, password))
        conn.commit()
        messagebox.showinfo("Success","User added successfully!")
        view_user()
    else:
        messagebox.showwarning("Input Error", "All fields are required!")
        clear_enteries()
 
def view_user():
    for row in tree.get_children():
        tree.delete(row)
 
    c.execute("SELECT * FROM users")
 
    rows=c.fetchall()
 
    for row in rows:
        tree.insert("",tk.END,values=row)
 
def edit_user():
    user_id=user_id_entry.get()
    email=email_entry.get()
    phone = Phone_entry.get()
    password=password_entry.get()
 
    if user_id and email and phone and password:
        c.execute("UPADTE users SET email=?, phone=?, password=? WHERE id =?",(email,phone, password,user_id))
        conn.commit()
        messagebox.showinfo("Success","User updated successfully!")
        view_user()
    else:
        messagebox.showwarning("Input Error", "All fields are required!")
        clear_enteries()
 
def delete_user():
    user_id=user_id_entry.get()
    if user_id:
        c.execute("DELETE FROM users WHERE id = ?",(user_id))
        conn.commit()
        messagebox.showinfo("Success","User deleted successfully!")
        view_user()
    else:
        messagebox.showwarning("Input Error", "All fields are required!")
        clear_enteries()
 
def clear_enteries():
    user_id_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    Phone_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)
 
 
root = tk.Tk()
root.title("User Registration Form")
root.geometry("400x500")
root.configure(bg='#ffcc66')
 
frame=tk.Frame(root,bg="white",padx=20,pady=20)
frame.pack(pady=10)
 
tk.Label(frame, text="User ID (for edit/delete)",font=("Arial",10,"bold"),bg="white").grid(row=0,column=0,sticky="w")
user_id_entry=tk.Entry(frame,width=30,relief="sunken")
user_id_entry.grid(row=1,column=0,columnspan=2,pady=5)
 
 
tk.Label(frame, text="Email",font=("Arial",10,"bold"),bg="white").grid(row=2,column=0,sticky="w")
email_entry=tk.Entry(frame,width=30,relief="sunken")
email_entry.grid(row=3,column=0,columnspan=2,pady=5)
 
 
tk.Label(frame, text="Phone",font=("Arial",10,"bold"),bg="white").grid(row=4,column=0,sticky="w") #w- left, e - right, s - bottom, n- top
Phone_entry=tk.Entry(frame,width=30,relief="sunken")
Phone_entry.grid(row=5,column=0,columnspan=2,pady=5)
 
 
tk.Label(frame, text="Password",font=("Arial",10,"bold"),bg="white").grid(row=6,column=0,sticky="w")
password_entry=tk.Entry(frame,width=30,relief="sunken")
password_entry.grid(row=7,column=0,columnspan=2,pady=5)
 
tk.Button(frame, text="Add",bg="green",fg="white",font=("Arial",12,"bold"),command=add_user).grid(row=8,column=0,pady=10)
tk.Button(frame, text="View",bg="blue",fg="black",font=("Arial",12,"bold"),command=view_user).grid(row=8,column=1,pady=10)
tk.Button(frame, text="Edit",bg="orange",fg="white",font=("Arial",12,"bold"),command=edit_user).grid(row=9,column=0,pady=10)
tk.Button(frame, text="Delete",bg="red",fg="white",font=("Arial",12,"bold"),command=delete_user).grid(row=9,column=1,pady=10)
 
 
columns=('ID','Email','Phone','Password')
tree=ttk.Treeview(root,columns=columns,show='headings')
tree.heading('Email',text='Email')
tree.heading('Phone',text='Phone')
tree.heading('Password',text='Password')
 
tree.pack(pady=20)
 
 
view_user()
 
root.mainloop()
 
conn.close()
