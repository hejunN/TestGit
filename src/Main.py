# _*_ coding: utf-8 _*_
# @Time     :2020/12/14 11:41
# @Author   :HE JUN
# @File     :Main.py

import numpy as np
import functools
print(np.info)


def op(f):
    def wrap(arg):
        print("do some thing")
        f(arg)
        print("do other thing")
    return wrap

@op
def test(arg):
    print("say hello".format(arg))

test("heun")