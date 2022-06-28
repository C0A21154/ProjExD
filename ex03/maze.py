from email.mime import image
from pickle import GLOBAL
import tkinter as tk
import tkinter.messagebox as tkm
from tracemalloc import start
import maze_maker as mmake

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my, cx, cy

    if key == "Up":
        if makemaze[my-1][mx] == 0:
            my -= 1
    elif key == "Down":
        if makemaze[my+1][mx] == 0:
            my += 1
    elif key == "Left":
        canvas.itemconfigure(ImageID, image = toriL)
        if makemaze[my][mx-1] == 0:
            mx -= 1
    elif key == "Right":
        canvas.itemconfigure(ImageID, image = toriR)
        if makemaze[my][mx+1] == 0:
            mx += 1

    cx = mx * 100 +50
    cy = my *100 + 50
    canvas.coords("tori", cx, cy)

    if mx == 13 and  my == 7:
        tkm.showinfo("ゴール","ゴールおめでとう!!")
        exit()

    maze.after(65, main_proc)


if __name__ == "__main__":
    maze = tk.Tk()
    maze.title("迷えるこうかとん")
    
    canvas = tk.Canvas(maze, width = 1500, height = 900, bg = "black")
    canvas.pack()

    makemaze =  mmake.make_maze(15, 9)
    mmake.show_maze(canvas, makemaze)

    start_image = tk.PhotoImage(file = "fig/start.png")
    goal_image = tk.PhotoImage(file = "fig/goal.png")
    road_image = tk.PhotoImage(file = "fig/road.png")
    for i in range(9):
        for j in range(15):
            if makemaze[i][j] == 0:
                canvas.create_image(j * 100 + 50, i * 100 + 50, image = road_image)

    toriR = tk.PhotoImage(file = "fig/2.png")
    toriL = tk.PhotoImage(file = "fig/5.png")
    mx, my = 1, 1
    cx, cy = mx * 100 + 50, my * 100 + 50
    canvas.create_image(cx, cy, image = start_image)
    canvas.create_image(13 * 100 + 50, 7 * 100 + 50, image = goal_image)
    ImageID = canvas.create_image(cx, cy, image = toriR, tag = "tori")
    key = ""

    maze.bind("<KeyPress>", key_down)
    maze.bind("<KeyRelease>", key_up)
    main_proc()
    maze.mainloop()