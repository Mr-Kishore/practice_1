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
    result_label.config(text=f"{name}, your age is {age}")

def clearData():
    nameValue.set("")
    yearValue.set("")
    monthValue.set("")
    dayValue.set("")
    result_label.config(text="")

def saveData():
    name = nameValue.get()
    year = yearValue.get()
    month = monthValue.get()
    day = dayValue.get()
    with open("saved_data.txt", "a") as file:
        file.write(f"Name: {name}, Date of Birth: {year}-{month}-{day}\n")

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

calculate_button = Button(text="Calculate Age", command=calculateAge)
calculate_button.grid(row=5, column=1, pady=10)

result_label = Label(root, text="")
result_label.grid(row=6, column=1)

clear_button = Button(text="Clear Data", command=clearData)
clear_button.grid(row=7, column=0, pady=10)

save_button = Button(text="Save Data", command=saveData)
save_button.grid(row=7, column=1, pady=10)

root.mainloop()
