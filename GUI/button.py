
import tkinter
from tkinter import ttk


def main():
    root = tkinter.Tk()

    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    go_forward_button = ttk.Button(frame1, text='Forward')
    go_forward_button.grid()

    root.mainloop()
    
main()