Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=5
>>> id(num)
1702557680
>>> id(num)
1702557680
>>> id(name)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    id(name)
NameError: name 'name' is not defined
>>> name='dheeraj\'
SyntaxError: EOL while scanning string literal
>>> name='dheeraj'
>>> id(name)
24493344
>>> a=b
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a=b
NameError: name 'b' is not defined
>>> a=10
>>> b=a
>>> a
10
>>> b
10
>>> a=b
>>> a
10
>>> b
10
>>> i(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    i(a)
NameError: name 'i' is not defined
>>> id(a)
1702557760
>>> id(b)
1702557760
>>> id(10)
1702557760
>>> id(dheeraj)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    id(dheeraj)
NameError: name 'dheeraj' is not defined
>>> id('dheeraj')
24493344
>>> c=9
>>> a
10
>>> b
10
>>> c
9
>>> d=8
>>> d=c
>>> c
9
>>> d
9
>>> d=c
>>> d
9
>>> c=8
>>> id(9)
1702557744
>>> id(d)
1702557744
>>> d=c
>>> d
8
>>> id(9)
1702557744
>>> id(b)
1702557760
>>> id(d)
1702557728
>>> id(c)
1702557728
>>> #we cannot change variables to constants in python. Generally variables are mutable and constants are immutable. But in python we can change the constants too. So we can show our intention not to change by using capital letters
>>> PI=3.14
>>> PI
3.14
>>> type(name)
<class 'str'>
>>> type(num)
<class 'int'>
>>> type(s)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    type(s)
NameError: name 's' is not defined
>>> type(a)
<class 'int'>
>>> type('dheeraj')
<class 'str'>
>>> type(10)
<class 'int'>
>>> 3.14