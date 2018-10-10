try:
    a=input("你可以输入一些英文字母、数字、空格、字符：\n")
    g=len(a)
    zimu=0
    number=0
    kongge=0
    zifu=0
    for i in a:
        if 65<=ord(i)<=90 or 97<=ord(i)<=122:
            zimu=zimu+1
        if ord(i)>=48 and ord(i)<=57:
            number=number+1
        elif ord(i)==32:
            kongge=kongge+1
        else:
            zifu=g-number-zimu-kongge
        
    print("英文字母个数{:},数字个数{:},空格数{:},字符个数{:}".format(zimu,number,kongge,zifu))

except:
    print("输入错误")
