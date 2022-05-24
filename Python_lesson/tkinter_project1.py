import sys
from tkinter import Button, mainloop

x = Button(
    text="Нажми меня",
    command=(lambda:sys.stdout.write("Bomjur epta\n")))
x.pack()
mainloop()