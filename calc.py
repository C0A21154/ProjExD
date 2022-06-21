import tkinter as tk
import tkinter.messagebox as tkm
from turtle import right

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, f"{txt}")
    tkm.showinfo(txt, f"{txt}のボタンがクリックされました")

dentaku = tk.Tk()
dentaku.title("電卓")
dentaku.geometry("300x600")

entry = tk.Entry(dentaku, width = 10, justify = 'right', font = ("Times New Roman", 40))
entry.grid(columnspan = 10)

for i in range(9, -2,-1):
    if (i == -1):
        a = tk.Button(text = "+", width = 4, height = 2, font = ("Times New Roman", 30))
    
    else :
        a = tk.Button(text = f"{i}", width = 4, height = 2, font = ("Times New Roman", 30)) 
        
    a.bind("<1>", button_click)
    a.grid(row = 1 + (9 - i) // 3, column = (9 - i) % 3)

dentaku.mainloop()
