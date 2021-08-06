Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data={1:'dheeraj',2:'kiran',3:'harsh'}
>>> data
{1: 'dheeraj', 2: 'kiran', 3: 'harsh'}
>>> data[1]
'dheeraj'
>>> data[4]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    data[4]
KeyError: 4
>>> data.get[1]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    data.get[1]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> data.get(1)
'dheeraj'
>>> data.get(4)
>>> print(data.get(4))
None
>>> print(data.get(3))
harsh
>>> data.get(4,'Not Found')
'Not Found'
>>> data[4]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    data[4]
KeyError: 4
>>> data[3]
'harsh'
>>> data[4,'Not Given']
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    data[4,'Not Given']
KeyError: (4, 'Not Given')
>>> data(4,'NG')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    data(4,'NG')
TypeError: 'dict' object is not callable
>>> keys=['dheeraj','kiran','rahul']
>>> values=['Phython','java','JS']
>>> #to form as a dictionary
>>> data=dict(zip(keys,values))
>>> data
{'dheeraj': 'Phython', 'kiran': 'java', 'rahul': 'JS'}
>>> data[kiran]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    data[kiran]
NameError: name 'kiran' is not defined
>>> data['kiran']
'java'
>>> data['Suv']='fulstack'
>>> data
{'dheeraj': 'Phython', 'kiran': 'java', 'rahul': 'JS', 'Suv': 'fulstack'}
>>> #to del values
>>> del data['harsh']
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    del data['harsh']
KeyError: 'harsh'
>>> del data['rahul']
>>> data
{'dheeraj': 'Phython', 'kiran': 'java', 'Suv': 'fulstack'}
>>> clear
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> data.clear
<built-in method clear of dict object at 0x03C2AD98>
>>> 
>>> 
>>> 
>>> 