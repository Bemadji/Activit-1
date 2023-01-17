from tkinter import *
import tkinter as tkinter

root = Tk()
root.title("Bienvenue sur la plateforme d'Orientation Universitaire !")
root.geometry("950*550 +180+50")
logo=Canvas(root,width=900,height=500,bg="blue")
logo.place(x=10,y=7)
log=Label(logo,text="Bienvenue sur la plateforme",font=("arial",19,"bold"))
log.place(x=20,y=10)
identifiant=Label(logo,text="Saisir le email ou le tel",bg="blue",font=("arial",15,"bold"),fg="#fff")
identifiant.place(x=350,y=130)

mdp=Button(logo,text="Mot de passe",bg="blue",font=("arial",15))
mdp.place(x=400,y=190)

root.mainloop()

