Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=15
>>> b=12
>>> x=(a//4+b**3)<2000 and (b%4!=0)
>>> c
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> x
False
>>> #a//4= 15//4=3
>>> #b%4=12%4=0 so the first statement is true but second one is false so it is false