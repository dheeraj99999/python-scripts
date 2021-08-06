Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=2.5
>>> type(num)
<class 'float'>
>>> num=5
>>> type(num)
<class 'int'>
>>> num=6+9j
>>> num
(6+9j)
>>> type(num)
<class 'complex'>
>>> #to convert float to int
>>> if a=5.6
SyntaxError: invalid syntax
>>> a=5.6
>>> b=int(a)
>>> type(b)
<class 'int'>
>>> b
5
>>> #to convert into float
>>> k=float(b)
>>> k
5.0
>>> #to convert to complex
>>> k=6
>>> c=complex(k,b)
>>> c
(6+5j)
>>> c=complex(b)
>>> c
(5+0j)
>>> #bool(boolean)
>>>  b<k
 
SyntaxError: unexpected indent
>>> 
>>> b>k
False
>>> b<k
True
>>> Bool=b<k
>>> type(Bool)
<class 'bool'>
>>> int(True)
1
>>> int(False)
0
>>> lst=[1,2,3,4,5]
>>> type(lst)
<class 'list'>
>>> s={1,2,3}
>>> s
{1, 2, 3}
>>> type(s)
<class 'set'>
>>> t=[1,2]
>>> type(t)
<class 'list'>
>>> t=(5,6,7,8)
>>> type(t)
<class 'tuple'>
>>> str='dheeraj'
>>> type(str)
<class 'str'>
>>> st='a'
>>> type(st)
<class 'str'>
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> type(range(10))
<class 'range'>
>>> d={'dheeraj':'samsung,'rahul':'Iphone','Kiran':'mi'}
   
SyntaxError: invalid syntax
>>> d={'dheeraj':'samsung','rahul':'Iphone','Kiran':'mi'}
>>> d
{'dheeraj': 'samsung', 'rahul': 'Iphone', 'Kiran': 'mi'}
>>> d.keys()
dict_keys(['dheeraj', 'rahul', 'Kiran'])
>>> d.values()
dict_values(['samsung', 'Iphone', 'mi'])
>>> d['dheeraj']
'samsung'
>>> d.get('dheeraj')
'samsung'
>>> 