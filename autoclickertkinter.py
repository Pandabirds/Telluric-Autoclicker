import time
import pynput
import tkinter as tk
import threading

#* Settings:
#* TargetX
#* TargetY
#* SetPos
#* ReturnCursor
#* Milliseconds

root = tk.Tk()
root.configure(bg = "#2b5b84")
root.geometry("253x150")
root.resizable(0, 0)
root.title("TA")

running = False
firstRun = True

def on_press(key):
    if str(key) == "Key.f6":
        global running
        global firstRun
        running = not running
        if firstRun:
            firstRun = False
            start_program()

def on_move(x, y):
    currentMouseCoordinatesLabel.config(text = "({0}, {1})".format(x, y))

listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()

listener2 = pynput.mouse.Listener(on_move=on_move)
listener2.start()

setPosValue = tk.BooleanVar()
returnCursorValue = tk.BooleanVar()

targetXLabel = tk.Label(text = "Target (X)", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")
targetXEntry = tk.Entry(borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")

targetYLabel = tk.Label(text = "Target (Y)", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")
targetYEntry = tk.Entry(borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")

millisecondsLabel = tk.Label(text = "Ms", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")
millisecondsEntry = tk.Entry(borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")

numOfClicksLabel = tk.Label(text = "# Of Clicks", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")
numOfClicksEntry = tk.Entry(borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")

setPosLabel = tk.Label(text = "Set Position", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")
setPosCheckbutton = tk.Checkbutton(var = setPosValue, borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#2b5b84", activebackground = "#FFD43B", activeforeground = "#2b5b84")

returnCursorLabel = tk.Label(text = "Return Cursor", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")
returnCursorCheckbutton = tk.Checkbutton(var = returnCursorValue, borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#2b5b84", activebackground = "#FFD43B", activeforeground = "#2b5b84")

currentMouseCoordinatesLabel = tk.Label(text = "", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")
# * -----------------------------------------

targetXLabel.grid(row = 0, column = 0)
targetXEntry.grid(row = 1, column = 0)
targetXEntry.insert(0, "0")

targetYLabel.grid(row = 0, column = 1)
targetYEntry.grid(row = 1, column = 1)
targetYEntry.insert(0, "0")

millisecondsLabel.grid(row = 2, column = 0)
millisecondsEntry.grid(row = 3, column = 0)

numOfClicksLabel.grid(row = 2, column = 1)
numOfClicksEntry.grid(row = 3, column = 1)

setPosLabel.grid(row = 4, column = 0)
setPosCheckbutton.grid(row = 5, column = 0)

returnCursorLabel.grid(row = 4, column = 1)
returnCursorCheckbutton.grid(row = 5, column = 1)

currentMouseCoordinatesLabel.grid(row = 6, column = 0)

def start_program():
    mouse = pynput.mouse.Controller()
    targetX = int(targetXEntry.get())
    targetY = int(targetYEntry.get())
    ms = int(millisecondsEntry.get())
    numOfClicks = int(numOfClicksEntry.get())
    
    setPos = setPosValue.get()
    returnCursor = returnCursorValue.get()
    global running
    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()
    print(running)
    
    while True:
        if running:
            if setPos:
                oldPos = mouse.position
                mouse.position = (targetX, targetY)
            mouse.click(pynput.mouse.Button.left, numOfClicks)
            if setPos:
                mouse.position = oldPos
            if ms != 0:
                time.sleep(ms / 1000)

root.mainloop()