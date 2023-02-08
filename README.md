# bindpy

The bindpy package allows for partial application of arguments to a function, making it easy to create specialized versions of the function with some arguments pre-filled.
It is a better version of the Python's standard `partial` function from the `functools` package inspired by C++'s `std::bind`.

## Install

Expect gracefully crafted support for any version of Python 3+, but confidently tested in version 3.7 and higher.

```
pip install bindpy
```

## Usage


```python
from bindpy import *
```

### `bind` function

The `show` function takes three arguments, `a1`, `a2` and `a3`, and returns a string composed of their values separated by spaces. The `show_10` function is a partially applied version of `show`, with `a2` bound to `_1`, `a1` bound to `_2` and `a3` bound to `10`.

Bind support placeholders : `_1`, `_2`, ... `_10`. The placeholders allow you to partially apply a function and leave certain arguments to be filled in later. This allows you to reuse the partially applied function and pass different values for the placeholder argument.

Overall, `bind` and placeholders make it easier to create reusable and composable functions by allowing you to fix certain arguments and create new functions that take fewer arguments.

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
### `bind_front` function

`bind_front` pre-specifies function arguments like `functools.partial`. It takes a function and values, returns new function with values bound to front. When called with remaining args, values passed to `bind_front` are automatically inserted in front.

```python
def add(a, b, c=0):
    return a + b + c


add_10 = bind_front(add, 10)
result = add_10(20, c=30)
print(result)  # 60

add_20_30 = bind_front(add, 20, 30)
result = add_20_30() # call add(20, 30)
print(result)  # 50
```

### `bind_back` function

`bind_back` also pre-specifies function arguments but with values bound to end of arg list after all others. It takes a function and key-value pairs, returns new function with values bound to end. When called with remaining args, values passed to `bind_back` are automatically inserted at end.

```python
add_30 = bind_back(add, c=30)
result = add_30(10, 20)
print(result)  # 60

add_40 = bind_back(add, 40)
result = add_40(10, 20) # call add(10, 20, 40)
print(result)  # 70

add_10 = bind_back(add, 10)
result = add_10(12)  # call add(10, 12), c=0 by  default
print(result)  # 22
```

### Sequential binding

You can combine `bind_front` and `bind_back` to create a function that has arguments pre-specified at both the front and end of the argument list. 
For example, the code:
```python
def func(p1, p2, p3, p4, p5):
    return " ".join(map(str, [p1, p2, p3, p4, p5]))
    
b_func = bind_front(bind_back(func, 4, 5), 1, 2)
print(b_func(3)) # 1 2 3 4 5
```

can be replaced with:

```python
b_func_v2 = bind(func, 1, 2, _1, 4, 5) # using placeholder *_1*
print(b_func_v2(3)) # 1 2 3 4 5
```

----

We hope this information helps you effectively use the bind functions in your project. If you have any questions or feedback, please reach out to us. Happy coding!

----

## Acknowledgements

We would like to express our sincere gratitude to all the individuals who have made this project a reality. Their contributions, guidance, and support have been invaluable. Thank you to everyone who has played a part in bringing this project to life.

* [Daniil Dudkin](https://github.com/unterumarmung)
* ChatGPT
