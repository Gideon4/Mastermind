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
history = []

def makesolution():
    global solution
    while len(solution) < 4:
        r = random.randint(0,5)
        if colors[r] not in solution:
            solution.append(colors[r])

def score(guess):
    global solution, white, black
    white = 0
    black = 0
    for i in range(4):
        if guess[i] == solution[i]:
            white += 1
        else:
            for j in range(4):
                if guess[i] == solution[j]:
                    black += 1
    history[-1].append(white)
    history[-1].append(black)

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

def submit():
    global count
    if "" not in currentguess:
        history.append(currentguess.copy())
        count += 1
        score(currentguess)
        draw()

def draw():
    global canvas
    canvas.delete(tkinter.ALL)
    canvas.create_rectangle(0, 0, cwidth, cheight, fill = "#ffffff")
    xpos = 10
    ypos = 10
    for guess in history:
        counter = 0
        for color in guess:
            if counter < 4: 
                canvas.create_oval(xpos, ypos, xpos + 30, ypos + 30, fill = color)
                xpos += 40
            elif counter == 4:
                for i in range(color):
                    canvas.create_oval(xpos, ypos, xpos + 20, ypos + 20, fill = "#ffffff")
                    xpos += 25
            elif counter == 5:
                for j in range(color):
                    canvas.create_oval(xpos, ypos, xpos + 19, ypos + 19, fill = "#000000")
                    xpos += 25
            counter += 1
        xpos = 10
        ypos += 45
        counter = 0

root.config(bg="#ffffff")

b1 = tkinter.Button(root, width = 4, height = 2, bg = "#999999", command = lambda: colorpicker(0, b1))
b1.grid(row = 1, column = 0)

b2 = tkinter.Button(root, width = 4, height = 2, bg = "#999999", command = lambda: colorpicker(1, b2))
b2.grid(row = 1, column = 1)

b3 = tkinter.Button(root, width = 4, height = 2, bg = "#999999", command = lambda: colorpicker(2, b3))
b3.grid(row = 1, column = 2)

b4 = tkinter.Button(root, width = 4, height = 2, bg = "#999999", command = lambda: colorpicker(3, b4))
b4.grid(row = 1, column = 3)

submit = tkinter.Button(root, text = "Submit Guess", padx = 10, bg  = "#ff0000", fg = "#ffffff", font = "Arial 16 bold", command = submit)
submit.grid(row = 1, column = 4, padx = 10)

cwidth = 350
cheight =400

canvas = tkinter.Canvas(root, width = cwidth, height = cheight)
canvas.grid(row = 2, column = 0, columnspan = 5)

makesolution()
draw()

root.mainloop()
