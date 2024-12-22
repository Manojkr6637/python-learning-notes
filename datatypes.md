# Object types / data types

-Number: 1234, 2.3, 3+4k, 0b111, decimal() fraction

-string : 'span', "span", "Bob's" b'a\x01c' u'sp\xc4m'
-list: [1, 2, [3, 4]], list(range(10))
tuple: (1, "span", 4, 'u'), tuple('span'), nametuple
-dictionary: {'food':'span'} dict(hours=10)

-set: set('abc'), {'a', 'b', 'c'}

file: open("egges.txt")
boolean: True, FALSE
functions, modules, classes

advance: Decorators, Generators, Iterators
 Metaprogrammming

 **->power
 import math
 import random
 math.pi
 random.random(10)

random.choice([1, 2,3, 4,5])
username="chaiaurcode"
username[0]='A'->X

username[0]// beg
username[-1]//last
username[-2]
username[1:3] start and end
dir(username)
array sstrat with 0 index

#list same like array
 mylist=[123, "hello", 3.14]
 len(mylist)

 # dictionary
  myd={"name":"Manoj", 'age':'20'}
  myd["name"]

  # tupbles
  mytuple=(1, 2, 3)

  mytuple[0]

  # advance
  l1=[1, 2, 3]
  l2=l1// reference
  l2=l1[:]// copy
print(l1)->[1, 2, 3]
print(l2)->[1, 2, 3]
import copy
h2=copy.copy(l1)// same l2=l1[:]
// l2=copy.deepcopy(l1)

m=[1,2,3]
n=m
m==n->true->check value
m is n->check memory reference->true

m=[1, 2, 3]
n=[1,2, 3]
m==n//true
but m is n->not true

#number-object
40+2.23->high precision
int(2.3)
float(2)
'chai'+'code'-operator overloading

repr('chai')

str('chai')
print('chai')
True-False->capital

x<y<z
x<y and y<z
or

import math
math.floor(3.5)
math.trunc(3.3)
2+1j

octa
0o20
0xFF
0b1000
oct(43)
hex(64)
bin(54)
int('54',8)
int('1000', 2)

x=1
x<<2

import random
random.ranint(1,100)
l1=['lemon',''masala']
random.choice(l1)
random.shuffle(l1)

0.1+0.1+0.1-0.3
5.551115123125783e-17
from decimal import Decimal
from fractions import Fractions
setone={1, 2, 3, 4}
setone & {1, 3}->instection
union(|)
setone | {1, 3, 5}
setone-{1, 2, 3, 4}

type({})->get data type

type(True) or type(1)

True is 1->not
True+4->5


====================
''
""
""""""
slicing:str[0:4]

num_list="0123456789"

n=num_list[:]

n1=num_list[3:]
n=num_list[:7]
n=num_list[0:7:3]

============
string
s="cahi"
s.lower();
s.strip()
s.replace("c","x")
chai="lemon, Ginger,  Masala";
chai.split('')
chai.split(",")
chai.find('chai')-> index or -1
chai.count('chia')

chai_type="Masala"
quantity = 2
order="I ordered {} cups of  chai"
order.format(quantity, chai_type)

chai_variety= ["Lemon", "Masala"]

"".join(chai_variety)
" ".join(chai_variety)
"-".join(chai_variety)
for letter in chai:
    letter

================
chai="He said, "Masala chai is awesome""->X

chai="He said, \"Masala chai is awesome\" "->work


chai="Masala\Chai"
"Masala\Chai"

chai="Masala\nChai"

chai = r"c:\user\pwd\"->r=>raw
print(chai)

chai ="Masala chai"

"Masala" in chai


List:->Array

list=["a", 'b','c']
print(list[1:2])
[2:]
[1:3]
l[1:2]="lemon"->
l1[1:3]=["abdc"]
l1[1:3]=["aa","bb"]
l1[1:1]

l1[1:3]=[]
==loop===
l=[1, 3,"abc"]
for i in l
 print(i, end='-')
 l.append("bbb")//add lat

if "abb" in l

l.pop() # last return
l.remove(1)->not restult

l.insert(1, "bbb")


l2=l1->copy reference
l2=l1.copy()

=========
squared_nums=[x** for x in range(10)]
[0, 1,4 9, 16, 26, 36, 49, 64, 81]

cube_num = [x**3 for y in range(5)]


========
Dictionalirs
chai_types={"Masala":"spicy", "Ginger":"Zensty"}
chai_types['Masala']="Heel"


for type in chai_types
   print(type(key), chai_types[key])

for key, valye in chai_types.items():
   print(key, value)

   len(chai_types)

   chai_types.pop('key')
   chai_types.popitem()

   del chai_types['key']
   chai_types_copy=chai_types.copy()


{{},{},{}}

tea_shop={

"chai":{"Masala":"Hell"},
"tea":{"green","Black"}

}
tea_shop["chai"]["Masala"]

squared_num={x:x**2 for x in range(6)}

keys=["Masala", "Ginger"]
default_value="Delicous"

new_dict=dict.fromkeys(keys, default_value)
new_dict=dict.fromkeys(keys, keys)

===tuples====
type_types=(1, ,2, 3)
type_types[0]
type_types[0]=2-X     
more_tea=(3, 4) 
all_tea=type_types+more_tea

if "green" in type_types:
   print("more tea")

 (f, s, t)=  type_types


 ==================Take input from users====
 userName=input("Enter user name:\n")


 Run:python3 solutions1.py

 if score>=101:
  print('Not valid')
  exit()

  price=12 if age>=18 else 8


  =============loops=========

  for num in numbers:
    if num===4
     continue

while n>0:
  num-=1
unique_items=set()

if item in unique_items
     break

import time
wait_time = 1
max_retires = 1
===========
Iteration tool:          iter       Iterable Objects
(for, comprehension)                  (lists, file)


__next__

ex.
  chai.py
   import time
   name = 'Manoj'
   print("Name is", name)

   ===
   run
    f = open('chai.py')

    f.readline()

    or
    f.__next__()


    for line in open('chai.py').readlines():->memory load more

      for line in open('chai.py'):
        print(line, end='')
   
   ==while loop
   f=open('chai.py')
   while True:
      line = f.readline()
      if not line: break
      print(line, end='') 

  test = 'Manoj'

  if not test:
    print('Not')



 iter()->keywords       
mylist = [1, 2, 3, 4]

I = iter(mylist)
>>I
I.__next__()

f = open('chai.py')

>>iter(f) is f
 true
>> iter(f) is f.__iter__()
true

>>iter(myNewList) is myNewList
false

eg. d = {'a':1, 'b': 2}

for  key in d.keys():
   print(key)


I = iter(d)

>>I

next()->__next()__ same

===
R  = range(5)
>>R
I = next(I)
>>I
===============functions==================

def sqaure_o_num(number):
   return n**2

result = sqaure_o_num(2)

print(result)

===lamda function============

cube = lambda x: x**3


================multiple argumets====
    def sum_all(*args):
       return sum(args)
   
   # ==================keys values===



def print_kwargs(**kwargs):
     for key, value in kwargs.items():
         print(f"{key}- {value}")
    
print_kwargs(name='Manoj')

print_kwargs(name='Manoj', age= 23)


==============yield===

def even_generator(n):
    for i in range(2, limit+1, 2)
      yield i

for num in even_generator(10):
  print(num)
============recursions========


========scopes=========
global x=99
 def f():
     x=20
     def f2():
       global x
       x=40
      


===============OOPs============
Class  Car:
   self __init__(self, name, age):
         self.name=name

   // private
     self.__name

   inheritance
   ElectricCar(Car):
      def __init__(self, height)
       super().__init__(name, age)


     // polymorphism
     Car
      def full_detail():
     ElectricCar(Car):
      def full_detail():


 

// count total object
static

not modify or update properties

use @property decorator
 Car.brand = 'Tata'//Not modified
 @staticmethod


isinstance->


print(isinstance(teslaCar, ElectricCar))



===multiple inheritance===
Yes support
===============Decorators==============
as higher functions as js



