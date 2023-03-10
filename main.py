"""
Fakime Nur Ozdemir
jan 2023
2048 version 1.0 """
import tkinter
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("2048 by Faki")
window.geometry("495x700+30+80")
window.config(background="#888888")

# variables
intervaley = 90
intervalex = 90
nmove = 0

# frame1
frame1 = Frame(window, highlightbackground="black", highlightthickness=2)
frame1.place(x=320, y=80)

lbl_2048 = Label(frame1, text="2048", bg="#4F7942", height=2, width=17, fg="white")
lbl_2048.pack()

# frame2
frame2 = Frame(window, highlightbackground="#4F7942", highlightthickness=3)
frame2.place(x=300, y=122)

lbl_scr = Label(frame2, text="Score", background="#888888", height=3, width=9, fg="black")
lbl_scr.pack()

# frame3
frame3 = Frame(window, highlightbackground="#4F7942", highlightthickness=3)
frame3.place(x=380, y=122)

lbl_tpscr = Label(frame3, text="Top Score", background="#888888", height=3, width=9, fg="black")
lbl_tpscr.pack()

# list de couleurs
list_colors = {
    0: "grey",
    2: "#EA9999",
    4: "#F6B26B",
    8: "#B6D7A8",
    16: "#FFE599",
    32: "#C27BA0",
    64: "#A2C4C9",
    128: "#597EAA",
    256: "#B4A7D6",
    512: "#F9CB9C",
    1024: "#D5A6BD",
    2048: "#9FC5F8",
    4096: "#E69138",
    8192: "#8E7CC3",
}
#tableau des valeur pour la fonc tasse4
numbers = [[2, 2, 4, 4], [0, 0, 0, 0], [0, 2, 2, 4], [0, 2, 2, 8]]
labels = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]

for line in range(len(numbers)):
    for col in range(len(numbers[line])):
        labels[line][col] = Label(text="", width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 17),
                                  highlightbackground="black", highlightthickness=3)
        labels[line][col].place(x=70 + intervalex * col, y=250 + intervaley * line)

# functions
# reçoit 4 nombres, tasse vers le a,  et en renvoie 5
def tasse_4(a,b,c,d):
    nmove=0 #sert à savoir si on a réussi à bouger
    # ici le code va manipuler a,b,c et d
    if (c == 0 and d > 0):
        c,d = d, 0
        nmove+=1

    if (b == 0 and c > 0):
        b,c,d = c, d, 0
        nmove+= 1

    if (a==0 and b>0):
        a,b,c,d = b,c,d,0
        nmove+= 1

    if (a==b and a>0):
        a,b,c,d = 2*a,c,d,0
        nmove += 1

    if (b==c and b>0):
        b,c,d= 2* b,d,0
        nmove += 1

    if (c==d and c>0):
        c,d = 2*c,0
        nmove += 1


    # ici on retourne les cinq valeurs en un tableau
    temp=[a,b,c,d,nmove] #tableau temporaire de fin
    return temp

#la fonction ici sert tasser vers la gauche
def moveleft(event):
    movetotal = 0
    for ligne in range (4):
        n = 0
        [numbers[ligne][0],numbers[ligne][1],numbers[ligne][2],numbers[ligne][3],n]= tasse_4(numbers[ligne][0],numbers[ligne][1],numbers[ligne][2],numbers[ligne][3])
        movetotal += n;
    display()
    print(movetotal)

#la fonction ici sert tasser vers la droite
def moveright(event):
    movetotal = 0
    for ligne in range (4):
        n = 0
        [numbers[ligne][3],numbers[ligne][2],numbers[ligne][1],numbers[ligne][0],n] = tasse_4(numbers[ligne][3],numbers[ligne][2],numbers[ligne][1],numbers[ligne][0])
        movetotal += n;
    display()
    print(movetotal)

#la fonction ici sert à tasser vers l'haut
def moveup(event):
    movetotal = 0
    for line in range (4):
        n = 0
        [numbers[0][line],numbers[1][line],numbers[2][line],numbers[3][line],n] = tasse_4(numbers[0][line],numbers[1][line],numbers[2][line],numbers[3][line])
        movetotal += n;
    display()
    print(movetotal)

#la function ici sert à tasser vers le bas
def movedown(event):
    movetotal = 0
    for line in range (4):
        n = 0
        [numbers[3][line],numbers[2][line],numbers[1][line],numbers[0][line],n] = tasse_4(numbers[3][line],numbers[2][line],numbers[1][line],numbers[0][line])
        movetotal += n;
    display()
    print(movetotal)

#la fonction ici sert à refresh le jeu actuel
def display():
    for line in range(len(numbers)):
        for col in range(len(numbers[line])):
            if numbers[line][col] == 0:
                labels[line][col].config(text="", bg=list_colors[numbers[line][col]])
            else:
                labels[line][col].config(text=numbers[line][col], bg=list_colors[numbers[line][col]])

#fonction de new button
def new_button():
    global numbers
    numbers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 4]]
    display()

# new button (aide Carlos>aide Athos)
new_button = tkinter.Button(window, command=new_button, text="Nouveau", background="#274E13", fg="#888888")
new_button.place(x=395, y=180)

#assignation des touches a,w,s,d
window.bind("d",moveright)
window.bind("a",moveleft)
window.bind("w",moveup)
window.bind("s",movedown)


display()
window.mainloop()

