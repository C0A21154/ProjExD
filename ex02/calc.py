import tkinter as tk
import tkinter.messagebox as tkm
from turtle import right

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    if (txt == "="):
        enter()
        return 0
    elif (txt == "×"):
        txt = "*"
    elif (txt == "÷"):
        txt = "/"
    elif (txt == "C"):
        entry.delete(-1)
        return 0
    elif (txt == "AC"):
        entry.delete(0, tk.END)
        return 0
    elif (txt == "%"):
        ans = (eval(entry.get())) * 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"{ans}")

    entry.insert(tk.END, f"{txt}")

def enter():
    ans = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, f"{ans}")

dentaku = tk.Tk()
dentaku.title("電卓")
dentaku.geometry("392x460")
enzansi = ["÷", "×", "-", "+"]
option = [" ","%", "C", "AC"]

entry = tk.Entry(dentaku, width = 15, justify = 'right', font = ("Times New Roman", 35))
entry.grid(columnspan = 10)

for i in range(4):
    a = tk.Button(text = f"{option[i]}", width = 4, height = 1, font = ("Times New Roman", 30))
    a.bind("<1>", button_click)
    a.grid(row = 1, column = i)


for i in range(4):
    a = tk.Button(text = f"{enzansi[i]}", width = 4, height = 1, font = ("Times New Roman", 30))
    a.bind("<1>", button_click)
    a.grid(row = i + 2, column = 3)

for i in range(9, -3,-1):
    if (i == 0):
        a = tk.Button(text = f"{i}", width = 4, height = 1, font = ("Times New Roman", 30))
        a.bind("<1>", button_click)
        a.grid(row = 5, column = 1)
    
    elif (i == -1):
        a = tk.Button(text = "=", width = 4, height = 1, font = ("Times New Roman", 30))
        a.bind("<1>", button_click)
        a.grid(row = 5, column = 2)

    elif (i == -2):
        a = tk.Button(text = ".", width = 4, height = 1, font = ("Times New Roman", 30))
        a.bind("<1>", button_click)
        a.grid(row = 5, column = 0)
        
    else :
        a = tk.Button(text = f"{i}", width = 4, height = 1, font = ("Times New Roman", 30)) 
        a.bind("<1>", button_click)
        a.grid(row = 2 + (9 - i) // 3, column = (9 - i) % 3)
   

dentaku.mainloop()
