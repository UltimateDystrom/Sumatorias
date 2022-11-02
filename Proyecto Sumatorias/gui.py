from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
from summatory import *
from tkinter import messagebox
from pathlib import Path
from tkinter import filedialog
from pathlib import Path

# Basic frame configs
root = Tk()
root.title("Sumatorias")
icon = ImageTk.PhotoImage(Image.open('images/logo sumatorias.png'))
root.wm_iconphoto(False, icon)
root.resizable(FALSE, FALSE)
root.option_add('*tearOff', FALSE)
root.geometry('700x500+450+100')

# Functions
def calculate():
    expression = e.get()
    min_num = e_i.get()
    max_num = e_n.get()
    variable = e_v.get()

    if expression == "" or min_num == "" or max_num == "" or variable == "":
        messagebox.showwarning("Error", "Rellena todos los campos.")

    try:
        min_num = int(min_num)
        max_num = int(max_num)
    except:
        messagebox.showwarning("Error", "No ingresaste un rango válido.")
    
    if isRight(expression, variable):
        sum = str(summatory(expression, variable, min_num, max_num))
        lbl_result['text'] = sum
        bttn_p = Button(root, text="¿Deseas ver el procedimiento?", fg='black', bg='#c6bfa6', borderwidth=2, width=-20, height=-2000, command= lambda: process(expression, min_num, max_num, variable))
        bttn_p.place(x=285, y=270)
    else:
        messagebox.showwarning("Error", "Expresión no válida.")

def process(expression, min_num, max_num, variable):

    l_process = summatory_p(expression, variable, min_num, max_num)
    s_process = ""

    if expression == "" or min_num == "" or max_num == "" or variable == "":
        messageboxshowwarning("Error", "Rellena todos los campos.")

    for i in l_process:
        s_process += i
        s_process += "\n"

    path = str(Path.home() / 'Downloads')

    file = filedialog.asksaveasfile(initialdir= path, defaultextension='.txt', filetypes=[("Archivo de Texto", ".txt")])
    file.write(s_process)


def info_help():
    messagebox.showinfo("Información", "El programa utiliza como expresión matemáticas las reglas de Python:\n + = Suma\n - = Resta\n * = Multiplicación\n / = División\n ** = Exponente\n Se puede utilizar el factorial encerrando una expresión\n en una función fact y encerrar esa función\n entre paréntesis.\n Ejemplo:\n Factorial de x multiplicando a 5x:\n (fact(x))*(5*x)\n")


def info_creator():
    messagebox.showinfo("Acerca de", "Programa creado por Dylan H. Rojas.")

# Menu bar
menubar = Menu(root)
root['menu'] = menubar
menu_options = Menu(menubar)

menubar.add_cascade(menu=menu_options, label='Opciones')
menu_options.add_command(label='Ayuda', command= info_help)
menu_options.add_command(label='Salir', command= root.quit)
menu_options.add_command(label='Acerca de', command= info_creator)

# Background
img_bg = ImageTk.PhotoImage(Image.open('images/Interfaz Sumatorias.png'))
lbl_bg = Label(root, image= img_bg)
lbl_bg.place(x=0, y=0)

# Entries
e = Entry(root, width=35, borderwidth=5)
e.place(x=260, y=180)

e_n = Entry(root, width=5, borderwidth=2)
e_n.place(x=177, y=125)

e_i = Entry(root, width=5, borderwidth=2)
e_i.place(x=190, y=250)

e_v = Entry(root, width=5, borderwidth=2)
e_v.place(x=580,y=150)

# Button calculate
img_bttn = ImageTk.PhotoImage(Image.open('images/boton calcular suma.png'))
bttn_1 = Button(image=img_bttn, bg='#c6bfa6', borderwidth=0, command=calculate)
bttn_1.place(x=295, y=220)

# Label result
lbl_result = Label(root, text="", font=("Cambria Math", 20), fg='black', background= '#c6bfa6')
lbl_result.place(x=320, y=338)
root.mainloop()