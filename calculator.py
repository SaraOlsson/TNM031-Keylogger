# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
#expression = ""

class Calculator:

	def __init__(self):
		self.expression = ""
		self.equation = None
		self.gui = None

		self.init_calculator()

	# Function to update expressiom
	# in the text entry box
	def press(self, num):
		# point out the global expression variable
		#global expression

		# concatenation of string
		self.expression = self.expression + str(num)

		# update the expression by using set method
		self.equation.set(self.expression)


	# Function to evaluate the final expression
	def equalpress(self):
		# Try and except statement is used
		# for handling the errors like zero
		# division error etc.

		# Put that code inside the try block
		# which may generate the error
		try:

			#global expression

			# eval function evaluate the expression
			# and str function convert the result
			# into string
			total = str(eval(self.expression))

			self.equation.set(total)

			# initialze the expression variable
			# by empty string
			self.expression = ""

		# if error is generate then handle
		# by the except block
		except:

			self.equation.set(" error ")
			self.expression = ""


	# Function to clear the contents
	# of text entry box
	def clear(self):
		#global expression
		self.expression = ""
		self.equation.set("")

	def quit(self):
		#print("quit")
		self.gui.destroy()

	def init_calculator(self):

		# create a GUI window
		self.gui = Tk()

		# set the background colour of GUI window
		self.gui.configure(background="light gray")

		# set the title of GUI window
		self.gui.title("Simple Calculator")

		# set the configuration of GUI window
		self.gui.geometry("265x125")

		# StringVar() is the variable class
		# we create an instance of this class
		self.equation = StringVar()

		# create the text entry box for
		# showing the expression .
		expression_field = Entry(self.gui, textvariable=self.equation)

		# grid method is used for placing
		# the widgets at respective positions
		# in table like structure .
		expression_field.grid(columnspan=4, ipadx=70)

		self.equation.set('enter your expression')

		bg_color = 'white'
		# create a Buttons and place at a particular
		# location inside the root window .
		# when user press the button, the command or
		# function affiliated to that button is executed .
		button1 = Button(self.gui, text=' 1 ', fg='black', bg=bg_color,
						command=lambda: self.press(1), height=1, width=7)
		button1.grid(row=2, column=0)

		button2 = Button(self.gui, text=' 2 ', fg='black', bg=bg_color,
						command=lambda: self.press(2), height=1, width=7)
		button2.grid(row=2, column=1)

		button3 = Button(self.gui, text=' 3 ', fg='black', bg=bg_color,
						command=lambda: self.press(3), height=1, width=7)
		button3.grid(row=2, column=2)

		button4 = Button(self.gui, text=' 4 ', fg='black', bg=bg_color,
						command=lambda: self.press(4), height=1, width=7)
		button4.grid(row=3, column=0)

		button5 = Button(self.gui, text=' 5 ', fg='black', bg=bg_color,
						command=lambda: self.press(5), height=1, width=7)
		button5.grid(row=3, column=1)

		button6 = Button(self.gui, text=' 6 ', fg='black', bg=bg_color,
						command=lambda: self.press(6), height=1, width=7)
		button6.grid(row=3, column=2)

		button7 = Button(self.gui, text=' 7 ', fg='black', bg=bg_color,
						command=lambda: self.press(7), height=1, width=7)
		button7.grid(row=4, column=0)

		button8 = Button(self.gui, text=' 8 ', fg='black', bg=bg_color,
						command=lambda: self.press(8), height=1, width=7)
		button8.grid(row=4, column=1)

		button9 = Button(self.gui, text=' 9 ', fg='black', bg=bg_color,
						command=lambda: self.press(9), height=1, width=7)
		button9.grid(row=4, column=2)

		button0 = Button(self.gui, text=' 0 ', fg='black', bg=bg_color,
						command=lambda: self.press(0), height=1, width=7)
		button0.grid(row=5, column=0)

		plus = Button(self.gui, text=' + ', fg='black', bg=bg_color,
					command=lambda: self.press("+"), height=1, width=7)
		plus.grid(row=2, column=3)

		minus = Button(self.gui, text=' - ', fg='black', bg=bg_color,
					command=lambda: self.press("-"), height=1, width=7)
		minus.grid(row=3, column=3)

		multiply = Button(self.gui, text=' * ', fg='black', bg=bg_color,
						command=lambda: self.press("*"), height=1, width=7)
		multiply.grid(row=4, column=3)

		divide = Button(self.gui, text=' / ', fg='black', bg=bg_color,
						command=lambda: self.press("/"), height=1, width=7)
		divide.grid(row=5, column=3)

		equal = Button(self.gui, text=' = ', fg='black', bg=bg_color,
					command=self.equalpress, height=1, width=7)
		equal.grid(row=5, column=2)

		clear = Button(self.gui, text='Clear', fg='black', bg=bg_color,
					command=self.clear, height=1, width=7)
		clear.grid(row=5, column='1')

		self.gui.bind('<Escape>', lambda e: self.gui.destroy())

		# start the self.gui
		self.gui.mainloop()
