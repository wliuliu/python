from PIL import Image
import os
im = Image.open('D:\\Kingsoft\\JX3HD\\bin\\zhcn_hd\\DCIM\\2018-02-16_14-51-39-000.jpg')
def picture(im):
    width,height = im.size
    width = 39
    height = 50
    im = im.resize((39,50))
    im.save('D:\\pythonwork\\me.jpg')
    return im
picture(im)
a = os.path.getsize('D:\\pythonwork\\me.jpg')
print(a)
if (a<10240):
    print("压缩成功")
else:
    print("压缩失败")
