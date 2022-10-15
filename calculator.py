from tkinter import *
from math import sqrt

window = Tk()
window.geometry("377x355+600+300")
window.resizable(False, False)
window.title("Calculator")
window.configure(background="#000060")

expression = ""


def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def button_clear_all():
    global expression
    expression = ""
    input_text.set("0")


def button_clear_one():
    global expression
    expression = expression[:-1]
    input_text.set(expression)
    if expression == "":
        input_text.set("0")


def button_equal():
    try:
        global expression
        result = str(eval(expression))  # 'eval':This function is used to evaluates the string expression directly
        input_text.set(result)
        expression = result
    except:
        input_text.set("Choose other number")


# def percent():
#     global expression
#     expression = expression.split("-")
#     print(expression)
#     percentage = float(expression[0]/expression[1])
#     result = str(percentage)
#     input_text.set(result)
#     expression = result


def square_root():
    try:
        global expression
        sq_root_value = sqrt(float(expression))
        result = str(sq_root_value)
        input_text.set(result)
        expression = result
    except:
        input_text.set("error")


def x_na_vtora():
    try:
        global expression
        x = pow(float(expression), 2)
        result = str(x)
        input_text.set(result)
        expression = result
    except:
        pass


def plus_minus():
    try:
        global expression
        expression = float(expression)
        if float(expression) <= 0:
            expression = abs(float(expression))
        else:
            expression = -abs(float(expression))
        expression = str(expression)
        input_text.set(str(expression))
    except:
        pass


input_text = StringVar()
input_text.set("0")

expression_field = Entry(window, textvariable=input_text, justify=RIGHT, font=('"Digital 7" 20'))
expression_field.place(x=3, y=2, width=371, height=50)

# ------------ 1 red
button_clr_all = Button(window, text='Clear', bg='red', command=lambda: button_clear_all(), font=('"Digital 7" 20'))
button_clr_all.place(x=2, y=55, height=60, width=150)

button_clr_one = Button(window, text='←', bg='orange', command=lambda: button_clear_one(), font=('"Digital 7" 20'))
button_clr_one.place(x=152, y=55, height=60, width=75)

button_koren = Button(window, text='√', bg='#909090', command=lambda: square_root(), font=('"Digital 7" 20'))
button_koren.place(x=227, y=55, height=60, width=75)

button_x_2 = Button(window, text='x²', bg='#909090', command=lambda: x_na_vtora(), font=('"Digital 7" 20'))
button_x_2.place(x=302, y=55, height=60, width=75)

# ------------ 2 red
button7 = Button(window, text='7', bg='#E0E0E0', command=lambda: button_click("7"), font=('"Digital 7" 20'))
button7.place(x=2, y=115, height=60, width=75)

button8 = Button(window, text='8', bg='#E0E0E0', command=lambda: button_click("8"), font=('"Digital 7" 20'))
button8.place(x=77, y=115, height=60, width=75)

button9 = Button(window, text='9', bg='#E0E0E0', command=lambda: button_click("9"), font=('"Digital 7" 20'))
button9.place(x=152, y=115, height=60, width=75)

button_open = Button(window, text='(', bg='#909090', command=lambda: button_click("("), font=('"Digital 7" 20'))
button_open.place(x=227, y=115, height=60, width=75)

button_close = Button(window, text=')', bg='#909090', command=lambda: button_click(")"), font=('"Digital 7" 20'))
button_close.place(x=302, y=115, height=60, width=75)

# ------------ 3 red
button4 = Button(window, text='4', bg='#E0E0E0', command=lambda: button_click("4"), font=('"Digital 7" 20'))
button4.place(x=2, y=175, height=60, width=75)

button5 = Button(window, text='5', bg='#E0E0E0', command=lambda: button_click("5"), font=('"Digital 7" 20'))
button5.place(x=77, y=175, height=60, width=75)

button6 = Button(window, text='6', bg='#E0E0E0', command=lambda: button_click("6"), font=('"Digital 7" 20'))
button6.place(x=152, y=175, height=60, width=75)

button_add = Button(window, text='+', bg='#909090', command=lambda: button_click("+"), font=('"Digital 7" 20'))
button_add.place(x=227, y=175, height=60, width=75)

button_subtract = Button(window, text='-', bg='#909090', command=lambda: button_click("-"), font=('"Digital 7" 20'))
button_subtract.place(x=302, y=175, height=60, width=75)

# ------------ 4 red
button1 = Button(window, text='1', bg='#E0E0E0', command=lambda: button_click("1"), font=('"Digital 7" 20'))
button1.place(x=2, y=235, height=60, width=75)

button2 = Button(window, text='2', bg='#E0E0E0', command=lambda: button_click("2"), font=('"Digital 7" 20'))
button2.place(x=77, y=235, height=60, width=75)

button3 = Button(window, text='3', bg='#E0E0E0', command=lambda: button_click("3"), font=('"Digital 7" 20'))
button3.place(x=152, y=235, height=60, width=75)

button_multiply = Button(window, text='*', bg='#909090', command=lambda: button_click("*"), font=('"Digital 7" 20'))
button_multiply.place(x=227, y=235, height=60, width=75)

button_division = Button(window, text='/', bg='#909090', command=lambda: button_click("/"), font=('"Digital 7" 20'))
button_division.place(x=302, y=235, height=60, width=75)

# ------------ 5 red
button_plus_minus = Button(window, text='±', bg='#E0E0E0', command=lambda: plus_minus(), font=('"Digital 7" 20'))
button_plus_minus.place(x=2, y=295, height=60, width=75)

button_decimal = Button(window, text=',', bg='#E0E0E0', command=lambda: button_click("."), font=('"Digital 7" 20'))
button_decimal.place(x=152, y=295, height=60, width=75)

button0 = Button(window, text='0', bg='#E0E0E0', command=lambda: button_click("0"), font=('"Digital 7" 20'))
button0.place(x=77, y=295, height=60, width=75)

button_ravno = Button(window, text='=', bg='green', command=lambda: button_equal(), font=('"Digital 7" 20'))
button_ravno.place(x=227, y=295, height=60, width=150)


window.mainloop()
