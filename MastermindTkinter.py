import tkinter
import random

colors = ["#ff0000","#ffff00","#00ff00","#00ffff","#0000ff","#ff00ff"]

root = tkinter.Tk()
colorwindow = ""
solution = []
white = 0
black = 0
count = 0
currentguess = [""] * 4

def makesolution():
    global solution
    while len(solution) < 4:
        r = random.randint(0,5)
        if r not in solution:
            solution.append(r)

def score(guess):
    global solution
    global white
    global black
    white = 0
    black = 0
    for i in range(4):
        if guess[i] == str(solution[i]):
            white += 1
        else:
            for j in range(4):
                if guess[i] == str(solution[j]):
                    black += 1
    if white == 4:
        print("You win. You got it in " + str(count) + " guesses.")
    elif count == 8:
        print("No one loves you and you suck at your only job.")
    else:
        print("Whites:" + str(white) + " & Blacks:" + str(black))
        playerguess()

def playerguess():
    global count
    print("Make a guess.")
    guess = input()
    count += 1
    score(guess)

def colorpicker(position, button):
    global colorwindow
    colorwindow = tkinter.Toplevel(root)
    red = tkinter.Button(colorwindow, width = 4, height = 2, bg = colors[0], command = lambda: closecolorwindow(position, button, colors[0]))
    red.grid(row = 0, column = 0)
    yellow = tkinter.Button(colorwindow, width = 4, height = 2, bg = colors[1], command = lambda: closecolorwindow(position, button, colors[1]))
    yellow.grid(row = 0, column = 1)
    green = tkinter.Button(colorwindow, width = 4, height = 2, bg = colors[2], command = lambda: closecolorwindow(position, button, colors[2]))
    green.grid(row = 0, column = 2)
    cyan = tkinter.Button(colorwindow, width = 4, height = 2, bg = colors[3], command = lambda: closecolorwindow(position, button, colors[3]))
    cyan.grid(row = 0, column = 3)
    blue = tkinter.Button(colorwindow, width = 4, height = 2, bg = colors[4], command = lambda: closecolorwindow(position, button, colors[4]))
    blue.grid(row = 0, column = 4)
    magenta = tkinter.Button(colorwindow, width = 4, height = 2, bg = colors[5], command = lambda: closecolorwindow(position, button, colors[5]))
    magenta.grid(row = 0, column = 5)

def closecolorwindow(position, button, color):
    global colorwindow
    colorwindow.destroy()
    button.config(bg=color)
    currentguess[position] = color

def draw():
    global canvas
    canvas.delete(tkinter.ALL)
    canvas.create_rectangle(0, 0, cwidth, cheight, fill = "wheat")

root.config(bg="wheat")

b1 = tkinter.Button(root, width = 4, height = 2, bg = "#999999", command = lambda: colorpicker(0, b1))
b1.grid(row = 1, column = 0)

b2 = tkinter.Button(root, width = 4, height = 2, bg = "#999999", command = lambda: colorpicker(1, b2))
b2.grid(row = 1, column = 1)

b3 = tkinter.Button(root, width = 4, height = 2, bg = "#999999", command = lambda: colorpicker(2, b3))
b3.grid(row = 1, column = 2)

b4 = tkinter.Button(root, width = 4, height = 2, bg = "#999999", command = lambda: colorpicker(3, b4))
b4.grid(row = 1, column = 3)

submit = tkinter.Button(root, text = "Submit Guess", padx = 10)
submit.grid(row = 1, column = 4, padx = 10)

cwidth = 300
cheight = 400

canvas = tkinter.Canvas(root, width = cwidth, height = cheight)
canvas.grid(row = 2, column = 0, columnspan = 5)

makesolution()
draw()

root.mainloop()
