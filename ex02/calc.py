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
        entry.insert(tk.END, ans)

    entry.insert(tk.END, txt)

def enter():
    ans = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, ans)

dentaku = tk.Tk()
dentaku.title("電卓")
dentaku.geometry("392x460")
enzansi = ["÷", "×", "-", "+"]
option = [" ","%", "C", "AC"]

entry = tk.Entry(dentaku, width = 15, justify = 'right', font = ("Times New Roman", 35))
entry.grid(columnspan = 10)

for c,i in enumerate(["","%","C","AC",7,8,9,"÷",4,5,6,"×",1,2,3,"-",".",0,"=","+"]):
        button=tk.Button(dentaku,
                      text=f"{i}",
                      width=4,
                      height=1,
                      font=("Times New Roman",3))
        button.bind("<1>",button_click)
        x=c%4+1
        y=c//4+1
        button.grid(row=y,column=x)
   

dentaku.mainloop()
