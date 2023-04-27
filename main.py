from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x300")

# create a frame that has the entire length covered
frame = Frame(root , bg = "grey", borderwidth = 5, relief = SUNKEN)
frame.pack(side = TOP, fill = X)

# create a frame that has the entire length and width covered
frame2 = Frame(root , bg = "grey", borderwidth = 5, relief = SUNKEN)
frame2.pack(side = TOP, fill = BOTH, expand = True)

# there is an entry widget inside the first frame
e = Entry(frame, width = 35, borderwidth = 5)
e.pack(side= TOP, fill = X)

# there are buttons of numbers, operators and clear button inside the second frame
b1 = Button(frame2, text = "1", padx = 40, pady = 20)  
b2 = Button(frame2, text = "2", padx = 40, pady = 20)
b3 = Button(frame2, text = "3", padx = 40, pady = 20)
b4 = Button(frame2, text = "4", padx = 40, pady = 20)
b5 = Button(frame2, text = "5", padx = 40, pady = 20)
b6 = Button(frame2, text = "6", padx = 40, pady = 20)
b7 = Button(frame2, text = "7", padx = 40, pady = 20)
b8 = Button(frame2, text = "8", padx = 40, pady = 20)
b9 = Button(frame2, text = "9", padx = 40, pady = 20)
b0 = Button(frame2, text = "0", padx = 40, pady = 20)
b_add = Button(frame2, text = "+", padx = 40, pady = 20)
b_sub = Button(frame2, text = "-", padx = 40, pady = 20)
b_mul = Button(frame2, text = "*", padx = 40, pady = 20)
b_div = Button(frame2, text = "/", padx = 40, pady = 20)
b_equal = Button(frame2, text = "=", padx = 40, pady = 20)
b_clear = Button(frame2, text = "Clear", padx = 40, pady = 20)

# here all the buttons are packed using grid
b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 0, column = 2)
b_add.grid(row = 0, column = 3)
b4.grid(row = 1, column = 0)
b5.grid(row = 1, column = 1)
b6.grid(row = 1, column = 2)
b_sub.grid(row = 1, column = 3)
b7.grid(row = 2, column = 0)
b8.grid(row = 2, column = 1)
b9.grid(row = 2, column = 2)
b_mul.grid(row = 2, column = 3)
b0.grid(row = 3, column = 0)
b_clear.grid(row = 3, column = 1)
b_equal.grid(row = 3, column = 2)
b_div.grid(row = 3, column = 3)


root.mainloop()
