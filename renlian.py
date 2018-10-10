##from tkinter import *
##root=Tk()
##root.geometry('800x600')
##label1=Label(root,text='你好',padx=20,pady=5,bg='blue',fg='red')#内边距
##label1.pack(side=LEFT,padx=20,pady=5)#控件布局方式：pack(),place(),grid(),外边距
##
##entry=Entry(root,width=20)
##entry.pack(side=LEFT)
##
##button=Button(root,text='点我',padx=20,pady=5,bg='blue',fg='red')
##button.pack(side=LEFT)
##
##mainloop()
###############################################################################
from tkinter import *
import PIL
from PIL import Image,ImageTk
root=Tk()
root.geometry('800x600')
label1=Label(root,text='你好',padx=20,pady=5,bg='blue',fg='red')#内边距
label1.grid(row=0,column=0,sticky=E+W)#控件布局方式：pack(),place(),grid(),外边距

entry=Entry(root,width=20)
entry.grid(row=99,column=0,padx=20,pady=5)

button=Button(root,text='点我',padx=20,pady=5,bg='blue',fg='red')
button.grid(row=0,column=1,padx=20,pady=5)

img=PIL.Image.open('D:\Kingsoft\JX3HD\bin\zhcn_hd\DCIM\2017-11-12_03-43-42-000.jpg')

img.thumbnail((500,500))

originImage=ImageTk.PhotoImage(img)
label_img=Label(root,image=originImage)
label_img.grid(row=1,column=0,columnspan=2)


menu=Menu(root)
menu.add_command(label='菜单')
root['menu']=menu

mainloop()
