#最大公约数
import math
a=eval(input("请输入第一个数字：\n"))
b=eval(input("请输入第二个数字：\n"))
c=math.gcd(a,b)#c是公约数
print("最大公约数{:}".format(math.gcd(a,b)))
d=a*b/c
print("最小公倍数{:}".format(d))
