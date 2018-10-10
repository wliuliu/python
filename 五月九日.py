from PIL import Image
img=Image.open("2017-12-30_22-33-57-000.jpg")
r,g,b=img.split()

om=Image.merge("RGB",(b,g,r))
om.save("exchange-r-b.jpg")
