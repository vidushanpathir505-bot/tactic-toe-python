from gui import GameEngine
import tkinter as tk

def main():

    root = tk.Tk()
    app =  GameEngine(root)
    root.mainloop()

if __name__ == "__main__":
    main()