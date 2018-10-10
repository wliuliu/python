from tkinter import *
from tkinter import filedialog,font
import os
imoprt imghdr

def isPic(fileDir);
    fileType = imghdr.what(fileDir)
    picTypes = ['jpg','jpeg','png','bmp','tiff','ico']
    if fileType in picTypes:
        return True
    else:
        return False

def browseFile():
    fileDir=filedialog.askopenfilename(initialdir = os.curdir)
    if fileDir!='':
        if isPic(fileDir):

root = Tk()
root.resizable(0,0)
root.title('颜值排行榜')
##root.iconbitmap('b13.ico')
root.geometry('1080x620')

menu = Menu(root)
menu.add_command(label='颜值排行榜')
root['menu']=menu

originFrameBorder = Frame(root,height=500,width=500,bd=2,relief=GROOVE)
originFrameBorder.grid(row=1,column=0,sticky=W,padx=20,pady=10)

originFrame =Frame(originFrameBorder,height=500,width=500)
originFrame.pack()

resultFrameBorder = Frame(root,height=500,width=500,bd=2,relief=GROOVE)
resultFrameBorder.grid(row=1,column=1,sticky=E,padx=20,pady=10)

resultFrame= Frame(resultFrameBorder,height=500,width=500)
resultFrame.pack()

selectFrame =Frame(root,height=20,width=500)
selectFrame.grid(row=2,column=0)
imagleLabel = Label(selectFrame,text='图片路径：')
imagleLabel.grid(row=0,column=0)
imagleEntry = Entry(selectFrame,width=60)
imagleEntry.grid(row=0,column=1)
imageEntry.con

infoFrame = Frame(root,height=20,width=500)
infoFrame.grid(row=2,column=1)
infoLabel = Label(infoFrame,text='')
infoLabel.pack()

selectFileButton = Button(root,height=1,width=20,text='选择图片',command=browersrelief=RIDGE)
selectFileButton.grid(row=3,column=0,pady=10)

detectButton = Button(root,width=20,height=1,text='检测',relief=RIDGE)
detectButton.grid(row=3,column=1,pady=10)

root.mainloop()




