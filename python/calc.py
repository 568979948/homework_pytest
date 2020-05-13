#!/usr/bin/env python
# type hints 类型提示
class Calc:

    def add(self, a: int, b: int):
        try:
            c= a+b
            return c
        except Exception as e:
            return "Exception: "+str(e)

    def sub(self, a: int, b: int):
        try:
            c= a-b
            print(a,b,c)
            return c
        except Exception as e:
            return "Exception: "+str(e)

    def mul(self, a: int, b: int):
        try:
            c= a*b
            return c
        except Exception as e:
            return "Exception: "+str(e)

    def div(self, a, b):
        try:
            c= a / b
            return c
        except Exception as e:
            return "Exception:"+str(e)

# aa=Calc()
# print(aa.sub('aaabbb','bbb'))