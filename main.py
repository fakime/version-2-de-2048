"""
Fakime Nur Ozdemir
jan 2023
2048 version 1.0 """
import tkinter
from tkinter import *
import random
import copy
from tkinter import messagebox

window = Tk()
window.title("2048 by Faki")
window.geometry("495x700+30+80")
window.config(background="#888888")
window.resizable(width=False,height=False)

# variables
intervaley = 90
intervalex = 90
nmove = 0
score = 0
first2048 = 1
first8192 = 1

# frame1
frame1 = Frame(window, highlightbackground="black", highlightthickness=2)
frame1.place(x=320, y=80)

lbl_2048 = Label(frame1, text="2048", bg="#4F7942", height=2, width=17, fg="white")
lbl_2048.pack()

# frame2
frame2 = Frame(window, highlightbackground="#4F7942", highlightthickness=3)
frame2.place(x=350, y=122)

lbl_scr = Label(frame2, text=f"Score\n {score}", background="#888888", height=3, width=9, fg="black")
lbl_scr.pack()

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
numbers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 8192, 0, 0]]
labels = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]

for line in range(len(numbers)):
    for col in range(len(numbers[line])):
        labels[line][col] = Label(text="", width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 17),
                                  highlightbackground="black", highlightthickness=3)
        labels[line][col].place(x=70 + intervalex * col, y=250 + intervaley * line)

# functions
# reçoit 4 nombres, tasse vers le a,  et en renvoie 5
def tasse_4(a,b,c,d):
    global score
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
        score+= 2*a
    if (b==c and b>0):
        b,c,d= 2* b,d,0
        nmove += 1
        score+=2*b
    if (c==d and c>0):
        c,d = 2*c,0
        nmove += 1
        score+=2*c

#afficher le score
    lbl_scr.config(text=f"Score\n {score}")
    print(score)
    # ici on retourne les cinq valeurs en un tableau
    temp=[a,b,c,d,nmove] #tableau temporaire de fin
    return temp


#la fonction ici sert à refresh le jeu actuel
def display():
    for line in range(len(numbers)):
        for col in range(len(numbers[line])):
            if numbers[line][col] == 0:
                labels[line][col].config(text="", bg=list_colors[numbers[line][col]])
            else:
                labels[line][col].config(text=numbers[line][col], bg=list_colors[numbers[line][col]])

#perdu
def movement():
    global numbers
    moveperdu = 0
    #copied my numbers
    numbers2 = copy.deepcopy(numbers)
    #move left
    for ligne in range(4):
        [numbers2[ligne][0], numbers2[ligne][1], numbers2[ligne][2], numbers2[ligne][3],nmove] = tasse_4(numbers2[ligne][0],numbers2[ligne][1],numbers2[ligne][2],numbers2[ligne][3])
        moveperdu += nmove
    #move right
    for ligne in range(4):
        [numbers2[ligne][3], numbers2[ligne][2], numbers2[ligne][1], numbers2[ligne][0], nmove] = tasse_4(numbers2[ligne][3],numbers2[ligne][2],numbers2[ligne][1],numbers2[ligne][0])
        moveperdu += nmove
    #move up
    for line in range(4):
        [numbers2[0][line], numbers2[1][line], numbers2[2][line], numbers2[3][line], nmove] = tasse_4(numbers2[0][line],numbers2[1][line],numbers2[2][line],numbers2[3][line])
        moveperdu += nmove
    #move down
    for line in range(4):
        [numbers2[3][line], numbers2[2][line], numbers2[1][line], numbers2[0][line], nmove] = tasse_4(numbers2[3][line],numbers2[2][line],numbers2[1][line],numbers2[0][line])
    moveperdu += nmove

    if moveperdu == 0:
        messagebox.showinfo("PERDU","Vous avez perdu !")
        window.config(background="#6EA482")
#gagne
def movement2():
    global first8192, first2048
    for line in range(len(numbers)):
        for col in range(len(numbers[line])):
            if first8192 == 1:
                if numbers[line][col] == 8192:
                    messagebox.showinfo("WIN", "Vous avez WIN!")
                    window.config(background="#4C54B4")
                    first8192 = 0
            if first2048 == 1:
                if numbers[line][col]== 2048:
                    messagebox.showinfo("2048", "Vous avez fait 2048!")
                    first2048 = 0


#generer avec une chance de 80-20 % (aide de thibault)
def spawncase2_4():
    if random.random() >= 0.8:
        return 4
    else:
        return 2

#la fonctione qui sert à random le placement de un chiffres
def rondom():
    randomline = random.randint(0, 3)
    randomcolumn = random.randint(0, 3)
    while numbers[randomline][randomcolumn]>0:
        randomline = random.randint(0, 3)
        randomcolumn = random.randint(0, 3)
    numbers[randomline][randomcolumn] = spawncase2_4()
    display()

rondom()
rondom()

#la fonction ici sert tasser vers la gauche
def moveleft(event):
    global nmove
    movetotal = 0
    for ligne in range(4):
        [numbers[ligne][0],numbers[ligne][1],numbers[ligne][2],numbers[ligne][3],nmove]= tasse_4(numbers[ligne][0],numbers[ligne][1],numbers[ligne][2],numbers[ligne][3])
        movetotal += nmove

    if movetotal == 0:
        print("Move")
    else:
        rondom()
        movement2()
        movement()
    display()

#la fonction ici sert tasser vers la droite
def moveright(event):
    movetotal = 0
    for ligne in range(4):
        [numbers[ligne][3],numbers[ligne][2],numbers[ligne][1],numbers[ligne][0],nmove] = tasse_4(numbers[ligne][3],numbers[ligne][2],numbers[ligne][1],numbers[ligne][0])
        movetotal += nmove
    if movetotal == 0:
        print("Move")
    else:
        rondom()
        movement2()
        movement()

    display()


#la fonction ici sert à tasser vers l'haut
def moveup(event):
    movetotal = 0
    for line in range(4):
        [numbers[0][line],numbers[1][line],numbers[2][line],numbers[3][line],nmove] = tasse_4(numbers[0][line],numbers[1][line],numbers[2][line],numbers[3][line])
        movetotal += nmove
    if movetotal == 0:
        print("Move")
    else:
        rondom()
        movement2()
        movement()

    display()

#la function ici sert à tasser vers le bas
def movedown(event):
    movetotal = 0
    for line in range(4):
        [numbers[3][line],numbers[2][line],numbers[1][line],numbers[0][line],nmove] = tasse_4(numbers[3][line],numbers[2][line],numbers[1][line],numbers[0][line])
        movetotal += nmove
    if movetotal == 0:
        print("Move")
    else:
        rondom()
        movement2()
        movement()
    display()

#fonction de new button
def new_button():
    global numbers,score
    numbers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    score = 0
    lbl_scr.config(text=f"Score\n {score}")
    window.config(background="#888888")
    rondom()
    rondom()
    display()

# new button (aide Carlos>aide Athos)
new_button = tkinter.Button(window, command=new_button, text="Nouveau", background="#274E13", fg="#888888")
new_button.place(x=360, y=180)

#assignation des touches a,w,s,d
window.bind("d",moveright)
window.bind("a",moveleft)
window.bind("w",moveup)
window.bind("s",movedown)

display()
window.mainloop()

