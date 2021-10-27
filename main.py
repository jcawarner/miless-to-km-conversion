from tkinter import *


def conversion():
	conv = round(int(miles.get()) * 1.609344, 2)
	km_conversion.config(text=conv)


window = Tk()
window.title("Miles to Kilometers")
window.config(padx=20, pady=20)
window.minsize(width=200, height=150)

enter_miles = Label(window, text="Enter Miles:")
enter_miles.grid(row=0, column=0)
enter_miles.config(padx=10, pady=10)

miles = Entry(width=5)
miles.grid(row=0, column=1)

miles_label = Label(window, text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to = Label(window, text="is equal to")
is_equal_to.grid(row=1, column=0)

km_conversion = Label(window, text=0)
km_conversion.grid(row=1, column=1)
km_conversion.config(padx=10, pady=10)

km_label = Label(window, text="Km")

calculate_button = Button(window, text="Calculate", command=conversion)
calculate_button.grid(row=2, column=1)
calculate_button.

window.mainloop()
