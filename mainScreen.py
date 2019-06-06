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
__draw__ >>> funcion que dibuja todo lo necesario para la pantalla de pruebas

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



class Test_Drive:

    def __init__(self):

        #-------------------Settings of window-----------------#
        self.height = 728
        self.width = 1024

        #Window itself
        self.V_test = Tk()
        self.V_test.title('Formula CE')
        self.V_test.minsize(self.width, self.height)
        self.V_test.resizable(width=NO, height=NO)

        #Main canvas
        self.C_test = Canvas(self.V_test, width=self.width, height=self.height, bg='#f0f0f0')
        self.C_test.place(x=0, y=0)

        #Configuracion del carro, variables necesarias
        self.pwm = 0
        self.dir_state = 0
        self.lf = 0
        self.lb = 0
        self.ld = 0

    def cargarImagen(self, nombre):
        ruta = os.path.join('resources', nombre)
        imagen = PhotoImage(file=ruta)
        return imagen

    def __draw__(self, car, driver, country, team):
        aceleracion = 100
        count = StringVar()
        count.set(0)

        battery_level = StringVar()
        battery_level.set(100)
        color = 'black'

        dir_state = 0 #variable que guarda estado de direccionales

        # <--- | ^  |  --->
        #  -1  | 0  |  1

        #YA ENVIAA
        def acelera(event): #YA ENVIA COMANDOS

            if self.pwm == 1000:
                print("velocidad maxima")
            else:
                self.pwm += aceleracion
                count.set(self.pwm)
                msg = 'pwm: ' + str(self.pwm)+ ' ;'
                myCar.send(msg)
                cambiaColor()
                print('comando enviado: ', msg)
        #YA ENVIA
        def reverse(event): #YA ENVIA COMANDOS

            if self.pwm == -600:
                print("reversa maxima")
            else:

                self.pwm-=aceleracion
                count.set(self.pwm)
                msg = 'pwm: ' + str(self.pwm)+ ' ;'
                myCar.send(msg)
                print('comando enviado: ', msg)
                cambiaColor()
        #YA ENIVIA
        def dir_lights_right(): #YA ENVIA COMANDOS

            if self.dir_state == -1:
                self.dir_state = 0
                msg = 'lr: 0;'
                myCar.send(msg)
                print('Comando enviado: ', msg)


            else:

                self.dir_state = 1
                msg = 'lr:1;'
                myCar.send(msg)
                print('Comando enviado: ', msg)
                time.sleep(0.5)

                self.dir_state = 0
                msg = 'lr:0;'
                myCar.send(msg)
                print('Comando enviado: ', msg)
                time.sleep(0.5)

                self.dir_state = 1
                msg = 'lr:1;'
                myCar.send(msg)
                print('Comando enviado: ', msg)
                time.sleep(0.5)

                self.dir_state = 0
                msg = 'lr:0;'
                myCar.send(msg)
                print('Comando enviado: ', msg)

                time.sleep(0.5)

                print('done')
        #YA ENVIA
        def dir_lights_left(): #YA ENVIA COMANDOS

            if self.dir_state == 1:
                self.dir_state = 0
                print('comando direccionales: ',self.dir_state)

            else:

                self.dir_state = -1
                msg = 'll:1;'
                myCar.send(msg)
                print('Comando enviado: ', msg)
                time.sleep(0.5)

                self.dir_state = 0
                msg = 'll:0;'
                myCar.send(msg)
                print('Comando enviado: ', msg)
                time.sleep(0.5)

                self.dir_state = -1
                msg = 'll:1;'
                myCar.send(msg)
                print('Comando enviado: ', msg)
                time.sleep(0.5)

                self.dir_state = 0
                msg = 'll:0;'
                myCar.send(msg)
                print('Comando enviado: ', msg)



                time.sleep(0.5)


                print('done')
        #YA ENVIA
        def gira_derecha():
            turn = 1
            msg = 'dir:1;'
            myCar.send(msg)
            print('Comando giro enviado: ',msg)

            dir_lights_right()
            msg = 'dir:0;'
            myCar.send(msg)
            print('Comando giro enviado: ', msg)

            turn = 0
        #YA ENVIA
        def gira_izquierda():

            turn = -1
            msg = 'dir:-1;'
            myCar.send(msg)
            print('Comando giro enviado: ', msg)

            dir_lights_left()
            msg = 'dir:0;'
            myCar.send(msg)
            print('Comando giro enviado: ', msg)

            turn = 0
        #YA ENVIA
        def brake(event):
            if self.pwm > 0:
                self.pwm -= 50
                count.set(self.pwm)
                msg = 'pwm: ' + str(self.pwm)+ ' ;'
                myCar.send(msg)
                print('comando enviado: ', msg)
                cambiaColor()
            elif self.pwm <0:
                self.pwm +=50
                count.set(self.pwm)
                msg = 'pwm: ' + str(self.pwm)+ ' ;'
                myCar.send(msg)
                print('comando enviado: ', msg)
                cambiaColor()
        #====================FALTA DEFINIR=============#
        def movimiento_especial(event):
            print("Envia movimiento especial...")
        #====================FALTA DEFINIR=============#
        def celebracion(event):
            print("Envia celebracion...")

        #YA ENVIA
        def enciende_frontales(event):
            if self.lf == 0:
                myCar.send('lf:1;')
                print('Comando enviado: ', 'lf:1;')
                self.lf = 1
            else:
                myCar.send('lf:0;')
                print('Comando enviado: ', 'lf:0;')
                self.lf = 0
        #YA ENVIA
        def enciende_traseras(event):
            if self.lb == 0:
                myCar.send('lb:1;')
                print('Comando enviado: ', 'lb:1;')
                self.lb = 1
            else:
                myCar.send('lb:0;')
                print('Comando enviado: ', 'lb:0;')
                self.lb = 0
        #YA ENVIA
        def enciende_emergencia(event):
            if self.ld == 0:
                myCar.send('ll:1;')
                myCar.send('lr:1;')
                print('Comando enviado: ', 'lf:1;', 'lr:1;')
                self.ld = 1
            else:
                myCar.send('ll:0;')
                myCar.send('lr:0;')
                print('Comando enviado: ', 'll:0;', 'lr:0;')
                self.ld = 0
        #YA ENVIA
        def enciende_all_lights(event):
            enciende_frontales(event)
            enciende_traseras(event)
            enciende_emergencia(event)
            print('enciende todas las luces.....')

        def read_battery():

            level = myCar.readById('blvl')
            battery_level.set(level)
            print('Bateria actualizada..')

        #Etiquetas de informacion, carro, piloto...
        #Etiqueta del modelo del carro.
        marcaAuto = Label(self.C_test, text='Model: ' + str(car), font=("Arial ", 20), justify=CENTER)
        marcaAuto.place(x=0,y=10)
        #Etiqueta conductor.
        Nombre = Label(self.C_test, text ="Driver: " + str(driver), font=("Arial", 20), width = 15, justify= LEFT)
        Nombre.place(x=-25, y= 50)
        #Etiqueta pais
        Country = Label(self.C_test, text= str(country), font=('Arial', 20), justify=CENTER)
        Country.place(x=220, y= 50)
        #Etiqueta del equipo
        Team = Label(self.C_test, text ='Team: ' + str(team), font=('Arial', 20), justify=CENTER)
        Team.place(x=0, y =90)


        #---|------------------------|
        #   |  COMANDOS DEL CARRO    |
        #---|------------------------|

        #---------------Volante con medidor velocidad----------------#
        steer_image = self.cargarImagen('bg.png')
        steer = Label(self.C_test, image = steer_image)
        steer.image = steer_image
        steer.place(x=0,y=450)


        #-----------------Indicador velocidad------------------------#
        speed = Label(self.C_test, textvariable=count, font=('Unispace', 45), fg=color)
        speed.place(x=490,y=570)

        #--------------------Indicador de bateria--------------------#
        mark_battery = Label(self.C_test, text=' Battery Level: ', font=('Arial', 20))
        bat_level = Label(self.C_test, textvariable= (battery_level), font=('Unispace', 20))
        bat_level.place(x=940,y=0)
        mark_battery.place(x=750,y=0)

        #------------------Boton ayuda--------------------------------#
        def ayuda():
            Ayuda = Canvas(self.V_test, width = 400, height=600, bg='white')
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
        botton_help = Button(self.C_test, bitmap='question', relief = FLAT, command= ayuda)
        botton_help.place(x=990, y=695)
        #--------------------Boton Update bateria---------------------#
        refresh = Button(self.C_test, bitmap ='warning', command= read_battery)
        refresh.place(x=1010,y=5)
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

        #---------------------------Binding Events--------------------#
        self.V_test.bind("w", acelera) ##Acelerador, con tecla W
        self.V_test.bind("s", reverse) ##Freno, con tecla S
        self.V_test.bind("<Right>", thread_turn_right)
        self.V_test.bind("<Left>", thread_turn_left)
        self.V_test.bind("<space>", brake)
        self.V_test.bind("<Shift-Right>", dir_lights_right)
        self.V_test.bind("<Shift-Left>", thread_dir_izq)
        self.V_test.bind("l", enciende_frontales)
        self.V_test.bind('b', enciende_traseras)
        self.V_test.bind('e', enciende_emergencia)
        self.V_test.bind("a", enciende_all_lights)
        self.V_test.bind('z', movimiento_especial)
        self.V_test.bind('c', celebracion)


        self.V_test.mainloop()



ventana = Test_Drive()
ventana.__draw__('Ferrari 458', 'Eduardo', 'CRC', 'Red Bull')

