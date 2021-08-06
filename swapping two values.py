Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=6
>>> temp=a
>>> a=b
>>> b=temp
>>> a
6
>>> b
5
>>> a
6
>>> b
5
>>> a=8
>>> b=4
>>> a=a+b
>>> b=a-b
>>> a=a-b
>>> a
4
>>> b
8
>>> a,b=b,a
>>> a
8
>>> b
4
>>> Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
SyntaxError: invalid syntax
>>> a=b
>>> a=5