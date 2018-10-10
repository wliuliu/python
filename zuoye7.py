from tkinter import *
import PIL
from PIL import Image,ImageTk

root=Tk()
root.geometry('800x800')
root.title("人脸检测")
root.resizable(0,0)

frame1=Frame(root,width=400,height=510,bg='white',bd=2,relief=RAISED)
frame1.grid(row=0,column=0)

frame2=Frame(root,width=400,height=510,padx=20,pady=5,bg='white',bd=2,relief=RAISED)
frame2.grid(row=0,column=2)

label1=Label(root,text='图片路径',fg='black')
label1.grid(row=89,column=0,padx=20,sticky=W)

label1=Label(root,text='',fg='black')
label1.grid(row=89,column=1,padx=20,sticky=W)

label2 = Label(root,text='请选择一张图片！',padx=20,pady=5,fg='green')
label2.grid(row=89,column=2,padx=20,sticky=W)


entry=Entry(root,width=20,bg='white')
entry.grid(row=89,column=0,padx=20,pady=5)

menu=Menu(root)
menu.add_command(label='颜值排行榜')
root['menu']=menu

button=Button(root,text='选择图片',bg='pink',fg='black')
button.grid(row=99,column=0,padx=20,pady=5)

button=Button(root,text='检测',padx=20,pady=5,bg='pink',fg='black')
button.grid(row=99,column=2,padx=20,pady=5)

img=PIL.Image.open('D:\Kingsoft\JX3HD\bin\zhcn_hd\DCIM\2017-11-14_21-38-31-000.jpg')
img.thumbnail((500,500))

originImage=ImageTk.PhotoImage(img)
label_img=Label(frame1,image=originImage)
label_img.grid(row=1,column=0,columnspan=2)



mainloop()
