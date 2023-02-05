from fbind import *


def add(a, b, c=0):
    return a + b + c

add_30 = bind_back(add, c=30)
result = add_30(10, 20)
print(result) # 60

add_40 = bind_back(add, 40) 
result = add_40(10, 20)
print(result) # 70

add_10 = bind_back(add, 10) 
result = add_10(10) # c=0 by  default
print(result) # 20