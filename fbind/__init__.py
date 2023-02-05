from .placeholder import *
from .bind import *

_1 = Placeholder(0)
_2 = Placeholder(1)
_3 = Placeholder(2)
_4 = Placeholder(3)
_5 = Placeholder(4)
_6 = Placeholder(5)
_7 = Placeholder(6)
_8 = Placeholder(7)
_9 = Placeholder(8)
_10 = Placeholder(9)

arg_1 = _1
arg_2 = _2
arg_3 = _3
arg_4 = _4
arg_5 = _5
arg_6 = _6
arg_7 = _7
arg_8 = _8
arg_9 = _9
arg_10 = _10

# used for show placeholders when a user import a package
__all__  = []
__all__ += ['_1', '_2', '_3', '_4', '_5', '_6', '_7', '_8', '_9', '_10']
__all__ += ['arg_1', 'arg_2', 'arg_3', 'arg_4', 'arg_5', 'arg_6', 'arg_7', 'arg_8', 'arg_9', 'arg_10']
__all__.append('bind')