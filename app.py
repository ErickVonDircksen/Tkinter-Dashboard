from struct import pack
from tkinter import *
from psutil import virtual_memory
import psutil
import time
import threading



def convertBytes():
    return f'{virtual_memory().used/1024/1024/1024: .2f} GB'

def procInfo():
        return psutil.cpu_count()
    
def ramInfo():
    return f'{virtual_memory().available/1024/1024/1024: .2f} GB'

root = Tk()
root.title("DashBoard")

mem = convertBytes()
proc = procInfo()
ram = ramInfo()

VirtMemLabel = Label(root,width=10,height=4, text='Virt Mem \n used'+ mem,bg='#aaa')

procLabel = Label(root,width=10,height=4, text='nº de cpus '+ str(proc),bg='#aab')

ramLabel =  Label(root,width=10,height=4,text= 'Ram\n disponivel'+ ram,bg='#aac')

diskLabel = Label(root,width=10,height=4,text='disk')

redeLabel = Label(root,width=10,height=4,text='rede')

VirtMemLabel.grid(row=0, column=0,columnspan=1)
procLabel.grid(row=0, column=1,columnspan=1)
ramLabel.grid(row=1, column=0,columnspan=1)
diskLabel.grid(row=1, column=1,columnspan=1)
redeLabel.grid(row=1, column=2,columnspan=1)

root.mainloop()
