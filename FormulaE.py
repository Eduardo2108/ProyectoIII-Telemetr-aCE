"""  ______________________________________________________________________________________________________________ """
''' / Instituto Tecnologico de Costa Rica                                                                          \ '''
''' \ Parte 2:  Formula E CE TEC                                                                                   / '''
''' / Estudiantes: Jose Andres Rodriguez Rojas (2019279722)                                                        \ '''
''' \              Eduardo Zumbado Granados    (2019003973)                                                        / '''
''' / Curso: Taller de programacion                                                                                \ '''
''' \ I Semestre 2019                                                                                              / '''
''' / Profesor: Jeff Schmidt Peralta                                                                               \ '''
""" \______________________________________________________________________________________________________________/ """

"""******************************************************************************************************************"""
'''*************************************             LIBRERIAS          *********************************************'''
'''******************************************************************************************************************'''

from tkinter import *
from tkinter import messagebox
import sys
from TestScreen import Test_Drive

'''******************************************************************************************************************'''
'''***************************************             METODOS          *********************************************'''
'''******************************************************************************************************************'''


# Metodo independiente: Carga una el logo de la escuderia dada.
def cargar_logo(escuderia):
    imagen = PhotoImage(file='Escuderias/' + escuderia + "/Logo.PNG")
    imagen_reducida = imagen.subsample(x=7, y=7)
    return imagen_reducida


# Metodo independiente: Carga una imagen.
def cargar_imagen(nombre):
    imagen = PhotoImage(file='Images/' + nombre)
    imagen_reducida = imagen.subsample(x=7, y=7)
    return imagen_reducida


# Metodo independiente: Mustra la ventana de informacion de desarrollador con sus datos correspondientes y oculta las
# demas ventanas.
def mostrar_ventanaabout():
    ventanabout.deiconify()
    ventanaprincipal.iconify()

    desarrollador1.delete(0, END)
    desarrollador2.delete(0, END)

    lbldesarollador1 = Label(ventanabout, text="Desarollador:", font=("Courier", 14))
    lbldesarollador1.place(x=20, y=10)
    lbldesarollador2 = Label(ventanabout, text="Desarollador:", font=("Courier", 14))
    lbldesarollador2.place(x=20, y=220)
    lblinfo_software = Label(ventanabout, text="Informacion del software:", font=("Courier", 14))
    lblinfo_software.place(x=20, y=440)

    lblinfo1 = Label(ventanabout, text="Pais de desarrollo: Costa Rica", font=("Courier", 12))
    lblinfo1.place(x=40, y=470)
    lblinfo2 = Label(ventanabout, text="Version del programa: v0.0.1000000", font=("Courier", 12))
    lblinfo2.place(x=40, y=490)
    lblinfo3 = Label(ventanabout, text="Funcional en Python 3.7", font=("Courier", 12))
    lblinfo3.place(x=40, y=510)
    lblinfo4 = Label(ventanabout, text="Marca registrada ®", font=("Courier", 12))
    lblinfo4.place(x=40, y=530)

    imagen_des2 = cargar_imagen("Desarrollador2.GIF")
    canvasabout.create_image((550, 260), image=imagen_des2, anchor=NW)

    imagen_des1 = cargar_imagen("Desarrollador1.GIF")
    canvasabout.create_image((550, 50), image=imagen_des1, anchor=NW)

    desarrollador1.insert(END, " Nombre: Eduardo Zumbado Granados", " Carne: 2019003973",
                          " Institucion: Tecnologico de Costa Rica", " Carrera: Ingenieria en computadores",
                          " Curso: Taller de programacion",
                          " Grupo: 1", " Profesor: Jeff Schmidt Prealta")
    desarrollador2.insert(END, " Nombre: Jose Andres Rodriguez Rojas", " Carne: 2019279722",
                          " Institucion: Tecnologico de Costa Rica", " Carrera: Ingenieria en computadores",
                          " Curso: Taller de programacion",
                          " Grupo: 1", " Profesor: Jeff Schmidt Peralta")
    volver = Button(ventanabout, text="Volver", command=lambda: main(), bg="White", font=("Courier", 12))
    volver.place(x=610, y=525)
    ventanabout.mainloop()


# Metodo independiente: Mustra la ventana de informacion de escuderia con sus datos correspondientes y oculta las
# # demas ventanas.
def mostrar_ventanaescuderia(escuderia):
    ventanaprincipal.iconify()
    ventananuevoauto.iconify()
    ventanatestdrive.iconify()
    ventanaescuderia.deiconify()
    info = leerDatosEscuderia(escuderia)
    canvasescuderia.create_rectangle(10, 20, 950, 120)
    lblinfo = Label(ventanaescuderia, text="Informacion de la escuderia", font=("Courier", 10))
    lblinfo.place(x=20, y=10)
    lblesp1 = Label(ventanaescuderia,
                    text="                                                                                      ",
                    font=("Courier", 10))
    lblesp1.place(x=20, y=35)
    lblnombre = Label(ventanaescuderia, text="Nombre de la escuderia: " + info[0], font=("Courier", 11))
    lblnombre.place(x=20, y=35)
    lblesp2 = Label(ventanaescuderia,
                    text="                                                                                      ",
                    font=("Courier", 10))
    lblesp2.place(x=20, y=65)
    lblubicacion = Label(ventanaescuderia, text="Ubicacion de la escuderia: " + info[1], font=("Courier", 11))
    lblubicacion.place(x=20, y=65)
    lblesp3 = Label(ventanaescuderia,
                    text="                                                                                      ",
                    font=("Courier", 10))
    lblesp3.place(x=20, y=95)
    lblpatrocinadores = Label(ventanaescuderia, text="Patrocinadores de la escuderia: " + info[2],
                              font=("Courier", 11))
    lblpatrocinadores.place(x=20, y=95)
    logo = cargar_logo(escuderia)
    canvasescuderia.create_rectangle((720, 25, 900, 115), fill='White')
    canvasescuderia.create_image((725, 25), anchor=NW, image=logo)

    lblautos = Label(ventanaescuderia, text="Autos", font=("Courier", 24))
    lblautos.place(x=30, y=150)
    lblpilotos = Label(ventanaescuderia, text="Pilotos", font=("Courier", 24))
    lblpilotos.place(x=430, y=150)
    lblorden1 = Label(ventanaescuderia, text="Orden", font=("Courier", 14))
    lblorden1.place(x=190, y=145)
    lblorden2 = Label(ventanaescuderia, text="Orden", font=("Courier", 14))
    lblorden2.place(x=590, y=145)

    la = leerAutosEscuderia(escuderia)
    lp = leerPilotosEscuderia(escuderia)

    la.ordenar("A")
    lp.ordenar("A", "RGP")

    la.mostrar()
    lp.mostrar()

    asc_autos = Button(ventanaescuderia, text="Ascendente", command=lambda: [la.ordenar("A"), la.mostrar()], bg="White",
                       font=("Courier", 8))
    asc_autos.place(x=270, y=130)
    desc_autos = Button(ventanaescuderia, text="Descendente", command=lambda: [la.ordenar("D"), la.mostrar()],
                        bg="White", font=("Courier", 8))
    desc_autos.place(x=270, y=165)

    asc_RGP_pilotos = Button(ventanaescuderia, text="Ascendente por RGP",
                             command=lambda: [lp.ordenar("A", "RGP"), lp.mostrar()], bg="White", font=("Courier", 8))
    asc_RGP_pilotos.place(x=670, y=130)
    asc_REP_pilotos = Button(ventanaescuderia, text="Ascendente por REP",
                             command=lambda: [lp.ordenar("A", "REP"), lp.mostrar()], bg="White", font=("Courier", 8))
    asc_REP_pilotos.place(x=670, y=165)
    desc_RGP_pilotos = Button(ventanaescuderia, text="Descendente por RGP",
                              command=lambda: [lp.ordenar("D", "RGP"), lp.mostrar()], bg="White", font=("Courier", 8))
    desc_RGP_pilotos.place(x=815, y=130)
    desc_REP_pilotos = Button(ventanaescuderia, text="Descendente por REP",
                              command=lambda: [lp.ordenar("D", "REP"), lp.mostrar()], bg="White", font=("Courier", 8))
    desc_REP_pilotos.place(x=815, y=165)

    testdrive = Button(ventanaescuderia, text="Test drive", command=lambda: mostrar_ventanatestdrive(escuderia),
                       bg="White", font=("Courier", 12))
    testdrive.place(x=850, y=410)

    agregarauto = Button(ventanaescuderia, text="Agregar\nauto", command=lambda: mostrar_ventanaagregarauto(escuderia),
                         bg="White", font=("Courier", 12))
    agregarauto.place(x=850, y=460)

    volver = Button(ventanaescuderia, text="Volver", command=lambda: main(), bg="White", font=("Courier", 12))
    volver.place(x=850, y=530)

    salir = Button(ventanaescuderia, text="Salir", command=lambda: sys.exit(), bg="White", font=("Courier", 12))
    salir.place(x=850, y=580)

    ventanaprincipal.mainloop()
    ventanaescuderia.mainloop()


# Metodo independiente:  Mustra la ventana de captura de informacion para el "Test drive"  y oculta las
# demas ventanas.
def mostrar_ventanatestdrive(escuderia):

    def show_td(car, driver, coun, team):

        ventanaescuderia.iconify()
        test_drive = Test_Drive(car,team,driver,coun)

        #img = test_drive.cargarImagen('bg.png')
        #label = Label(test_drive.C_test,image = img)
        #label.place(0,450)

        test_drive.__draw__()

    ventanaescuderia.iconify()
    ventanatestdrive.deiconify()
    lblintro = Label(ventanatestdrive,
                     text="Inroduzca los datos del auto a conducir,\nuna vez llenados presione el boton 'Iniciar'",
                     font=("Courier", 10), justify=LEFT)
    lblintro.place(x=10, y=10)
    lblescuderia = Label(ventanatestdrive, text="Escuderia:", font=("Courier", 10))
    lblescuderia.place(x=10, y=60)
    team = Entry(ventanatestdrive, font=("Courier", 10), width=25)
    team.insert(END, str(escuderia))
    team.config(state=DISABLED)
    team.place(x=10, y=85)
    lblconductor = Label(ventanatestdrive, text="Conductor:", font=("Courier", 10))
    lblconductor.place(x=10, y=120)
    conductor = Entry(ventanatestdrive, font=("Courier", 10), width=25)
    conductor.place(x=10, y=145)
    lblnacionalidad = Label(ventanatestdrive, text="Nacionalidad:", font=("Courier", 10))
    lblnacionalidad.place(x=10, y=180)
    nacionalidad = Entry(ventanatestdrive, font=("Courier", 10), width=25)
    nacionalidad.place(x=10, y=205)
    lblauto = Label(ventanatestdrive, text="Auto:", font=("Courier", 10))
    lblauto.place(x=10, y=240)
    auto = Entry(ventanatestdrive, font=("Courier", 10), width=25)
    auto.place(x=10, y=265)

    carro = auto.get()
    piloto = conductor.get()
    country = nacionalidad.get()

    iniciar = Button(ventanatestdrive, text="Iniciar", bg="White", font=("Courier", 11), command=lambda:show_td(auto.get(),conductor.get(),nacionalidad.get(),escuderia))
    iniciar.place(x=250, y=300)



    volver = Button(ventanatestdrive, text="Volver", command=lambda: mostrar_ventanaescuderia(escuderia), bg="White",
                    font=("Courier", 11))

    volver.place(x=10, y=300)
    ventanatestdrive.mainloop()


# Metodo independiente:  Mustra la ventana de agregar un nuevo auto y oculta las demas ventanas.
def mostrar_ventanaagregarauto(escuderia):
    ventanaescuderia.iconify()
    ventananuevoauto.deiconify()
    lblintro = Label(ventananuevoauto,
                     text="Inroduzca los datos del auto a ingresar, una vez llenados\npresione el boton 'Agregar auto'",
                     font=("Courier", 10), justify=LEFT)
    lblintro.place(x=10, y=10)
    lblmarca = Label(ventananuevoauto, text="Marca:", font=("Courier", 10))
    lblmarca.place(x=10, y=60)
    marca = Entry(ventananuevoauto, font=("Courier", 10), width=25)
    marca.insert(END, str(escuderia))
    marca.config(state=DISABLED)
    marca.place(x=10, y=85)
    lblmodelo = Label(ventananuevoauto, text="Modelo:", font=("Courier", 10))
    lblmodelo.place(x=10, y=120)
    modelo = Entry(ventananuevoauto, font=("Courier", 10), width=25)
    modelo.place(x=10, y=145)
    lblpaisfabric = Label(ventananuevoauto, text="Pais de fabricacion:", font=("Courier", 10))
    lblpaisfabric.place(x=10, y=180)
    paisfabric = Entry(ventananuevoauto, font=("Courier", 10), width=25)
    paisfabric.place(x=10, y=205)
    lbltemporada = Label(ventananuevoauto, text="Temporada:", font=("Courier", 10))
    lbltemporada.place(x=10, y=240)
    temporada = Entry(ventananuevoauto, font=("Courier", 10), width=25)
    temporada.place(x=10, y=265)
    lblcantbaterias = Label(ventananuevoauto, text="Cantidad de baterias:", font=("Courier", 10))
    lblcantbaterias.place(x=10, y=300)
    cantbaterias = Entry(ventananuevoauto, font=("Courier", 10), width=25)
    cantbaterias.place(x=10, y=325)
    lbltensionxbateria = Label(ventananuevoauto, text="Tension por bateria:", font=("Courier", 10))
    lbltensionxbateria.place(x=275, y=60)
    tensionxbateria = Entry(ventananuevoauto, font=("Courier", 10), width=25)
    tensionxbateria.place(x=275, y=85)
    lblpilasxbateria = Label(ventananuevoauto, text="Pilas por bateria:", font=("Courier", 10))
    lblpilasxbateria.place(x=10, y=360)
    pilasxbateria = Entry(ventananuevoauto, font=("Courier", 10), width=25)
    pilasxbateria.place(x=10, y=385)

    lblestado = Label(ventananuevoauto, text="Estado:", font=("Courier", 10))
    lblestado.place(x=275, y=120)
    estado = Entry(ventananuevoauto, font=("Courier", 10), width=25)
    estado.place(x=275, y=145)
    lblconsumotores = Label(ventananuevoauto, text="Consumo de motores:", font=("Courier", 10))
    lblconsumotores.place(x=275, y=180)
    consumotores = Entry(ventananuevoauto, font=("Courier", 10), width=25)
    consumotores.place(x=275, y=205)
    lblsensores = Label(ventananuevoauto, text="Sensores:", font=("Courier", 10))
    lblsensores.place(x=275, y=240)
    sensores = Entry(ventananuevoauto, font=("Courier", 10), width=25)
    sensores.place(x=275, y=265)
    lblpeso = Label(ventananuevoauto, text="Peso:", font=("Courier", 10))
    lblpeso.place(x=275, y=300)
    peso = Entry(ventananuevoauto, font=("Courier", 10), width=25)
    peso.place(x=275, y=325)
    lbleficiencia = Label(ventananuevoauto, text="Eficiencia:", font=("Courier", 10))
    lbleficiencia.place(x=275, y=360)
    eficiencia = Entry(ventananuevoauto, font=("Courier", 10), width=25)
    eficiencia.place(x=275, y=385)

    agregarauto = Button(ventananuevoauto, text="Agregar\nauto",
                         command=lambda: escribirnuevoauto(escuderia, str(marca.get()), str(modelo.get()),
                                                           str(paisfabric.get()), str(temporada.get()),
                                                           str(cantbaterias.get()), str(pilasxbateria.get()),
                                                           str(tensionxbateria.get()), str(estado.get()),
                                                           str(consumotores.get()), str(sensores.get()),
                                                           str(peso.get()), int(eficiencia.get())), bg="White",
                         font=("Courier", 11))
    agregarauto.place(x=400, y=420)

    volver = Button(ventananuevoauto, text="Volver", command=lambda: mostrar_ventanaescuderia(escuderia), bg="White",
                    font=("Courier", 11))
    volver.place(x=10, y=435)
    ventananuevoauto.mainloop()


# Metodo independiente: Metodo que recibe informacion del metodo "mostrar_ventanaagregarauto" y escribe en el archivo
# de texto la informacion del auto a ingresar
def escribirnuevoauto(escuderia, marca, modelo, paisfabric, temporada, cantbaterias, pilasxbateria, tensionxbateria,
                      estado, consumotores, sensores, peso, eficiencia):
    if isinstance(marca, str) and isinstance(modelo, str) and isinstance(paisfabric, str) and isinstance(temporada,
                                                                                                         str) and isinstance(
        cantbaterias, str) and isinstance(pilasxbateria, str) and isinstance(tensionxbateria, str) and isinstance(
        estado, str) and isinstance(consumotores, str) and isinstance(sensores, str) and isinstance(peso,
                                                                                                    str) and isinstance(
        int(eficiencia),
        int) and marca != '' and modelo != '' and paisfabric != '' and temporada != '' and cantbaterias != '' and pilasxbateria != '' and tensionxbateria != '' and estado != '' and consumotores != '' and sensores != '' and peso != '':
        auto = '\n{Marca: "' + marca + '", Modelo: "' + modelo + '", Pais de fabricacion: "' + paisfabric + '", Foto: "Default.PNG", Anio de temporada: "' + temporada + '", Cantidad de baterias: "' + cantbaterias + '", Pilas por bateria: "' + pilasxbateria + '", Tension por bateria: "' + tensionxbateria + '", Estado: "' + estado + '", Consumo de motores: "' + consumotores + '", Sensores: "' + sensores + '", Peso: "' + peso + '", Eficiencia: "' + str(
            eficiencia) + '"}'
        archivo = open('./Escuderias/' + escuderia + "/Autos.txt", "r")
        datosanteriores = archivo.read()
        archivo.close()
        archivo = open('./Escuderias/' + escuderia + "/Autos.txt", "w")
        archivo.write(datosanteriores + auto)
        archivo.close()
        messagebox.showinfo("Que elegancia la de Francia", "Auto ingresado exitosamente.")
        mostrar_ventanaescuderia(escuderia)
    else:
        messagebox.showinfo("Suave un toque",
                            "Alguno de los datos fue ingresado incorrectamente, por favor intentelo de nuevo")


# Metodo independiente: Metodo que lee el archivo  "Datos.txt", correspondiente al de cada escuderia y retorna su
# nombre, ubicacion y patrocinadores
def leerDatosEscuderia(escuderia):
    archivo = open('./Escuderias/' + escuderia + "/Datos.txt", "r")
    datos = archivo.read()
    archivo.close()

    nombre = ""
    ubicacion = ""
    patrocinadores = ""

    contador = 0
    index = 1

    while datos[index] != '}':
        if datos[index] == '"':
            index += 1
            while datos[index] != '"':
                if contador == 0:
                    nombre += str(datos[index])
                elif contador == 1:
                    ubicacion += str(datos[index])
                else:
                    patrocinadores += str(datos[index])
                index += 1
            contador += 1
        index += 1

    info = [nombre, ubicacion, patrocinadores]
    return info


# Metodo independiente: Metodo que lee el archivo "Autos.txt" de la escuderia correspondiente y crea un nuevo Auto(nodo)
# con la informacion leida.
def leerAutosEscuderia(escuderia):
    archivo = open('./Escuderias/' + escuderia + "/Autos.txt", "r")
    datos = archivo.read()
    archivo.close()

    la = Lista_autos()
    index = 1

    while index < len(datos) - 1:
        contador = 0
        marca = ""
        modelo = ""
        paisfabric = ""
        foto = ""
        aniotemp = ""
        cantbaterias = ""
        pilasxbateria = ""
        tensionxbateria = ""
        estado = ""
        consumotores = ""
        sensores = ""
        peso = ""
        eficiencia = ""
        while datos[index] != '}':
            if datos[index] == '"':
                index += 1
                while datos[index] != '"':
                    if contador == 0:
                        marca += str(datos[index])
                    elif contador == 1:
                        modelo += str(datos[index])
                    elif contador == 2:
                        paisfabric += str(datos[index])
                    elif contador == 3:
                        foto += str(datos[index])
                    elif contador == 4:
                        aniotemp += str(datos[index])
                    elif contador == 5:
                        cantbaterias += str(datos[index])
                    elif contador == 6:
                        pilasxbateria += str(datos[index])
                    elif contador == 7:
                        tensionxbateria += str(datos[index])
                    elif contador == 8:
                        estado += str(datos[index])
                    elif contador == 9:
                        consumotores += str(datos[index])
                    elif contador == 10:
                        sensores += str(datos[index])
                    elif contador == 11:
                        peso += str(datos[index])
                    else:
                        eficiencia += str(datos[index])
                    index += 1
                contador += 1
            index += 1
        la.agregar_auto(marca, modelo, paisfabric, foto, aniotemp, cantbaterias, pilasxbateria, tensionxbateria,
                        estado, consumotores, sensores, peso, eficiencia)
        if datos[index] == '}':
            index += 1
    return la


# Metodo independiente: Metodo que lee el archivo "Pilotos.txt" de la escuderia correspondiente y crea un nuevo
# Piloto(nodo) con la informacion leida.
def leerPilotosEscuderia(escuderia):
    archivo = open('./Escuderias/' + escuderia + "/Pilotos.txt", "r")
    datos = archivo.read()
    archivo.close()

    lp = Lista_pilotos()
    index = 1

    while index < len(datos) - 1:
        contador = 0
        nombre = ""
        edad = ""
        nacionalidad = ""
        aniotemp = ""
        competparticip = ""
        participdestacadas = ""
        participfallidas = ""
        victorias = ""
        while datos[index] != '}':
            if datos[index] == '"':
                index += 1
                while datos[index] != '"':
                    if contador == 0:
                        nombre += str(datos[index])
                    elif contador == 1:
                        edad += str(datos[index])
                    elif contador == 2:
                        nacionalidad += str(datos[index])
                    elif contador == 3:
                        aniotemp += str(datos[index])
                    elif contador == 4:
                        competparticip += str(datos[index])
                    elif contador == 5:
                        participdestacadas += str(datos[index])
                    elif contador == 6:
                        participfallidas += str(datos[index])
                    else:
                        victorias += str(datos[index])
                    index += 1
                contador += 1
            index += 1
        lp.agregar_piloto(nombre, edad, nacionalidad, aniotemp, competparticip, participdestacadas, participfallidas,
                          victorias)
        if datos[index] == '}':
            index += 1
    return lp


'''******************************************************************************************************************'''
'''***************************************             CLASES          **********************************************'''
'''******************************************************************************************************************'''

# Clase: Declaracion de la clase Piloto que funciona a razon de nodo de la clase Lista_pilotos
class Piloto:
    # Metodo de clase Piloto: Metodo que inicializa cada instanciacion de esta clase
    def __init__(self, nombre, edad, nacionalidad, aniotemp, competparticip, participdestacadas, participfallidas,
                 victorias):
        self.next = None
        self.prev = None
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.aniotemp = aniotemp
        self.competparticip = competparticip
        self.participdestacadas = participdestacadas
        self.participfallidas = participfallidas
        self.victorias = victorias
        self.rend_global = ((int(victorias) + int(participdestacadas)) / (
                int(competparticip) - int(participfallidas))) * 100
        self.rend_especifico = (int(victorias) / (int(competparticip) - int(participfallidas))) * 100
        self.pos = 0


# Clase: Declaracion de la clase Auto que funciona a razon de nodo de la clase Lista_autos
class Auto:
    # Metodo de clase Auto: Metodo que inicializa cada instanciacion de esta clase
    def __init__(self, marca, modelo, paisfabric, foto, aniotemp, cantbaterias, pilasxbateria, tensionxbateria,
                 estado, consumotores, sensores, peso, eficiencia):
        self.next = None
        self.prev = None
        self.marca = marca
        self.modelo = modelo
        self.paisfabric = paisfabric
        self.foto = foto
        self.aniotemp = aniotemp
        self.cantbaterias = cantbaterias
        self.pilasxbateria = pilasxbateria
        self.tensionxbateria = tensionxbateria
        self.estado = estado
        self.consumotores = consumotores
        self.sensores = sensores
        self.peso = peso
        self.eficiencia = eficiencia
        self.pos = 0


# Clase: Declaracion de la calse "Lista_autos" que funciona a razon de lista de nodos, donde cada nodo corresponde a una
# instanciacion de la clase Auto
class Lista_autos:
    # Metodo de clase Lista_autos: Metodo que inicializa cada instanciacion de esta clase
    def __init__(self):
        self.head = None
        self.tail = None

    # Metodo de clase Lista_autos: Metodo que agrega un nodo de tipo Auto al final de la lista
    def agregar_auto(self, marca, modelo, paisfabric, foto, aniotemp, cantbaterias, pilasxbateria, tensionxbateria,
                     estado, consumotores, sensores, peso, eficiencia):
        auto = Auto(marca, modelo, paisfabric, foto, aniotemp, cantbaterias, pilasxbateria, tensionxbateria, estado,
                    consumotores, sensores, peso, eficiencia)
        if self.head is None:
            self.head = auto
            self.tail = auto
        else:
            aux = self.tail
            self.tail = auto
            aux.next = auto
            auto.prev = aux

    # Metodo de clase Lista_autos: Metodo que ordena los nodos existentes en la lista segun el orden dado(ascendente
    # o descendente)
    def ordenar(self, orden):
        ordenado = False
        if orden == "A":
            while not ordenado:
                ordenado = True
                aux = self.head
                while aux is not None:
                    if aux != self.tail:
                        if aux.eficiencia < aux.next.eficiencia:
                            ordenado = False
                            if aux == self.head:
                                tmp = aux.next
                                if tmp.next is not None:
                                    self.head = tmp
                                    tmp.prev = None
                                    aux.next = tmp.next
                                    tmp.next.prev = aux
                                    aux.prev = tmp
                                    tmp.next = aux
                                else:
                                    aux.next = None
                                    tmp.prev = None
                                    tmp.next = aux
                                    aux.prev = tmp
                                    self.head = tmp
                                    self.tail = aux
                            else:
                                tmp = aux.next
                                if tmp.next is not None:
                                    aux.prev.next = tmp
                                    aux.next = tmp.next
                                    tmp.next = aux
                                    tmp.prev = aux.prev
                                    aux.prev = tmp
                                    aux.next.prev = aux
                                else:
                                    aux.prev.next = tmp
                                    aux.next = tmp.next
                                    tmp.next = aux
                                    tmp.prev = aux.prev
                                    aux.prev = tmp
                                    self.tail = aux
                        else:
                            aux = aux.next
                    else:
                        if aux.eficiencia > aux.prev.eficiencia:
                            ordenado = False
                            tmp = aux.prev
                            self.tail = tmp
                            tmp.prev.next = aux
                            aux.next = tmp
                            tmp.next = None
                            aux.prev = tmp.prev
                            tmp.prev = aux
                        else:
                            aux = aux.next
        else:
            while not ordenado:
                ordenado = True
                aux = self.head
                while aux is not None:
                    if aux != self.tail:
                        if aux.eficiencia > aux.next.eficiencia:
                            ordenado = False
                            if aux == self.head:
                                tmp = aux.next
                                if tmp.next is not None:
                                    self.head = tmp
                                    tmp.prev = None
                                    aux.next = tmp.next
                                    tmp.next.prev = aux
                                    aux.prev = tmp
                                    tmp.next = aux
                                else:
                                    aux.next = None
                                    tmp.prev = None
                                    tmp.next = aux
                                    aux.prev = tmp
                                    self.head = tmp
                                    self.tail = aux
                            else:
                                tmp = aux.next
                                if tmp.next is not None:
                                    aux.prev.next = tmp
                                    aux.next = tmp.next
                                    tmp.next = aux
                                    tmp.prev = aux.prev
                                    aux.prev = tmp
                                    aux.next.prev = aux
                                else:
                                    aux.prev.next = tmp
                                    aux.next = tmp.next
                                    tmp.next = aux
                                    tmp.prev = aux.prev
                                    aux.prev = tmp
                                    self.tail = aux
                        else:
                            aux = aux.next
                    else:
                        if aux.eficiencia < aux.prev.eficiencia:
                            ordenado = False
                            tmp = aux.prev
                            self.tail = tmp
                            tmp.prev.next = aux
                            aux.next = tmp
                            tmp.next = None
                            aux.prev = tmp.prev
                            tmp.prev = aux
                        else:
                            aux = aux.next
        aux = self.head
        pos = 1
        while aux is not None:
            aux.pos = pos
            pos += 1
            aux = aux.next

    # Metodo de clase Lista_autos: Metodo que muestra la informacion de cada uno de los nodos en  el Listbox
    # correspondiente
    def mostrar(self):
        lista_autos.delete(0, END)
        aux = self.head
        while aux is not None:
            lista_autos.insert(END, "<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>", " " + str(aux.pos) + ". " + str(aux.marca),
                               " " + str(aux.modelo), "", "", " Temporada: " + str(aux.aniotemp), "",
                               " Eficiencia: " + str(aux.eficiencia), "", "", "", "", "", "", "", "", "",
                               "<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")
            aux = aux.next


# Clase: Declaracion de la calse "Lista_pilotos" que funciona a razon de lista de nodos, donde cada nodo corresponde a
# una instanciacion de la clase Piloto
class Lista_pilotos:
    # Metodo de clase Lista_pilotos: Metodo que inicializa cada instanciacion de esta clase
    def __init__(self):
        self.head = None
        self.tail = None

    # Metodo de clase Lista_pilotos: Metodo que agrega un nodo de tipo Piloto al final de la lista
    def agregar_piloto(self, nombre, edad, nacionalidad, aniotemp, competparticip, participdestacadas,
                       participfallidas, victorias):
        auto = Piloto(nombre, edad, nacionalidad, aniotemp, competparticip, participdestacadas, participfallidas,
                      victorias)
        if self.head is None:
            self.head = auto
            self.tail = auto
        else:
            aux = self.tail
            self.tail = auto
            aux.next = auto
            auto.prev = aux

    # Metodo de clase Lista_pilotos: Metodo que ordena los nodos existentes en la lista segun el orden(ascendente
    # o descendente) y el factor dado (por RGP: rendimiento global o REP: rendimiento especifico)
    def ordenar(self, orden, factor):
        ordenado = False
        if orden == 'A':
            if factor == 'RGP':
                while not ordenado:
                    ordenado = True
                    aux = self.head
                    while aux is not None:
                        if aux != self.tail:
                            if aux.rend_global < aux.next.rend_global:
                                ordenado = False
                                if aux == self.head:
                                    tmp = aux.next
                                    if tmp.next is not None:
                                        self.head = tmp
                                        tmp.prev = None
                                        aux.next = tmp.next
                                        tmp.next.prev = aux
                                        aux.prev = tmp
                                        tmp.next = aux
                                    else:
                                        aux.next = None
                                        tmp.prev = None
                                        tmp.next = aux
                                        aux.prev = tmp
                                        self.head = tmp
                                        self.tail = aux
                                else:
                                    tmp = aux.next
                                    if tmp.next is not None:
                                        aux.prev.next = tmp
                                        aux.next = tmp.next
                                        tmp.next = aux
                                        tmp.prev = aux.prev
                                        aux.prev = tmp
                                        aux.next.prev = aux
                                    else:
                                        aux.prev.next = tmp
                                        aux.next = tmp.next
                                        tmp.next = aux
                                        tmp.prev = aux.prev
                                        aux.prev = tmp
                                        self.tail = aux
                            else:
                                aux = aux.next
                        else:
                            if aux.rend_global > aux.prev.rend_global:
                                ordenado = False
                                tmp = aux.prev
                                self.tail = tmp
                                tmp.prev.next = aux
                                aux.next = tmp
                                tmp.next = None
                                aux.prev = tmp.prev
                                tmp.prev = aux
                            else:
                                aux = aux.next
            else:
                while not ordenado:
                    ordenado = True
                    aux = self.head
                    while aux is not None:
                        if aux != self.tail:
                            if aux.rend_especifico < aux.next.rend_especifico:
                                ordenado = False
                                if aux == self.head:
                                    tmp = aux.next
                                    if tmp.next is not None:
                                        self.head = tmp
                                        tmp.prev = None
                                        aux.next = tmp.next
                                        tmp.next.prev = aux
                                        aux.prev = tmp
                                        tmp.next = aux
                                    else:
                                        aux.next = None
                                        tmp.prev = None
                                        tmp.next = aux
                                        aux.prev = tmp
                                        self.head = tmp
                                        self.tail = aux
                                else:
                                    tmp = aux.next
                                    if tmp.next is not None:
                                        aux.prev.next = tmp
                                        aux.next = tmp.next
                                        tmp.next = aux
                                        tmp.prev = aux.prev
                                        aux.prev = tmp
                                        aux.next.prev = aux
                                    else:
                                        aux.prev.next = tmp
                                        aux.next = tmp.next
                                        tmp.next = aux
                                        tmp.prev = aux.prev
                                        aux.prev = tmp
                                        self.tail = aux
                            else:
                                aux = aux.next
                        else:
                            if aux.rend_especifico > aux.prev.rend_especifico:
                                ordenado = False
                                tmp = aux.prev
                                self.tail = tmp
                                tmp.prev.next = aux
                                aux.next = tmp
                                tmp.next = None
                                aux.prev = tmp.prev
                                tmp.prev = aux
                            else:
                                aux = aux.next
        else:
            if factor == 'RGP':
                while not ordenado:
                    ordenado = True
                    aux = self.head
                    while aux is not None:
                        if aux != self.tail:
                            if aux.rend_global > aux.next.rend_global:
                                ordenado = False
                                if aux == self.head:
                                    tmp = aux.next
                                    if tmp.next is not None:
                                        self.head = tmp
                                        tmp.prev = None
                                        aux.next = tmp.next
                                        tmp.next.prev = aux
                                        aux.prev = tmp
                                        tmp.next = aux
                                    else:
                                        aux.next = None
                                        tmp.prev = None
                                        tmp.next = aux
                                        aux.prev = tmp
                                        self.head = tmp
                                        self.tail = aux
                                else:
                                    tmp = aux.next
                                    if tmp.next is not None:
                                        aux.prev.next = tmp
                                        aux.next = tmp.next
                                        tmp.next = aux
                                        tmp.prev = aux.prev
                                        aux.prev = tmp
                                        aux.next.prev = aux
                                    else:
                                        aux.prev.next = tmp
                                        aux.next = tmp.next
                                        tmp.next = aux
                                        tmp.prev = aux.prev
                                        aux.prev = tmp
                                        self.tail = aux
                            else:
                                aux = aux.next
                        else:
                            if aux.rend_global < aux.prev.rend_global:
                                ordenado = False
                                tmp = aux.prev
                                self.tail = tmp
                                tmp.prev.next = aux
                                aux.next = tmp
                                tmp.next = None
                                aux.prev = tmp.prev
                                tmp.prev = aux
                            else:
                                aux = aux.next
            else:
                while not ordenado:
                    ordenado = True
                    aux = self.head
                    while aux is not None:
                        if aux != self.tail:
                            if aux.rend_especifico > aux.next.rend_especifico:
                                ordenado = False
                                if aux == self.head:
                                    tmp = aux.next
                                    if tmp.next is not None:
                                        self.head = tmp
                                        tmp.prev = None
                                        aux.next = tmp.next
                                        tmp.next.prev = aux
                                        aux.prev = tmp
                                        tmp.next = aux
                                    else:
                                        aux.next = None
                                        tmp.prev = None
                                        tmp.next = aux
                                        aux.prev = tmp
                                        self.head = tmp
                                        self.tail = aux
                                else:
                                    tmp = aux.next
                                    if tmp.next is not None:
                                        aux.prev.next = tmp
                                        aux.next = tmp.next
                                        tmp.next = aux
                                        tmp.prev = aux.prev
                                        aux.prev = tmp
                                        aux.next.prev = aux
                                    else:
                                        aux.prev.next = tmp
                                        aux.next = tmp.next
                                        tmp.next = aux
                                        tmp.prev = aux.prev
                                        aux.prev = tmp
                                        self.tail = aux
                            else:
                                aux = aux.next
                        else:
                            if aux.rend_especifico < aux.prev.rend_especifico:
                                ordenado = False
                                tmp = aux.prev
                                self.tail = tmp
                                tmp.prev.next = aux
                                aux.next = tmp
                                tmp.next = None
                                aux.prev = tmp.prev
                                tmp.prev = aux
                            else:
                                aux = aux.next
        aux = self.head
        pos = 1
        while aux is not None:
            aux.pos = pos
            pos += 1
            aux = aux.next

    # Metodo de clase Lista_pilotos: Metodo que muestra la informacion de cada uno de los nodos en  el Listbox
    # correspondiente
    def mostrar(self):
        lista_pilotos.delete(0, END)
        aux = self.head
        while aux is not None:
            lista_pilotos.insert(END, "<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>", " " + str(aux.pos) + ". " + str(aux.nombre),
                                 "", "", " Nacionalidad: " + str(aux.nacionalidad), "",
                                 " Temporada: " + str(aux.aniotemp), "", " Competencias: " + str(aux.competparticip),
                                 "", " Rendimiento global: " + str(aux.rend_global), "",
                                 " Rendimiento especifico: " + str(aux.rend_especifico), "", "", "", "",
                                 "<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")
            aux = aux.next


'''******************************************************************************************************************'''
'''**********************************             INTERFAZ GRAFICA          *****************************************'''
'''******************************************************************************************************************'''

ventanaprincipal = Tk()
ventanaprincipal.geometry("630x500")
ventanaprincipal.resizable(False, False)
ventanaprincipal.title('Menu de escuderias')
canvasprincipal = Canvas(ventanaprincipal, width=350, height=200)
canvasprincipal.place(x=0, y=0)

texto = Label(ventanaprincipal, text="Seleccione la escuderia a la que desea accesar", font=("Courier", 11))
texto.place(x=20, y=20)

image_esc_alfaromeo = cargar_logo("Alfa Romeo")
btn_alfaromeo = Button(ventanaprincipal, image=image_esc_alfaromeo,
                       command=lambda: mostrar_ventanaescuderia("Alfa Romeo"), bd=5)
btn_alfaromeo.place(x=20, y=60)

image_esc_ferrari = cargar_logo("Ferrari")
btn_esc_ferrari = Button(ventanaprincipal, image=image_esc_ferrari, command=lambda: mostrar_ventanaescuderia("Ferrari"),
                         bd=5)
btn_esc_ferrari.place(x=220, y=60)

image_esc_mclaren = cargar_logo("McLaren")
btn_esc_mclaren = Button(ventanaprincipal, image=image_esc_mclaren, command=lambda: mostrar_ventanaescuderia("McLaren"),
                         bd=5)
btn_esc_mclaren.place(x=420, y=60)

image_esc_mercedes = cargar_logo("Mercedes")
btn_esc_mercedes = Button(ventanaprincipal, image=image_esc_mercedes,
                          command=lambda: mostrar_ventanaescuderia("Mercedes"), bd=5)
btn_esc_mercedes.place(x=20, y=190)

image_esc_redbull = cargar_logo("Red Bull")
btn_esc_redbull = Button(ventanaprincipal, image=image_esc_redbull,
                         command=lambda: mostrar_ventanaescuderia("Red Bull"), bd=5)
btn_esc_redbull.place(x=220, y=190)

image_esc_renault = cargar_logo("Renault")
btn_esc_renault = Button(ventanaprincipal, image=image_esc_renault, command=lambda: mostrar_ventanaescuderia("Renault"),
                         bd=5)
btn_esc_renault.place(x=420, y=190)

image_esc_bmwsauber = cargar_logo("BMW Sauber")
btn_esc_bmwsauber = Button(ventanaprincipal, image=image_esc_bmwsauber,
                           command=lambda: mostrar_ventanaescuderia("BMW Sauber"), bd=5)
btn_esc_bmwsauber.place(x=20, y=310)

image_esc_honda = cargar_logo("Honda")
btn_esc_honda = Button(ventanaprincipal, image=image_esc_honda, command=lambda: mostrar_ventanaescuderia("Honda"), bd=5)
btn_esc_honda.place(x=220, y=310)

image_esc_lotus = cargar_logo("Lotus")
btn_esc_lotus = Button(ventanaprincipal, image=image_esc_lotus, command=lambda: mostrar_ventanaescuderia("Lotus"), bd=5)
btn_esc_lotus.place(x=420, y=310)

ventanaescuderia = Toplevel(width=1000, height=700)
ventanaescuderia.geometry("1000x700")
ventanaescuderia.resizable(False, False)
ventanaescuderia.title('Informacion de escuderia')
canvasescuderia = Canvas(ventanaescuderia, width=1000, height=700)
canvasescuderia.place(x=0, y=0)
ventanaescuderia.iconify()

lista_pilotos = Listbox(ventanaescuderia)
scroll_pilotos = Scrollbar(ventanaescuderia, command=lista_pilotos.yview)

lista_pilotos.config(yscrollcommand=scroll_pilotos.set, width=32, height=18, font=("Courier", 14), bd=10)
lista_pilotos.place(x=420, y=200)
scroll_pilotos.pack(side=RIGHT, fill=Y)

lista_autos = Listbox(ventanaescuderia)
scroll_autos = Scrollbar(ventanaescuderia, command=lista_autos.yview)

lista_autos.config(yscrollcommand=scroll_autos.set, width=32, height=18, font=("Courier", 14), bd=10)
lista_autos.place(x=20, y=200)
scroll_autos.pack(side=RIGHT, fill=Y)

ventanabout = Toplevel(width=700, height=570)
ventanabout.geometry("700x570")
ventanabout.resizable(False, False)
ventanabout.title('Informacion de desarrollador')
canvasabout = Canvas(ventanabout, width=700, height=600)
canvasabout.place(x=0, y=0)
ventanabout.iconify()

desarrollador1 = Listbox(ventanabout)
desarrollador1.config(width=45, height=7, font=("Courier", 12), bd=10)
desarrollador1.place(x=20, y=40)

desarrollador2 = Listbox(ventanabout)
desarrollador2.config(width=45, height=7, font=("Courier", 12), bd=10)
desarrollador2.place(x=20, y=250)

ventananuevoauto = Toplevel(width=550, height=475)
ventananuevoauto.geometry("490x475")
ventananuevoauto.resizable(False, False)
ventananuevoauto.title('Agregar nuevo auto')
canvasnuevoauto = Canvas(ventananuevoauto, width=550, height=475)
canvasnuevoauto.place(x=0, y=0)
ventananuevoauto.iconify()

ventanatestdrive = Toplevel(width=400, height=350)
ventanatestdrive.geometry("400x350")
ventanatestdrive.resizable(False, False)
ventanatestdrive.title('Test Drive')
canvastestdrive = Canvas(ventanatestdrive, width=400, height=350)
canvastestdrive.place(x=0, y=0)
ventanatestdrive.iconify()

'''******************************************************************************************************************'''
'''****************************************             MAIN          ***********************************************'''
'''******************************************************************************************************************'''


# Metodo independiente: Metodo que inicia el programa automaticamente
def main():
    ventanabout.iconify()
    ventanaescuderia.iconify()
    ventanaprincipal.deiconify()
    about = Button(ventanaprincipal, text="About", command=lambda: mostrar_ventanaabout(), bg="White",
                   font=("Courier", 11))
    about.place(x=10, y=460)
    salir = Button(ventanaprincipal, text="Salir", command=lambda: sys.exit(), bg="White", font=("Courier", 11))
    salir.place(x=560, y=460)
    ventanaprincipal.mainloop()


main()
