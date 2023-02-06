import unittest
from bindpy import *


def func(p1, p2, p3, p4, p5):
    return " ".join(map(str, [p1, p2, p3, p4, p5]))


class TestBind(unittest.TestCase):
    def test_base_example(self):
        func_v2 = bind(func, 1, arg_1, 3, arg_2, 5)
        self.assertEqual(func_v2(2, 4), "1 2 3 4 5")
        self.assertEqual(func_v2(4, 2), "1 4 3 2 5")
        self.assertEqual(func_v2(2, 4), "1 2 3 4 5")

    def test_use_kwargs(self):
        func_v2 = bind(func, p4=4, p5=5)
        self.assertEqual(func_v2(1, 2, 3), "1 2 3 4 5")
        self.assertEqual(func_v2(3, 2, 1), "3 2 1 4 5")
        self.assertEqual(func_v2(1, 2, 3), "1 2 3 4 5")

    def test_use_positional_and_kwargs(self):
        func_v2 = bind(func, p4=4, p5=5)
        self.assertEqual(func_v2(1, 2, 3), "1 2 3 4 5")
        self.assertEqual(func_v2(1, 2, 3), "1 2 3 4 5")
        self.assertEqual(func_v2(1, 2, 3), "1 2 3 4 5")

    def test_use_positional_in_kwargs(self):
        pass
        # dont work
        # func_v2 = bind(func, _1, _2, _3, p4=_2, p5=_1)
        # self.assertEqual(func_v2(1, 2, 3), '1 2 3 2 1')
        # self.assertEqual(func_v2(1, 2, 3), '1 2 3 2 1')
        # self.assertEqual(func_v2(1, 2, 3), '1 2 3 2 1')

    def test_revers_positional_call(self):
        func_v2 = bind(func, _5, _4, _3, _2, _1)
        self.assertEqual(func_v2(5, 4, 3, 2, 1), "1 2 3 4 5")
        self.assertEqual(func_v2(5, 4, 3, 2, 1), "1 2 3 4 5")
        self.assertEqual(func_v2(5, 4, 3, 2, 1), "1 2 3 4 5")

    def test_sequential_binding_calls(self):
        func_v2 = bind(bind(bind(bind(bind(func, _1), _1), _1), _1), _1)
        self.assertEqual(func_v2(1, 2, 3, 4, 5), "1 2 3 4 5")
        self.assertEqual(func_v2(1, 2, 3, 4, 5), "1 2 3 4 5")
        self.assertEqual(func_v2(1, 2, 3, 4, 5), "1 2 3 4 5")

        func_v2 = bind(bind(bind(bind(bind(func, _5), _4), _3), _2), _1)
        self.assertEqual(func_v2(1, 2, 3, 4, 5), "5 4 3 2 1")
        self.assertEqual(func_v2(1, 2, 3, 4, 5), "5 4 3 2 1")
        self.assertEqual(func_v2(1, 2, 3, 4, 5), "5 4 3 2 1")

    def test_front_back_sequential_binding(self):
        func_v2 = bind_front(bind_back(func, 4, 5), 1, 2)
        self.assertEqual(func_v2(3), "1 2 3 4 5")
        self.assertEqual(func_v2(3), "1 2 3 4 5")
        self.assertEqual(func_v2(3), "1 2 3 4 5")

