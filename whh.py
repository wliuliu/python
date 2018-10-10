import random
x=list(range(0,10))
for m in range(65,91):
    x.append(chr(m))
for n in range(97,123):
    x.append(chr(n))
y=""
for g in range(10):
    for i in range(8):
        y=y+str(random.choice(x))
print("{}".format(y))
