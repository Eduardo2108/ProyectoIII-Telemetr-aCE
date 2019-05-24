
from tkinter import *
"""
Clase que dibuja la ventana principal
"""
class Ventana:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.flag = True

    def Quit(self):
        self.flag = False
        print('quit')

    def __draw__(self):
        #Ventana Principal
        V_inicio = Tk()
        V_inicio.title('Formula CE')
        V_inicio.minsize(self.width, self.height)
        V_inicio.resizable(width=NO, height=NO)
        #_________________________
        # Canvas de la ventana...
        #_________________________

        C_inicio = Canvas(V_inicio, width=self.width, height=self.height, bg='white')
        C_inicio.place(x=0, y=0)

        #_______________________________________
        # Crea la cinta de opciones del programa
        #_______________________________________
        cinta_opciones = Menu(V_inicio)
        V_inicio.config(menu=cinta_opciones)

        # Boton Home
        cinta_opciones.add_cascade(label='Home')
        cinta_opciones.add_separator()

        # Boton about
        cinta_opciones.add_cascade(label='About')
        cinta_opciones.add_separator()

        # Boton posiciones
        cinta_opciones.add_cascade(label='Positions')
        cinta_opciones.add_separator()

        # boton de Test drive
        cinta_opciones.add_cascade(label='Test drive')

        # boton de salida
        cinta_opciones.add_cascade(label='Quit', command=self.Quit)
        V_inicio.mainloop()

