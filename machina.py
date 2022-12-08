from tkinter import *



root=Tk() # Generamos la Ventana
root.title("Maquina Expendedora")

# Definimos botones para la venta
#imgcoca = PhotoImage(file = r"\coca.jpg")
boton_coca= Button(root, text= "Coca Cola",width = 10, height= 2, command = lambda:click_boton())
boton_coca.grid( row = 1, column = 0,  padx = 5, pady = 5)





root.mainloop()
