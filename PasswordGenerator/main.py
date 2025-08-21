from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def GeneratPassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
  
    PassWordLetter =[random.choice(letters) for _ in range( random.randint(8, 10))]
    PassWordSymbol =[random.choice(symbols) for _ in  range(random.randint(2, 4))]
    PassWordNumber =[random.choice(numbers) for _ in  range(random.randint(2, 4))]
    
    password_list = PassWordLetter+PassWordSymbol+PassWordNumber
    random.shuffle(password_list)
    password = "".join(password_list)
    # print(password)
    AlreadyPassword = PasswordEntry.get()
    if len(AlreadyPassword)>0:
        PasswordEntry.delete(0,END)
    PasswordEntry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def AddInfo():
    Email = EmailEntry.get()
    PassWord = PasswordEntry.get()
    Website = WesbsiteEntry.get()
    NewData={
               Website:{
                        "email":Email,
                        "password":PassWord
                    }
             }
    
    if len(Website)==0 or len(PassWord)==0:
        messagebox.showinfo(title="OOPS",message="Some fields are not filled")
    else:  
        try:
             with open("data.json","r") as data_file:
                    data = json.load(data_file)
                    data.update(NewData)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(NewData,data_file,indent=4)
        else:   
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
             WesbsiteEntry.delete(0,END)
             PasswordEntry.delete(0,END)
       
def SearchPassword():
    Website = WesbsiteEntry.get()
    try:
        with open("data.json" ,"r")as data_file:
            data = json.load(data_file)
            Email = data[Website]["email"]
            Password = data[Website]["password"]
            messagebox.showinfo(title=Website,message=(f"Your email is :{Email}\n Password :{Password}"))
    except :
        messagebox.showinfo(title=Website,message=("Website not found"))
        



# ---------------------------- UI SETUP ------------------------------- #

Window = Tk()
Window.config(padx=50,pady=50)
Window.title("Password Manager")

canvas = Canvas(height=200,width=200)

LogoImg = PhotoImage(file = "logo.png")
canvas.create_image(100,100 ,image=LogoImg)
canvas.grid(column=1,row=0)

EmailLable = Label(text="Website")
EmailLable.grid(column=0,row=1)

NameLable =  Label(text="Email/Username :")
NameLable.grid(column=0,row=2)

PasswordLable =  Label(text="Password")
PasswordLable.grid(column=0,row=3)


WesbsiteEntry = Entry(width=38)
WesbsiteEntry.grid(column=1,row=1)
WesbsiteEntry.focus()

EmailEntry = Entry(width=55)
EmailEntry.grid(column=1,row=2,columnspan=2)
EmailEntry.insert(0,"xyz@gmail.com")


PasswordEntry = Entry(width=38)
PasswordEntry.grid(column=1,row=3)

GeneratorBtn = Button(text="Generate Password",command=GeneratPassword)
GeneratorBtn.grid(column=2,row=3,columnspan=2)


SearchBtn = Button(text="search",width=14,command=SearchPassword)
SearchBtn.grid(column=2,row=1,columnspan=2)

AddBtn = Button(text="Add" ,width=50, command=AddInfo)
AddBtn.grid(column=1,row=4 ,columnspan=2) 

Window.mainloop()
