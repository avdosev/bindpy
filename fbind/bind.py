from fbind.placeholder import *

def bind(fn, *args, **kwargs):
    def new_fn(*call_args, **call_kwargs):
        new_args = list(args)
        call_args = list(call_args)
        indexes = set()
        for i, arg in enumerate(new_args):
            if isinstance(arg, Placeholder):
                new_args[i] = call_args[arg.index]
                indexes.add(arg.index)
                
        for i in sorted(indexes, reverse=True):
            del call_args[i]
        
        return fn(*new_args, *call_args, **kwargs, **call_kwargs)
    return new_fn


def bind_front(fn, *bind_args, **bind_kwargs):
    """
Returns a new function that when called, will invoke the original function with any bind_args and bind_kwargs passed to bind_front being passed as positional and keyword arguments to the front of the argument list.

Parameters:
    fn (callable): The original function to be called.
    *bind_args (tuple): Positional arguments to be passed to the front of the argument list when the new function is called.
    **bind_kwargs (dict): Keyword arguments to be passed when the new function is called.

Returns:
    callable: A new function that when called, will invoke the original function with the bind_args and bind_kwargs passed to the front of the argument list.
    
```
def add(a, b, c=0):
    return a + b + c

add_10 = bind_front(add, 10)
result = add_10(20, c=30)
print(result) # 60

add_20_30 = bind_front(add, 20, 30)
result = add_20_30()
print(result) # 50
```
    """
    def new_fn(*call_args, **call_kwargs):
        return fn(*bind_args, *call_args, **bind_kwargs, **call_kwargs)

    return new_fn

def bind_back(fn, *bind_args, **bind_kwargs):
    """
Returns a new function that when called, will invoke the original function with any bind_args and bind_kwargs passed to bind_back being passed as positional and keyword arguments to the end of the argument list.

Parameters:
    fn (callable): The original function to be called.
    *bind_args (tuple): Positional arguments to be passed to the end of the argument list when the new function is called.
    **bind_kwargs (dict): Keyword arguments to be passed when the new function is called.

Returns:
    callable: A new function that when called, will invoke the original function with the bind_args and bind_kwargs passed to the end of the argument list.
    
```
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
```
    """
    def new_fn(*call_args, **call_kwargs):
        return fn(*call_args, *bind_args, **call_kwargs, **bind_kwargs)

    return new_fn