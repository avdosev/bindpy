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