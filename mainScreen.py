from tkinter import *
from threading import Thread
import threading
import time
import os
import winsound
import random
from tkinter import messagebox

"""
Clase que dibuja la ventana principal

Atributos:
height(entrada)>>> int, valor del alto de la ventana a crear
width(entrada)>>> int, valor del ancho de la ventana a crear

V_inicio >>> atributo que tiene como valor una instancia de ventana en tkinter
V_inicio.title >>> nombre de la ventana (titulo)
V_inicio >>> medidas de la ventana
V_inicio.resizable >>> control sobre el cambio de tamano de la ventana

C_inicio >>> canvas principal

cinta_opciones >>> menu en la ventana
V_inicio.config >>> configuracion de la ventana, para el menu.

Metodos:

canvas_clean >>> funcion que resetea el canvas, para hacer el cambio de pantalla
test_drive >>> funcion que dibuja todo lo necesario para la pantalla de pruebas
positions >>> dibuja la ventana de posiciones
about >>> dibuja la ventana de informacion
inicio >>> dibuja la ventana principal

__draw__ >>> funcion que pone todo en la pantalla y la actualiza

"""

class Ventana:

    def __init__(self, width, height):

        #-------------------Settings of window-----------------#
        self.height = height
        self.width = width

        #Window itself
        self.V_inicio = Tk()
        self.V_inicio.title('Formula CE')
        self.V_inicio.minsize(self.width, self.height)
        self.V_inicio.resizable(width=NO, height=NO)

        #Main canvas
        self.C_inicio = Canvas(self.V_inicio, width=self.width, height=self.height, bg='white')
        self.C_inicio.place(x=0, y=0)

        #Main menu
        self.cinta_opciones = Menu(self.V_inicio)
        self.V_inicio.config(menu=self.cinta_opciones)

        self.pwm = 0

    def cargarImagen(self, nombre):
        ruta = os.path.join('resources', nombre)
        imagen = PhotoImage(file=ruta)
        return imagen

    def canvas_clean(self):
        self.C_inicio.delete('all')

    def test_drive(self, car, driver, country, team):
        count = StringVar()
        count.set(0)
        def acelera():

            if self.pwm == 1020:
                print("velocidad maxima")
            else:
                self.pwm += 10
                count.set(self.pwm)


        def brake():

            if self.pwm == -1023:
                print("reversa maxima")
            else:
                self.pwm-=10
                count.set(self.pwm)
        #lineas guias para diseño del entorno... ''
        #______________________________
        self.C_inicio.create_line(0,(self.height/2),self.width,(self.height/2)) #horizontal
        self.C_inicio.create_line((self.width/2),0,  (self.width /2), self.height,) #vertical

        #Etiquetas de informacion, carro, piloto...
        marcaAuto = Label(self.C_inicio, text= str(car), font=("Arial ", 12), justify=CENTER)
        marcaAuto.place(x=10,y=10) #Etiqueta del modelo del carro...
        Nombre = Label(self.C_inicio, text = str(driver), font=('Arial', 12), width =9,justify= LEFT)
        Nombre.place(x=10, y= 40)
        Country = Label(self.C_inicio, text= str(country),font=('Arial', 12), justify=CENTER)
        Country.place(x=110, y= 40)
        Team = Label(self.C_inicio, text = 'Team ' + str(team),font=('Arial', 12), justify=CENTER )
        Team.place(x=10, y =70)
        #---|------------------------|
        #   |  COMANDOS DEL CARRO    |
        #---|------------------------|
        #--------------------Carga Imagenes--------------------------#
        gas_image = self.cargarImagen('gas.png')
        brake_image = self.cargarImagen('brake.png')
        #---------------------Acelerador-----------------------------#
        gas = Button(self.C_inicio, text='gas',command = acelera)
        gas.place(x=750, y=430)
        #------------------------Freno-------------------------------#
        freno = Button(self.C_inicio,text='brake', command = brake)
        freno.place(x=900, y=430)
        #-----------------Indicador velocidad------------------------#
        #self.C_inicio.create_text(330, 300, textvariable= count,font=("Unispace", "20"), anchor=NW)
        l = Label(self.C_inicio, textvariable=count,font=('Unispace', 45))
        l.place(x=490,y=300)
        #-----------------------Direccionales------------------------#


    def inicio(self):
        pass

    def about(self):
        pass

    def positions(self):
        pass

    def __draw__(self):

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
        self.cinta_opciones.add_cascade(label='Test drive',command= lambda: self.test_drive('Ferrari 428 italia ', 'Eduardo', 'CRC','Redbull'))


        self.V_inicio.mainloop()

ventana = Ventana(1024,728)

ventana.__draw__()