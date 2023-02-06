# bindpy

The bindpy package allows for partial application of arguments to a function, making it easy to create specialized versions of the function with some arguments pre-filled.
It is a better version of the Python's standard `partial` function from the `functools` package inspired by C++'s `std::bind`.

## Install

```
pip install bindpy
```

## Usage


```python
from bindpy import *
```

The `show` function takes three arguments, `a1`, `a2` and `a3`, and returns a string composed of their values separated by spaces. The `show_10` function is a partially applied version of `show`, with `a2` bound to `_1`, `a1` bound to `_2` and `a3` bound to `10`.

Bind support placeholders : `_1`, `_2`, ... `_10`. The placeholders allow you to partially apply a function and leave certain arguments to be filled in later. This allows you to reuse the partially applied function and pass different values for the placeholder argument.

Overall, bind and placeholders make it easier to create reusable and composable functions by allowing you to fix certain arguments and create new functions that take fewer arguments.

```python
def show(a1, a2, a3):
    return " ".join(map(str, [a1, a2, a3]))
    
show_10 = bind(show, _2, _1, a3=10)

print(show_10(20, 30)) # output: 30 20 10
```

***Convenient to use with functional style.***  

If you find lambda expressions unappealing, you can use bind for a more convenient and aesthetically pleasing experience with functional programming.

```python
def add(a, b, c):
  return a + b * c
  
numbers = [1, 2, 3, 4]
print(list(map(bind(add, _1, 10, 2), numbers))) # output 21 22 23 24
# same code with lambda
print(list(map(lambda x: add(x, 10, 2), numbers)))
```

```python
import os # used for example

files = ['a.txt', 'b.json']
my_join = bind(os.path.join, '.', 'data')
print(list(map(my_join, files))) # output ['./data/a.txt', './data/b.json']
```

