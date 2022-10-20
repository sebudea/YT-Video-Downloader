from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox as MessageBox

print(os.getcwd())

def accion():
    enlace=videos.get()     
    video = YouTube(enlace)  
    descarga = video.streams.get_highest_resolution()
    descarga.download()

def popup():
    MessageBox.showinfo("Sobre mí")

 
root = Tk()
root.config(bd=15)
root.title("Script SACDownloader YT")

imagen = PhotoImage(file="centroarcoirismini.png")
foto = Label(root, image=imagen, bd=10)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)


menubar.add_cascade(label="Para más información", menu=helpmenu)
helpmenu.add_command(label="Información del autor",command=popup)

menubar.add_command(label="Salir", command=root.destroy)


instrucciones = Label(root, text="Programa Python para descargar vídeos de Youtube\nSebastian Aristizabal Castañeda :D")
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2, column=1)

root.mainloop()