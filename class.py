from tkinter import *
from tkinter import filedialog
import os
def browsFile():#增加监听器的方法
    global entry
    filePath=filedialog.askopenfilename(initialdir=os.curdir)
    entry.config(state=NORMAL)#给entry设置状态，可以编辑

    entry.delete(0,END)
    entry.inser(0,filePath)#文本替换

    entry.config(state=DISABLED)#文本框不能编辑。disable一旦设置，文本替换不可编辑

root=Tk()
root.geometry('800x600')

label_img=Label(root,bg='black')
label_img.grid(row=0,column=0)

entry=Entry(root,width=20)
entry.grid(row=99,column=0,padx=20,pady=5)

button=Button(root,text='选择图片',command=browsFile)#增加监听器
button.grid(row=2,column=0)

button2=Button(root,text='检测',padx=20,pady=5,bg='pink',fg='black')
button2.grid(row=3,column=0)

filePath=filedialog.askopenfilename(initialdir=os.curdir)#打印路径
mainloop()
