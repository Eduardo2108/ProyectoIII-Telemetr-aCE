from tkinter import *
from threading import Thread
import time
import os
from time import sleep

from WiFiClient import NodeMCU


"""
Clase que dibuja la ventana test drive 

Atributos:
height  = int, alto de ventana
width = int, ancho de ventana

V_test = instancia de Tk()
v_test.tittle = titulo de la ventana
v_test.resizable = configuracion del tamaño  de la ventana

C_test = canvas para dibujar
C_test.place = configuracion del lugar del canvas

****Variables para controlar el carro****
pwm = motor
lf = luces frontales
lb = lucer traseras
ld = direccional derecha
li = direccional izquierda
le = direccionales de emergencia

**** Configuracion del carro ****
myCar = instancia de NodeMCU()
myCar.start = crea conexion

Metodos:

cargarImagen = cargar imagenes mas facilmente

__draw__ dibuja la ventana, con todos los componentes



"""

class Test_Drive:

    def __init__(self, car, team, driver, country):

        #-------------------Settings of window-----------------#
        self.height = 728
        self.width = 1024

        #Window itself
        self.V_test = Toplevel()
        self.V_test.title('Test Drive')
        self.V_test.minsize(self.width, self.height)
        self.V_test.resizable(width=NO, height=NO)

        #Main canvas
        self.C_test = Canvas(self.V_test, width=self.width, height=self.height, bg='#f0f0f0')
        self.C_test.place(x=0, y=0)

        #Configuracion del carro, variables necesarias
        self.pwm = 0

        self.lf = 0
        self.lb = 0
        self.ld = 0
        self.li = 0
        self.le = 0
        self.dir_state = 0
        self.direccion = 0
        #-------------------Datos---------------------#
        self.car = car
        self.driver = driver
        self.country = country
        self.team = team
        # ------------------Instancia del carro-------------------#
        self.myCar = NodeMCU()
        self.myCar.start()
    # Funcion que carga las imagenes a Tkinter

    def cargarImagen(self, nombre):
        ruta = os.path.join("resources", nombre)
        imagen = PhotoImage(file=ruta)
        return imagen
    #Funcion que dibuja en la ventana
    def __draw__(self):
        #Configuraciones del carro
        aceleracion = 100
        #Configuracion del velocimetro
        count = StringVar()
        count.set(0)
        #Configuracion del medidor de bateria
        battery_level = StringVar()
        battery_level.set(0)
        color = 'black'

        #Funcion que aumenta la velocidad
        def acelera(event): #YA ENVIA COMANDOS

            if self.pwm == 1000:
                print("velocidad maxima")
            else:
                self.pwm += aceleracion
                speed.config(text=str(self.pwm))
                msg = 'pwm: ' + str(self.pwm)+ ' ;'
                self.myCar.send(msg)
                cambiaColor()
                print('comando enviado: ', msg)
        #Funcion que disminuye la velocidad y hace reversa
        def reverse(event): #YA ENVIA COMANDOS

            if self.pwm == -800:
                print("reversa maxima")
            else:

                self.pwm-=aceleracion
                speed.config(text=str(self.pwm))
                msg = 'pwm: ' + str(self.pwm)+ ' ;'
                self.myCar.send(msg)
                #print('comando enviado: ', msg)
                cambiaColor()
        #Funcion que enciende direcionales derechas
        def dir_lights_right(): #YA ENVIA COMANDOS

            if self.dir_state == -1:
                self.dir_state = 0
                msg = 'lr: 0;'
                self.myCar.send(msg)
                #print('Comando enviado: ', msg)


            else:

                self.dir_state = 1
                msg = 'lr:1;'
                self.myCar.send(msg)
                #print('Comando enviado: ', msg)
                time.sleep(0.5)

                self.dir_state = 0
                msg = 'lr:0;'
                self.myCar.send(msg)
                #print('Comando enviado: ', msg)
                time.sleep(0.5)

                self.dir_state = 1
                msg = 'lr:1;'
                self.myCar.send(msg)
                #print('Comando enviado: ', msg)
                time.sleep(0.5)

                self.dir_state = 0
                msg = 'lr:0;'
                self.myCar.send(msg)
                #print('Comando enviado: ', msg)

                time.sleep(0.5)

                #print('done')
        #Funcion que enciende direccionales izquierdas
        def dir_lights_left(): #YA ENVIA COMANDOS

            if self.dir_state == 1:
                self.dir_state = 0
            # print('comando direccionales: ',self.dir_state)

            else:

                self.dir_state = -1
                msg = 'll:1;'
                self.myCar.send(msg)
                #print('Comando enviado: ', msg)
                time.sleep(0.5)

                self.dir_state = 0
                msg = 'll:0;'
                self.myCar.send(msg)
                #print('Comando enviado: ', msg)
                time.sleep(0.5)

                self.dir_state = -1
                msg = 'll:1;'
                self.myCar.send(msg)
                #print('Comando enviado: ', msg)
                time.sleep(0.5)

                self.dir_state = 0
                msg = 'll:0;'
                self.myCar.send(msg)
                #print('Comando enviado: ', msg)



                time.sleep(0.5)


                #print('done')
        #Funcion que gira a la derecha
        def gira_derecha():
            if self.direccion == 0:
                self.direccion = 1
                dir_lights_right()
                msg = 'dir:1;'
                self.myCar.send(msg)
                print('Comando giro enviado: ', msg)
                time.sleep(2)
            else:
                self.direccion=0
                msg = 'dir:0;'
                self.myCar.send(msg)
                print('Comando giro enviado: ', msg)
        #Funcion que gira a la izquierda
        def gira_izquierda():
            if self.direccion == 0:
                self.direccion = -1
                dir_lights_left()
                msg = 'dir:-1;'
                self.myCar.send(msg)
                print('Comando giro enviado: ', msg)
                time.sleep(2)
            else:
                self.direccion = 0
                msg = 'dir:0;'
                self.myCar.send(msg)
                print('Comando giro enviado: ', msg)
            #msg = 'dir:0;'
            #self.myCar.send(msg)
            #print('Comando giro enviado: ', msg)
        #Funcion que frena el carro
        def brake(event):
            if self.pwm > 0:
                self.pwm -= 50
                speed.config(text=str(self.pwm))
                print(count)
                msg = 'pwm: ' + str(self.pwm)+ ' ;'
                self.myCar.send(msg)
                print('comando enviado: ', msg)
                cambiaColor()
            elif self.pwm <0:
                self.pwm +=50
                speed.config(text=str(self.pwm))
                self.myCar.send(msg)
                print('comando enviado: ', msg)
                cambiaColor()

        #===================Celebracion==============#
        #enciende y apaga las luces de emergencia, a manera de burla a los perdedores
        def celebracion(event):
            pass
           #--------------------Boton Update bateria---------------------#

        #Funcion que enciende luces frontales
        def enciende_frontales(event):
            if self.lf == 0:
                self.myCar.send('lf:1;')
                print('Comando enviado: ', 'lf:1;')
                self.lf = 1
            else:
                self.myCar.send('lf:0;')
                print('Comando enviado: ', 'lf:0;')
                self.lf = 0
        #Funicion que enciende luces traseras
        def enciende_traseras(event):
            if self.lb == 0:
                self.myCar.send('lb:1;')
                print('Comando enviado: ', 'lb:1;')
                self.lb = 1
            else:
                self.myCar.send('lb:0;')
                print('Comando enviado: ', 'lb:0;')
                self.lb = 0
        #Funcion que enciende luces de emergencia
        def enciende_emergencia(event):
            if self.le == 0:
                self.myCar.send('le:1;')
                self.le = 1
            else:
                self.myCar.send('le:0;')
                self.le = 0
        #Funcion que lee la bateria

        def read_battery():

            while True:
                level = self.myCar.send("sense;")
                #print(self.myCar.read())
                time.sleep(2)
                bat = self.myCar.read()
                battery_level.set(bat)

        marcaAuto = Label(self.C_test, text='Model: ' + str(self.car), font=("Arial ", 20), justify=CENTER)
        marcaAuto.place(x=0,y=10)
        #Etiqueta conductor.
        Nombre = Label(self.C_test, text ="Driver: " + str(self.driver), font=("Arial", 20), width = 15, justify= LEFT)
        Nombre.place(x=-25, y= 50)
        #Etiqueta pais
        Country = Label(self.C_test, text= str(self.country), font=('Arial', 20), justify=CENTER)
        Country.place(x=220, y= 50)
        #Etiqueta del equipo
        Team = Label(self.C_test, text ='Team: ' + str(self.team), font=('Arial', 20), justify=CENTER)
        Team.place(x=0, y =90)


        #---|------------------------|
        #   |  COMANDOS DEL CARRO    |
        #---|------------------------|

        #---------------Volante con medidor velocidad----------------#
        steer_image = self.cargarImagen('bg.png')
        #print("Working directory: ", os.getcwd())
        #self.C_test.create_image(0, 450, anchor=NW, image=steer_image)
        #print(steer_image)
        steer = Label(self.C_test, image = steer_image)
        steer.image = steer_image
        steer.place(x=0,y=450)


        #-----------------Indicador velocidad------------------------#
        speed = Label(self.C_test, text='0', font=('Unispace', 45), fg=color)
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

        thread = Thread(target=read_battery, args=())
        thread.start()
        #---------------------------Binding Events--------------------#
        self.V_test.bind("w", acelera) ##Acelerador, con tecla W
        self.V_test.bind("s", reverse) ##Freno, con tecla S
        self.V_test.bind("<Right>", thread_turn_right)
        self.V_test.bind("<Left>", thread_turn_left)
        self.V_test.bind("<space>", brake)
        self.V_test.bind("<Shift-Right>", thread_dir_der)
        self.V_test.bind("<Shift-Left>", thread_dir_izq)
        self.V_test.bind("l", enciende_frontales)
        self.V_test.bind('b', enciende_traseras)
        self.V_test.bind('e', enciende_emergencia)
        self.V_test.bind('c', celebracion)

        self.V_test.mainloop()


#test_drive = Test_Drive('auto', 'conductor', 'pais', 'equipo')
#test_drive.__draw__()




