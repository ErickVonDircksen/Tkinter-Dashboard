from struct import pack
from tkinter import *
from psutil import virtual_memory
import psutil
import time
import threading


def convertBytes(value):
    return f'{value/1024/1024/1024: .2f} GB'


root = Tk()
root.title("DashBoard")
p = convertBytes(virtual_memory().used)

memLabel = Label(root, text=psutil.cpu_freq())
memLabel2 = Label(root, text=p)

memLabel.grid(row=0, column=0)
memLabel2.grid(row=1, column=1)


def att(memLabel, memLabel2):
    print(time.ctime())
    threading.Timer(2, att).start()
    p = psutil.cpu_freq()

    memLabel = Label(root, text=p)
    memLabel2 = Label(root, text=p)


att(memLabel, memLabel2)
root.mainloop()
