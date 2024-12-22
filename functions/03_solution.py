

def sum_all(*args):
     return sum(args)
 
 
print(sum_all(1, 2,3))
print(sum_all(3))
print(sum_all(1, 2, 3, 5))


# ==================keys values===



def print_kwargs(**kwargs):
     for key, value in kwargs.items():
         print(f"{key}- {value}")
    
print_kwargs(name='Manoj')

print_kwargs(name='Manoj', age= 23)