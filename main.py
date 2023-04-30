import tkinter as tk
from interface import MyGui


def main():
    root = tk.Tk()
    root.geometry('200x200')
    root.title('Aplikacja pogodowa')
    gui = MyGui(root)
    root.mainloop()

if __name__ == '__main__':
    main()
