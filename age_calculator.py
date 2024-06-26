from tkinter import *
from datetime import date

root = Tk()
root.geometry("700x500")
root.title("Age Calculator")

def calculateAge():
    today = date.today()
    name = nameValue.get()
    birthDate = date(int(yearValue.get()), int(monthValue.get()), int(dayValue.get()))
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    Label(text=f"{name} your age is {age}").grid(row=6, column=1)

Label(text="NAME").grid(row=1, column=0, padx=90)
Label(text="YEAR").grid(row=2, column=0)
Label(text="MONTH").grid(row=3, column=0)
Label(text="DAY").grid(row=4, column=0)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue)
yearEntry = Entry(root, textvariable=yearValue)
monthEntry = Entry(root, textvariable=monthValue)
dayEntry = Entry(root, textvariable=dayValue)

nameEntry.grid(row=1, column=1, pady=10)
yearEntry.grid(row=2, column=1, pady=10)
monthEntry.grid(row=3, column=1, pady=10)
dayEntry.grid(row=4, column=1, pady=10)

Button(text="Calculate Age", command=calculateAge).grid(row=5, column=1, pady=10)

root.mainloop()
