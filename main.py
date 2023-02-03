import tkinter
from tkinter import ttk
from tkinter import messagebox

def print_data():

    accepted = acceptVar.get()

    if accepted == "Accepted":
        first_name = firstNameEntry.get()
        last_name = lastNameEntry.get()
        age = ageSpinbox.get()
        continent = continentCombobox.get()
        phone_number = phoneNumberEntry.get()

        city = cityEntry.get()
        postcode = postcodeEntry.get()
        street_name = streetNameEntry.get()
        house_number = houseNumberSpinbox.get()
        county = countyEntry.get()

        print("First Name:", first_name, "Last Name:", last_name, "Age:")
        print("Continent:", continent, "Phone Number:", phone_number)

        print("Town/city:", city, "\nHouse Number:", house_number, "Street Name:", street_name)
        print("Post Code:", postcode, "\nCounty:", county, "\n\n")

    else:
        tkinter.messagebox.showwarning(title="Error", message="Please accept the terms and conditions")


window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# User Info Frame

userInfoFrame = tkinter.LabelFrame(frame, text="User Information")
userInfoFrame.grid(row=0, column=0, padx=15, pady=15)

# Row 0-1, Column 0-2

firstNameLabel = tkinter.Label(userInfoFrame, text="First Name")
lastNameLabel = tkinter.Label(userInfoFrame, text="Last Name")

firstNameLabel.grid(row=0, column=0, padx=15, pady=5)
lastNameLabel.grid(row=0, column=1, padx=15, pady=5)

firstNameEntry = tkinter.Entry(userInfoFrame)
lastNameEntry  = tkinter.Entry(userInfoFrame)

firstNameEntry.grid(row=1, column=0, padx=15, pady=5)
lastNameEntry.grid(row=1, column=1, padx=15, pady=5)

ageLabel = tkinter.Label(userInfoFrame,text="Age")
ageSpinbox = tkinter.Spinbox(userInfoFrame, from_=18, to=115)

ageLabel.grid(row=0, column=2, padx=15, pady=5)
ageSpinbox.grid(row=1, column=2, padx=15, pady=5)

# Rows 2-3, Columns 0-1

continentLabel = tkinter.Label(userInfoFrame, text="Continent")
continentCombobox = ttk.Combobox(userInfoFrame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])

continentLabel.grid(row=2, column=1, padx=15, pady=5)
continentCombobox.grid(row=3, column=1, padx=15, pady=5)

phoneNumberLabel = tkinter.Label(userInfoFrame, text="Phone Number")
phoneNumberEntry = tkinter.Entry(userInfoFrame)

phoneNumberLabel.grid(row=2, column=0, padx=15, pady=5)
phoneNumberEntry.grid(row=3,column=0, padx=15, pady=5)

# Address Frame

addressFrame = tkinter.LabelFrame(frame, text="Address")
addressFrame.grid(row=1, column=0, padx=15, pady=15, sticky="news")

# Rows 0-1, Columns 0-2

cityLabel = tkinter.Label(addressFrame, text="Town/City")
cityEntry = tkinter.Entry(addressFrame)

cityLabel.grid(row=0, column=0, padx=15, pady=5)
cityEntry.grid(row=1, column=0, padx=15, pady=5)

postcodeLabel = tkinter.Label(addressFrame, text="Post Code")
postcodeEntry = tkinter.Entry(addressFrame)

postcodeLabel.grid(row=0, column=1, padx=15, pady=5)
postcodeEntry.grid(row=1, column=1, padx=15, pady=5)

houseNumberLabel = tkinter.Label(addressFrame, text="House Number")
houseNumberSpinbox = tkinter.Spinbox(addressFrame, from_=0, to="infinity")

houseNumberLabel.grid(row=0, column=2, padx=15, pady=5)
houseNumberSpinbox.grid(row=1, column=2, padx=15, pady=5)

# Rows 2-3, Column 0-1

streetNameLabel = tkinter.Label(addressFrame, text="Street Name")
streetNameEntry = tkinter.Entry(addressFrame)

streetNameLabel.grid(row=2, column=0, padx=15, pady=5)
streetNameEntry.grid(row=3, column=0, padx=15, pady=5)

countyLabel = tkinter.Label(addressFrame, text="County")
countyEntry = tkinter.Entry(addressFrame)

countyLabel.grid(row=2, column=1, padx=15, pady=5)
countyEntry.grid(row=3, column=1, padx=15, pady=5)

# Terms and conditions frame

termsConditionsFrame = tkinter.LabelFrame(frame)
termsConditionsFrame.grid(row=2,column=0, sticky="news", padx=15, pady=15)

acceptVar = tkinter.StringVar(value= "Not Accepted")
termsCheck = tkinter.Checkbutton(termsConditionsFrame,text="I accept the terms and conditions", variable=acceptVar, onvalue="Accepted", offvalue="Not Accepted")

termsCheck.grid(row=0,column=0)

button = tkinter.Button(frame,text="Enter", command=print_data)
button.grid(row=3,column=0,sticky="news",padx = 15,pady=15)

window.mainloop()