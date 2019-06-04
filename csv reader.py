#https://www.tutorialspoint.com/python/python_gui_programming.htm

import csv

dolphins = []

with open('dolphins.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        dolphins.append(row)
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        line_count += 1
    print(f'Processed {line_count} lines, {line_count-1} of which are entries.')

print(" ")

#Displays all column information based on row input 
def getrecord(x):
    return("Common Name: " + dolphins[x-1]["Common name"] + "\nScientific Name: " + dolphins[x-1]["Scientific name"]
            + "\nLatitude: " + dolphins[x-1]["Latitude"] + "\nLongitude: " + dolphins[x-1]["Longitude"] + "\nTotal Individuals: "
            + dolphins[x-1]["Total individuals"] + "\nYear Observed: " + dolphins[x-1]["Year observed"]) 

print(getrecord(4))

print(" ")

#Calculates how many total dolphins in the csv record
def individuals():
    total = 0
    for x in dolphins:
        total += int(x["Total individuals"])
    return("There are " + str(total) + " total dolphin sightings")

print(individuals())

print(" ")

#Calculates how many total dolphins based on dolphin type
def individuals_type(x):
    total = 0
    for y in dolphins:
        if y["Common name"] == x:
            total += int(y["Total individuals"])
    return("There are " + str(total) + " total dolphin sightings of the " + x)

print(individuals_type("Bottlenose dolphin - Common"))

print(" ")

#Calculates how many total dolphins based on year observed
def individuals_year(x):
    total = 0
    for y in dolphins:
        if y["Year observed"] == str(x):
            total += int(y["Total individuals"])
    return("There were " + str(total) + " dolphins sighted in " + str(x))

print(individuals_year(1899))

print(" ")

#returns a list of all the different common names
def common_names_list():
    names = []
    for x in dolphins:
        if x["Common name"] not in names:
            names.append(x["Common name"])
    return names

common_names_list()

print(" ")

#Prints a list of all the different scientific names
def scientific_names_list():
    names = []
    for x in dolphins:
        if x["Scientific name"] not in names:
            names.append(x["Scientific name"])
    return names

scientific_names_list()

print(" ")

#Prints a list of years
def years_list():
    years = []
    for x in dolphins:
        if x["Year observed"] not in years:
            years.append(x["Year observed"])
    return years

years_list()

print(" ")

#Calculates how many total dolphins of a specific species in a given year
def individuals_type_year(species, year):
    total = 0
    for x in dolphins:
        if x["Common name"] == species and x["Year observed"] == year:
            total += int(x["Total individuals"])
    return("There were " + str(total) + " " + species + " sighted in " + str(year))

print(individuals_type_year("Bottlenose dolphin - Common", "1999"))


from tkinter import *
from tkinter import Listbox
from tkinter import messagebox


def open_window():
    top = Toplevel()
    top.title("Data Lists")
    top.geometry("605x250+400+100")

    Label(top, text = "Choose a Data List Type:", anchor = "w").pack(fill = "both")

    def displayIndividuals():
        output.delete(0.0, END)
        output.insert(END, individuals())

    def displayCommonNames():
        output.delete(0.0, END)
        output.insert(END, common_names_list())

    def displayScientificNames():
        output.delete(0.0, END)
        output.insert(END, scientific_names_list())

    def displayYears():
        output.delete(0.0, END)
        output.insert(END, years_list())
        
    btnIndividuals = Button(top, text = "List Individuals", command = displayIndividuals)
    btnIndividuals.pack(anchor = "w")
    
    btnCommonNames = Button(top, text = "List Common Names", command = displayCommonNames)
    btnCommonNames.pack(anchor = "w")
    
    btnScientificNames = Button(top, text = "List Scientific Names", command = displayScientificNames)
    btnScientificNames.pack(anchor = "w")
    
    btnYearsList = Button(top, text = "List Years List", command = displayYears)
    btnYearsList.pack(anchor = "w")

    output = Text(top, width = 75, height = 6, wrap = WORD, background = "white")
    output.pack(anchor = "w")


def getrecord_window():
    def click():
        entered_text = textentry.get()
        output.delete(0.0, END)
        output.insert(END, getrecord(int(textentry.get())))
        
    top = Toplevel()
    top.title("Get Record Function")
    top.geometry("605x210+400+430")

    Label (top, text = "Get Record Function", anchor = "w").pack(fill = "both")
    Label (top, text = "Record Number (Between 1-387):", anchor = "w").pack(fill = "both")

    textentry = Entry(top, width = 20, bg = "white")
    textentry.pack(anchor = "w")

    Button (top, text = "Check record", width = 12, command = click).pack(anchor = "w")

    output = Text(top, width = 75, height = 6, wrap = WORD, background = "white")
    output.pack(anchor = "w")

def type_window():
    def click():
        entered_text = typeListbox.get(ACTIVE)
        output.delete(0.0, END)
        output.insert(END, individuals_type((typeListbox.get(ACTIVE))))
        
    top = Toplevel()
    top.title("Individuals Type Function")
    top.geometry("605x350+420+450")

    Label(top, text = "Returns the number of individuals based on common name", anchor = "w").pack(fill = "both")
    Label(top, text = "Common Name:", anchor = "w").pack(fill = "both")

    typeListbox = Listbox(top, width = 30)
    typeListbox.pack(anchor = W)
    for name in common_names_list():
        typeListbox.insert(END, name)
    
    Button (top, text = "Check record", width = 12, command = click).pack(anchor = "w")

    output = Text(top, width = 75, height = 6, wrap = WORD, background = "white")
    output.pack(anchor = "w")

def year_window():
    def click():
        entered_text = yearListbox.get(ACTIVE)
        output.delete(0.0, END)
        output.insert(END, individuals_year((yearListbox.get(ACTIVE))))
        
    top = Toplevel()
    top.title("Individuals Year Function")
    top.geometry("605x350+440+470")

    Label (top, text = "Returns the number of individuals sighted in a year", anchor = "w").pack(fill = "both")
    Label (top, text = "Year:", anchor = "w").pack(fill = "both")


    frame = Frame(top)
    frame.pack(anchor = "w")
    yearListbox = Listbox(frame, exportselection = 0, width = 30)
    yearListbox.pack(side = "left", fill = "y")

    scrollbar = Scrollbar(frame, orient = "vertical")
    scrollbar.config(command = yearListbox.yview)
    scrollbar.pack(side = "right", fill = "y")

    yearListbox.config(yscrollcommand = scrollbar.set)
    
    years = years_list()
    years.sort()
    for year in years:
        yearListbox.insert(END, year)


    Button (top, text = "Check record", width = 12, command = click).pack(anchor = "w")

    output = Text(top, width = 75, height = 6, wrap = WORD, background = "white")
    output.pack(anchor = "w")


def open_window3():
    top = Toplevel()
    top.title("Individuals list by Name & Year")
    top.geometry("605x530+420+120")

    def click():
            output.delete(0.0, END)
            output.insert(END, individuals_type_year(nameListbox.get(ACTIVE), yearListbox.get(ACTIVE)))

    Label(top, text = "Function that returns the individuals recorded by species in a certain year.", anchor = "w").pack(fill = "both")
    
    Label(top, text = "Common Name:", anchor = "w").pack(fill = "both")
    nameListbox = Listbox(top, exportselection = 0, width = 30)
    nameListbox.pack(anchor = W)
    names = common_names_list()
    names.sort()
    for name in names:
        nameListbox.insert(END, name)
    
    Label(top, text = "Year:").pack(anchor = "w")
    frame = Frame(top)
    frame.pack(anchor = "w")
    yearListbox = Listbox(frame, exportselection = 0, width = 30)
    yearListbox.pack(side = "left", fill = "y")

    scrollbar = Scrollbar(frame, orient = "vertical")
    scrollbar.config(command = yearListbox.yview)
    scrollbar.pack(side = "right", fill = "y")

    yearListbox.config(yscrollcommand = scrollbar.set)

    years = years_list()
    years.sort()
    for year in years:
        yearListbox.insert(END, year)

    Button(top, text = "Check record", width = 12, command = click).pack(anchor = "w")

    output = Text(top, width = 75, height = 6, wrap = WORD, background = "white")
    output.pack(anchor = "w")


def func(value):
    messagebox.showinfo("Dolphin Database", value)
    if value == "Get Record":
        getrecord_window()
    elif value == "Individuals Type":
        type_window()
    elif value == "Individuals Year":
        year_window()

window = Tk()
window.title("Dolphin Database")
window.geometry("360x135+40+100")

myPhoto = PhotoImage(file = "backup.gif")
Label (window, image = myPhoto).grid(column = 0, row = 5, sticky = W)

defaultWindow = Label(window, text = "This application shows dolphin data for you in this friendly GUI", font = "none 9 bold")
defaultWindow.grid(column = 0, row = 0, sticky = W)
defaultWindow1 = Label(window, text = "Tap a button to get started :)")
defaultWindow1.grid(column = 0, row = 1, sticky = W)
datalist = StringVar(window)
datalist.set("Functions w/ 1 Arguments")
functionList = ["Get Record", "Individuals Type", "Individuals Year"]
drop = OptionMenu(window, datalist, *functionList, command = func)

btn = Button(window, text = "Data Lists", command = open_window)
btn2 = Button(window, text = "Function w/ 2 Arguments", command = open_window3)
btn.grid(column = 0, row = 2, sticky = W)
btn2.grid(column = 0, row = 3, sticky = W)
drop.grid(column = 0, row = 4, sticky = W)

window.mainloop()

