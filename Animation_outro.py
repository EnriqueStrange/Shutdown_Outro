from tkinter import Tk, Label
from time import sleep
import os


class LoadingSplash():
    def __init__(self):
        self.root = Tk()
        self.root.config(bg="black")
        self.root.title("Outrow")
        self.root.attributes("-fullscreen", True)

        # Text Field
        Label(self.root, text="YOUR SYSTEM IS ABOUT TO DIE",
              font="Banschrift 15", bg="black", fg="#FFBD09").place(x=490, y=320)

        # Loading Block
        for i in range(16):
            Label(self.root, bg="#1F2732", width=2,
                  height=1).place(x=(i+25)*22, y=380)

       # Updating root to make animation
        self.root.update()
        self.play_animation()

        self.root.mainloop()

    # Loading Animation
    def play_animation(self):
        for i in range(7):
            for j in range(16):
                Label(self.root, bg="#FFBD09", width=2,
                      height=1).place(x=(j+25)*22, y=380)
                sleep(0.06)
                self.root.update_idletasks()
                # Make Block Dark
                Label(self.root, bg="#1F2732", width=2,
                      height=1).place(x=(j+25)*22, y=380)
        else:
            #os.system("shutdown /s /t 1")
            self.root.destroy()
            exit(0)


if __name__ == "__main__":
    LoadingSplash()
