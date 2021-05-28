# TODO: stop user after first mistake vs waiting until all 5 have been entered
# TODO: in renpy, flash green or red after evaluation

import tkinter as tk
import random

blinkOrder = []
userOrder = []
highscore = 0
score = 0
numclicks = 0

window = tk.Tk()


# increases score
def increase():
    value = int(score["text"])
    score["text"] = f"{value + 1}"
    if int(score["text"]) > int(counter["text"]):
        counter["text"] = f"{value + 1}"
    if score["text"] == 10:
        start['state'] = tk.DISABLED


# flashes a label; variable a: which display will be flashed and num is when it will flash
# as score increases, the flashes appear faster and for less time (done through subtraction)
def flash(a, num):
    if a == 0:
        window.after(500 * num + 300 - 25 * int(score["text"]), lambda: displayL.config(bg='yellow'))
        window.after(500 * num + 500 - 50 * int(score["text"]), lambda: displayL.config(bg='lightgrey'))
    elif a == 1:
        window.after(500 * num + 300 - 25 * int(score["text"]), lambda: displayM.config(bg='yellow'))
        window.after(500 * num + 500 - 50 * int(score["text"]), lambda: displayM.config(bg='lightgrey'))
    else:
        window.after(500 * num + 300 - 25 * int(score["text"]), lambda: displayR.config(bg='yellow'))
        window.after(500 * num + 500 - 50 * int(score["text"]), lambda: displayR.config(bg='lightgrey'))


# starts the flashes
def start():
    global blinkOrder
    global userOrder
    blinkOrder.clear()
    userOrder.clear()
    buttonL['state'] = tk.NORMAL
    buttonM['state'] = tk.NORMAL
    buttonR['state'] = tk.NORMAL
    for i in range(0, 5):
        n = random.randint(0, 2)
        flash(n, i)
        blinkOrder.append(n)


# responds to player clicks and evaluates if the response is correct
def evaluate(n):
    global numclicks
    global blinkOrder
    global userOrder
    numclicks += 1
    userOrder.append(n)
    if numclicks == 5:
        correct = True
        for i in range(0, 5):
            if blinkOrder[i] != userOrder[i]:
                correct = False
                score["text"] = 0
                break
        if correct:
            increase()

        # resets everything
        numclicks = 0
        buttonL['state'] = tk.DISABLED
        buttonM['state'] = tk.DISABLED
        buttonR['state'] = tk.DISABLED
        blinkOrder.clear()
        userOrder.clear()


# window stuff
window.rowconfigure([0, 1], minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)

displayL = tk.Label(master=window, text="0", bg='lightgrey')
displayL.grid(row=0, column=0)

displayM = tk.Label(master=window, text="0", bg='lightgrey')
displayM.grid(row=0, column=1)

displayR = tk.Label(master=window, text="0", bg='lightgrey')
displayR.grid(row=0, column=2)

startButton = tk.Button(master=window, text="Start", command=start)
startButton.grid(row=0, column=4)

buttonL = tk.Button(master=window, text="0", command=lambda: evaluate(0))  # changed to start here
buttonL.grid(row=1, column=0)

buttonM = tk.Button(master=window, text="0", command=lambda: evaluate(1))
buttonM.grid(row=1, column=1)

buttonR = tk.Button(master=window, text="0", command=lambda: evaluate(2))
buttonR.grid(row=1, column=2)

HS = tk.Label(master=window, text="High Score")
HS.grid(row=0, column=3)
counter = tk.Label(master=window, text="0")
counter.grid(row=1, column=3)

score = tk.Label(master=window, text="0")
score.grid(row=1, column=4)

window.configure(bg='lightgrey')

buttonL['state'] = tk.DISABLED
buttonM['state'] = tk.DISABLED
buttonR['state'] = tk.DISABLED

window.mainloop()
