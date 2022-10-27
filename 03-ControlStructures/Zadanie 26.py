from pickle import FALSE, TRUE
from signal import pause
from tkinter import END


PIN = "0805"

def check():
    x = input("Enter PIN code: ")
    if x==PIN: return TRUE
    else: print("Incorrect...")

for i in range(1,4,1):
    check()
    if TRUE: break
    else: i=i+1