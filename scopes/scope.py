
x =99

# def func():
#      global x  # not good practice
#      x=12

# func()

# print(x)


def f1():
     x=12
     def f2():
          print(x)
     return f2

myresult =  f1()
myresult()   # closure
print("My result: ")
 