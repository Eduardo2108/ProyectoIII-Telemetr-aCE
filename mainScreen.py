
from tkinter import *
"""
Clase que dibuja la ventana principal
"""
class Ventana:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.flag = True
        #Settings of window

        #Window itself
        self.V_inicio = Tk()
        self.V_inicio.title('Formula CE')
        self.V_inicio.minsize(self.width, self.height)
        self.V_inicio.resizable(width=NO, height=NO)
        #Main canvas
        self.C_inicio = Canvas(self.V_inicio, width=self.width, height=self.height, bg='white')

        #Main menu

        self.cinta_opciones = Menu(self.V_inicio)
        self.V_inicio.config(menu=self.cinta_opciones)

    def Quit(self):
        self.flag = False
        print('quit')
    def canvas_clean(self):
        pass
    def test_drive(self):
        



    def __draw__(self):
        #_________________________
        # Canvas de la ventana...
        #_________________________
        self.C_inicio.place(x=0, y=0)
        # Boton Home
        self.cinta_opciones.add_cascade(label='Home')
        self.cinta_opciones.add_separator()

        # Boton about
        self.cinta_opciones.add_cascade(label='About')
        self.cinta_opciones.add_separator()

        # Boton posiciones
        self.cinta_opciones.add_cascade(label='Positions')
        self.cinta_opciones.add_separator()

        # boton de Test drive
        self.cinta_opciones.add_cascade(label='Test drive')

        # boton de salida
        self.cinta_opciones.add_cascade(label='Quit', command=self.Quit)
        self.V_inicio.mainloop()

ventana = Ventana(500,500)

ventana.__draw__()