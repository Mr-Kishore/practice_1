from tkinter import *
from datetime import date

root = Tk()
root.geometry("700x500")
root.title("Age Calculator")

photo= PhotoImage(file="luffy1.0.png")
myImage = Label(image=photo)
myImage.grid(row=9, column=1)

def calculateAge():
    today = date.today()
    birthDate = date.today()
    int((monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate - ((today.month, today.day) < (birthDate.month, birthDate.day))
    Label(text = f"{nameValue.get()} your age is {age}").grid(row=5, column=1)
    
    Label(text="NAME").grid(row=1, column=0, padx=90)
    Label(text="YEAR").grid(row=2, colume=0)
    Label(text="MONTH").grid(row=3, column=0)
    Label(text="DAY").grid(row=4, column=0)
    nameValue = Stringvar()
    yearValue = Stringvar()
    monthValue = Stringvar()
    dayValue = Srtingvar()
    nameEntry = Entry(root, textvariable=nameValue)
    yearEntry = Entry(root, textvariable=yearValue)  
    monthEntry = Entry(root, textvatiable=monthValue)
    dayEntry = Entry(root, textvariable=dayValue)
    nameEntry.grid(row=1, column=1, pady=10)
    yearEntry.grid(row=2, column=1, pady=10)
    monthEntry.grid(row=3, column=1, pady=10)
    dayEntry.grid(row=4, column=1, pady=10)
    Button(text = "calculate age", command=calculateAge).grid(row=5, column=1, pady=10)
    
    root.mainloop()
    