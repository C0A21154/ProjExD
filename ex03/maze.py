import tkinter as tk
import tkinter.messagebox as tkm
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
        if makemaze[my][mx-1] == 0:
            mx -= 1
    elif key == "Right":
        if makemaze[my][mx+1] == 0:
            mx += 1

    cx = mx * 100 +50
    cy = my *100 + 50
    canvas.coords("tori", cx, cy)
    maze.after(65, main_proc)


if __name__ == "__main__":
    maze = tk.Tk()
    maze.title("迷えるこうかとん")
    
    canvas = tk.Canvas(maze, width = 1500, height = 900, bg = "black")
    canvas.pack()

    makemaze =  mmake.make_maze(15, 9)
    mmake.show_maze(canvas, makemaze)

    print(makemaze)

    tori = tk.PhotoImage(file = "fig/3.png")
    mx, my = 1, 1
    cx, cy = mx * 100 + 50, my * 100 + 50
    canvas.create_image(cx, cy, image = tori, tag = "tori")
    key = ""

    maze.bind("<KeyPress>", key_down)
    maze.bind("<KeyRelease>", key_up)
    main_proc()
    maze.mainloop()