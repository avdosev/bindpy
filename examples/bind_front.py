from bindpy import *


def add(a, b, c=0):
    return a + b + c


add_10 = bind_front(add, 10)
result = add_10(20, c=30)
print(result)  # 60

add_20_30 = bind_front(add, 20, 30)
result = add_20_30()
print(result)  # 50
