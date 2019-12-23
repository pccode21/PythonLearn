import PythonMagick
import tkinter
img=PythonMagick.Image('/eclipse-workspace/pictures/LOGO.jpg')
img.sample('128x128')
img.write('/eclipse-workspace/pictures/LOGO.ico')
win=tkinter.Tk()
win.title("")
win.geometry('250x250') 
win.iconbitmap('/eclipse-workspace/pictures/LOGO.ico')
win.mainloop()