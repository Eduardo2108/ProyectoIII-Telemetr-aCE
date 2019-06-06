from tkinter import *
from threading import Thread
import threading
import time
import os
import winsound
import random
from tkinter import messagebox
from time import  sleep


from WiFiClient import NodeMCU

"""
Clase que dibuja la ventana test drive 

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
myCar = NodeMCU()
myCar.start()


def get_log():
    indice = 0
    while (myCar.loop):
        while (indice < len(myCar.log)):
            mnsSend = "[{0}] cmd: {1}\n".format(indice, myCar.log[indice][0])
            SentCarScrolledTxt.insert(END, mnsSend)
            SentCarScrolledTxt.see("end")

            mnsRecv = "[{0}] result: {1}\n".format(indice, myCar.log[indice][1])
            RevCarScrolledTxt.insert(END, mnsRecv)
            RevCarScrolledTxt.see('end')

            indice += 1
        time.sleep(0.200)

p = Thread(target=get_log)
p.start()


class Test_Drive:

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
        self.C_inicio = Canvas(self.V_inicio, width=self.width, height=self.height, bg='#f0f0f0')
        self.C_inicio.place(x=0, y=0)

        #Main menu
        self.cinta_opciones = Menu(self.V_inicio)
        self.V_inicio.config(menu=self.cinta_opciones)

        self.pwm = 0
        self.dir_state = 0

    def cargarImagen(self, nombre):
        ruta = os.path.join('resources', nombre)
        imagen = PhotoImage(file=ruta)
        return imagen

    def test_drive(self, car, driver, country, team):

        count = StringVar()
        count.set(0)

        battery_level = StringVar()
        battery_level.set(100)
        color = 'black'
        dir_state = 0 #variable que guarda estado de direccionales

        # <--- | ^  |  --->
        #  -1  | 0  |  1
        def acelera(event):

            if self.pwm == 1000:
                print("velocidad maxima")
            else:
                self.pwm += 10
                count.set(self.pwm)
                cambiaColor()
        def reverse(event):

            if self.pwm == -600:
                print("reversa maxima")
            else:

                self.pwm-=10
                count.set(self.pwm)
                cambiaColor()
        def dir_lights_right():

            if self.dir_state == -1:
                self.dir_state = 0
                print('direccional derecha: ', self.dir_state)
            else:
                self.dir_state = 1
                print('direccional derecha: ', self.dir_state)
                time.sleep(0.5)

                self.dir_state = 0
                print('direccional derecha: ', self.dir_state)
                time.sleep(0.5)

                self.dir_state = 1
                print('direccional derecha: ', self.dir_state)
                time.sleep(0.5)

                self.dir_state = 0
                print('direccional derecha: ', self.dir_state)
                time.sleep(0.5)

                print('done')
        def dir_lights_left():

            if self.dir_state == 1:
                self.dir_state = 0
                print('comando direccionales: ',self.dir_state)

            else:

                self.dir_state = -1
                print('direccional izquierda: ', self.dir_state)
                time.sleep(0.5)

                self.dir_state = 0
                print('direccional izquierda: ', self.dir_state)
                time.sleep(0.5)

                self.dir_state = -1
                print('direccional izquierda: ', self.dir_state)
                time.sleep(0.5)

                self.dir_state = 0
                print('direccional izquierda: ', self.dir_state)
                time.sleep(0.5)


                print('done')
        def gira_derecha():
            turn = 1
            print('dir: ', turn)
            dir_lights_right()
            turn = 0
            print('dir: ', turn)
        def gira_izquierda():

            turn = -1
            print('dir: ' ,turn)
            dir_lights_left()
            turn = 0
            print("dir: " , turn )
        def brake(event):
            if self.pwm > 0:
                self.pwm -= 10
                count.set(self.pwm)
                cambiaColor()
            elif self.pwm <0:
                self.pwm +=10
                count.set(self.pwm)
                cambiaColor()
        def movimiento_especial(event):
            print("Envia movimiento especial...")
        def celebracion(event):
            print("Envia celebracion...")
        def enciende_frontales(event):
            print('enciende frontales')
        def enciende_traseras(event):
            print('eciende traseras')
        def enciende_emergencia(event):
            print("enciende ambas direccionales")
        def enciende_all_lights(event):
            enciende_frontales(event)
            enciende_traseras(event)
            enciende_emergencia(event)
            print('enciende todas las luces.....')


        #Etiquetas de informacion, carro, piloto...
        #Etiqueta del modelo del carro...
        marcaAuto = Label(self.C_inicio, text= 'Model: ' + str(car), font=("Arial ", 20), justify=CENTER)
        marcaAuto.place(x=0,y=10)

        Nombre = Label(self.C_inicio, text = "Driver: " +str(driver), font=("Arial", 20), width = 15,justify= LEFT)
        Nombre.place(x=-25, y= 50)

        Country = Label(self.C_inicio, text= str(country),font=('Arial', 20), justify=CENTER)
        Country.place(x=220, y= 50)

        Team = Label(self.C_inicio, text = 'Team: ' + str(team),font=('Arial', 20), justify=CENTER )
        Team.place(x=0, y =90)



        #---|------------------------|
        #   |  COMANDOS DEL CARRO    |
        #---|------------------------|

        #---------------Volante con medidor velocidad----------------#
        steer_image = self.cargarImagen('bg.png')
        steer = Label(self.C_inicio, image = steer_image)
        steer.image = steer_image
        steer.place(x=0,y=450)

        #-----------------Indicador velocidad------------------------#
        speed = Label(self.C_inicio, textvariable=count,font=('Unispace', 45),fg=color)
        speed.place(x=490,y=570)

        #Funcion que cambia el color del indicador
        def cambiaColor():

            if self.pwm == 0:
                speed.config(fg = 'green')

            elif self.pwm >= 10 and self.pwm <= 490:
                speed.config(fg= 'blue')

            elif self.pwm >= 500:
                speed.config(fg='red')

            elif self.pwm <= -10 and self.pwm >= -490:
                speed.config(fg = 'black')
            elif self.pwm <=-500:
                speed.config(fg='red')

        #--------------------Indicador de bateria--------------------#
        mark_battery = Label(self.C_inicio, text=' Battery Level: ',font=('Arial', 20))
        bat_level = Label(self.C_inicio, textvariable= (battery_level), font=('Unispace', 20))
        bat_level.place(x=950,y=0)
        mark_battery.place(x=700,y=0)
        #-----------------Threads necesarios--------------------------#

        #Threads para encender y apagar direccionales:

        def thread_dir_izq(event):
            dir_izq_thread = Thread(target= dir_lights_left, args=())
            dir_izq_thread.start()
        def thread_dir_der(event):

            dir_der_thread = Thread(target=dir_lights_right, args=())
            dir_der_thread.start()

        #Threads para girar, y encender las direccionales
        def thread_turn_right(event):
            turn_right = Thread(target=gira_derecha, args=())
            turn_right.start()
        def thread_turn_left(event):
            turn_left = Thread(target = gira_izquierda,args=())
            turn_left.start()

        #------------------Boton ayuda--------------------------------#


        def ayuda():
            Ayuda = Canvas(self.V_inicio, width = 400, height=600, bg='white')
            Ayuda.place(x=300, y= 50)

            Ayuda.create_text(200,20,text = 'How to drive ?',font=('Unispace', 20))

            Ayuda.create_text(200, 80, text='Movement:', font=('Unispace', 14))
            Ayuda.create_text(120, 140, text= ' Forward: W\n Reverse: s\n Brake: Space Bar', font=('Unispace', 12))

            Ayuda.create_text(200, 200,text= 'Direction:', font=('Unispace', 14))
            Ayuda.create_text(140,250, text='Right: Right arrow\nLeft: Left arrow', font=('Unispace',12))

            Ayuda.create_text(200, 300, text='Turn lights,¡Keep Shift down!:', font=('Unispace', 14))
            Ayuda.create_text(140,350, text='Left: Left arrow \n Right: Right arrow', font=("Unispace", 12))

            Ayuda.create_text(200, 450, text='Other lights: ', font=('Unispace', 14))
            Ayuda.create_text(140, 500, text=' Front: press l \n Back: press b \n Emergency: press e \n All: press a', font=("Unispace", 12))


            def exit():
                Ayuda.destroy()
            exit_button = Button(Ayuda, bitmap = 'error', command=exit)
            exit_button.place(x=380,y=580)





        botton_help = Button(self.C_inicio, bitmap= 'question', relief = FLAT, command= ayuda)
        botton_help.place(x=1000, y=695)
        #---------------------------Binding Events--------------------#
        self.V_inicio.bind("w",acelera) ##Acelerador, con tecla W
        self.V_inicio.bind("s",  reverse) ##Freno, con tecla S
        self.V_inicio.bind("<Right>", thread_turn_right)
        self.V_inicio.bind("<Left>",thread_turn_left)
        self.V_inicio.bind("<space>", brake)
        self.V_inicio.bind("<Shift-Right>",dir_lights_right)
        self.V_inicio.bind("<Shift-Left>", thread_dir_izq)
        self.V_inicio.bind("l", enciende_frontales)
        self.V_inicio.bind('b', enciende_traseras)
        self.V_inicio.bind('e', enciende_emergencia)
        self.V_inicio.bind("p", enciende_all_lights)
        self.V_inicio.bind('z',movimiento_especial)
        self.V_inicio.bind('c', celebracion)

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


ventana = Test_Drive(1024, 728)
ventana.__draw__()

