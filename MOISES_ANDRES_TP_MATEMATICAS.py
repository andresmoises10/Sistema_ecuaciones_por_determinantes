import tkinter as tk
from tkinter import Toplevel, Label, Entry, Button, Menu, messagebox
import tkinter as tk
from tkinter import *
import pandas as pd
from PIL import Image,ImageTk

def salir():
    ventana.destroy()

def mostrar_info():
    messagebox.showinfo("Acerca de...", "Desarrollado por: MOISÉS AZIZE, ANDRÉS")

def mostrar_matriz_det(a, b, c, d):
    ventana_matriz = Toplevel(ventana)
    ventana_matriz.title("Matriz ▲")
    delta_del_sistema = [[a, b], [c, d]]
    df_delta_del_sistema = pd.DataFrame(delta_del_sistema)

    label_matriz = tk.Label(ventana_matriz, text=df_delta_del_sistema.to_string(index=False, header=False))
    label_matriz.pack(padx=60, pady=30)

def mostrar_matriz_det_x(n_1, n_2, b,d):
    ventana_matriz = Toplevel(ventana)
    ventana_matriz.title("Matriz ▲X")
    delta_del_sistema_x = [[n_1, b], [n_2, d]]
    df_delta_del_sistema_x = pd.DataFrame(delta_del_sistema_x)

    label_matriz_x = tk.Label(ventana_matriz, text=df_delta_del_sistema_x.to_string(index=False, header=False))
    label_matriz_x.pack(padx=60, pady=30)

def mostrar_matriz_det_y(a, c, n_1, n_2):
    ventana_matriz = Toplevel(ventana)
    ventana_matriz.title("Matriz ▲Y")
    delta_del_sistema_y = [[a, n_1], [c, n_2]]
    df_delta_del_sistema_y = pd.DataFrame(delta_del_sistema_y)

    label_matriz_y = tk.Label(ventana_matriz, text=df_delta_del_sistema_y.to_string(index=False, header=False))
    label_matriz_y.pack(padx=60, pady=30)

def resolver_ecuaciones():
    a = int(entrada_a.get())
    b = int(entrada_b.get())
    c = int(entrada_c.get())
    d = int(entrada_d.get())
    n_1 = int(entrada_n_1.get())
    n_2 = int(entrada_n_2.get())

    #determinante = int((a * d) - (b * c))

    #determinante_X = int((n_1 * d) - (n_2 * b))
    
    #determinante_Y = int((n_2 * a) - (n_1 * c))

    #resultado_de_X = int((determinante_X / determinante))
    #resultado_de_Y = int((determinante_Y / determinante))

    #resultado_de_X = determinante_X / determinante
    #resultado_de_Y = determinante_Y / determinante

    determinante = a * d - b * c

    determinante_X = n_1 * d - n_2 * b

    determinante_Y = n_2 * a - n_1 * c

    resultado_de_X = determinante_X / determinante
    resultado_de_Y = determinante_Y / determinante

    resultado_de_X = int(resultado_de_X)
    resultado_de_Y = int(resultado_de_Y)

    lbl_resultados_x = Label(ventana, text="El valor de X en este sistema de ecuaciones es = " + str(resultado_de_X))
    lbl_resultados_x.place(y=325, x=50)

    lbl_resultados_y = Label(ventana, text="El valor de Y en este sistema de ecuaciones es = " + str(resultado_de_Y))
    lbl_resultados_y.place(y=345, x=50)
  
# ACÁ SE CREA LA VENTANA-------------------------------------

ventana = tk.Tk()
ventana.geometry("400x400")
ventana.title("TP promoción Matemáticas y Lógica")
ventana.resizable(width=False, height=False)

imagen_fondo = Image.open("C:/Users/andre/OneDrive/Escritorio/COLOQUIOS/FONDO_TP.png")
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
label_fondo = tk.Label(ventana, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
label_fondo = tk.Label(ventana, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Crear la barra de menú
menu = Menu(ventana)
ventana.config(menu=menu)

# Crear menús desplegables
ver_matrices = Menu(menu, tearoff=0)
menu.add_cascade(label="Ver matrices", menu=ver_matrices, font=("Arial", 12))

# MOSTRAR MATRICES 

#MATRIZ DETERMINANTE
ver_matrices.add_command(label="Matriz ▲", font=("Arial", 10), command=lambda: mostrar_matriz_det(
    int(entrada_a.get()), int(entrada_b.get()), int(entrada_c.get()), int(entrada_d.get())))

#MATRIZ X 
ver_matrices.add_command(label="Matriz ▲X", font=("Arial", 10), command=lambda: mostrar_matriz_det_x(int(entrada_n_1.get()),
    int(entrada_n_2.get()),int(entrada_b.get()),int(entrada_d.get())))

#MATRIZ Y
ver_matrices.add_command(label="Matriz ▲Y", font=("Arial", 10), command=lambda: mostrar_matriz_det_y(
    int(entrada_a.get()), int(entrada_c.get()),int(entrada_n_1.get()), int(entrada_n_2.get())))

ayuda = Menu(menu, tearoff=0)
menu.add_cascade(label="Ayuda", menu=ayuda)
ayuda.add_command(label="Acerca de....", command=mostrar_info)

salir_del_programa = Menu(menu, tearoff=0)
menu.add_cascade(label="Salir", menu=salir_del_programa)
salir_del_programa.add_command(label="WAKANDA FOREVER", command=salir)

lbl = Label(ventana, text="¡HOLA!\n\nBIENVENIDO A UN ATRAPANTE PROGRAMA\n\nEste programa resolverá un sistema de dos ecuaciones\nmediante el método de determinantes\nsegún el siguiente modelo: \n")
lbl.pack(side="top", pady=20)

lbl_1eq = Label(ventana, text="Por favor ingrese en orden los datos de las ecuaciones:\n")
lbl_1eq.pack(side="top", pady=60)

a_txt=StringVar()
b_txt=StringVar()
n_1_txt=StringVar()
c_txt=StringVar()
d_txt=StringVar()
n_2_txt=StringVar()

a_txt.set("aX")
b_txt.set("bY")
n_1_txt.set("n1")
c_txt.set("cX")
d_txt.set("dY")
n_2_txt.set("n2")

entrada_a = Entry(ventana, textvariable=a_txt)
entrada_a.place(y=250, x=70, width=30, height=30)

entrada_b = Entry(ventana, textvariable=b_txt)
entrada_b.place(y=250, x=110, width=30, height=30)

entrada_n_1 = Entry(ventana, textvariable=n_1_txt)
entrada_n_1.place(y=250, x=150, width=30, height=30)

entrada_c = Entry(ventana, textvariable=c_txt)
entrada_c.place(y=290, x=70, width=30, height=30)

entrada_d = Entry(ventana, textvariable=d_txt)
entrada_d.place(y=290, x=110, width=30, height=30)

entrada_n_2 = Entry(ventana, textvariable=n_2_txt)
entrada_n_2.place(y=290, x=150, width=30, height=30)

guardar = Button(ventana, text="Resolver", command=resolver_ecuaciones)
guardar.place(y=250, x=200, width=100, height=30)

ventana.mainloop()