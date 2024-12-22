def mul(n1, n2):
    return n1*n2

res = mul(2, 'h')
res = mul('a', 2)

print(res)


====Multi values return
import math
def res(radius):
    area=radius*radius
    cum=2*area
    return area, cum

a, c = res(2)

def greet(name='user'):
print("hello"+name+" , Good morning")



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