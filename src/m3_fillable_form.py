import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# TODO: 1. (6 pts)
#
#   1) Create a tkinter window with the title "Form".
#
#   2) Add a label and an entry box for each of the following pieces of
#      information.
#
#       - Name
#       - Address Line 1
#       - Address Line 2
#       - City
#       - State
#       - Zip Code
#       - Phone Number
#       - Email Address
#
#   3) Add a "Submit" button at the bottom of your form.
#
#   4) Give your form a color theme by changing the colors of your widgets.
#      Also, feel free to change the sizes of the widgets as you see fit.
#
#   5) Make sure you call the window's mainloop() method so your window will
#      appear.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
form = tk.Tk()
form.title("Form")

name = tk.Label(
    form,
    text = "Name: ",
    bg = "white",
    fg = "black",
    width = 8
)
name.pack()
addressLine1 = tk.Label(
    form,
    text = "Address Line 1: ",
    bg = "black",
    fg = "white",
    width = 17
)
addressLine1.pack()
addressLine2 = tk.Label(
    form,
    text = "Address Line 2: ",
    bg = "white",
    fg = "black",
    width = 17
)
addressLine2.pack()
city = tk.Label(
    form,
    text = "City: ",
    bg = "black",
    fg = "white",
    width = 6
)
city.pack()
state = tk.Label(
    form,
    text = "State: ",
    bg = "white",
    fg = "black",
    width = 7
)
state.pack()
zipCode = tk.Label(
    form,
    text = "Zip Code: ",
    bg = "black",
    fg = "white",
    width = 7
)
zipCode.pack()
phoneNumber = tk.Label(
    form,
    text = "Phone Number: ",
    bg = "white",
    fg = "black",
    width = 14
)
phoneNumber.pack()
emailAddress = tk.Label(
    form,
    text = "Email Address: ",
    bg = "black",
    fg = "white",
    width = 17
)
emailAddress.pack()
form.mainloop()