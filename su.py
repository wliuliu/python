def getInfo(num):
    birthdate=list(num[6:14])
    sex=num[-2]
    if int(sex)%2==0:
        gender='女'
    else:
        gender='男'
    return birthdate,gender

idNum="510603199111220974"
tuple1=getInfo(idNum)
tuple1[0].append('1111')
for i in range(len(tuple1[0])):
    tuple1[0][i]='1'
print(tuple1)
