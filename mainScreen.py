from tkinter import *



#Set Up de Ventana
width = 800
height = 400
#Ventana Principal

V_inicio=Tk()
V_inicio.title('Formula CE')
V_inicio.minsize(width, height)
V_inicio.resizable(width=NO, height=NO)

# Canvas de la ventana...
C_inicio=Canvas(V_inicio, width=800, height=600, bg='white')
C_inicio.place(x=0, y=0)


V_inicio.mainloop()