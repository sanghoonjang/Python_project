# Set a function


# lambda ( Instant function )
lambda argument: Expression

# Conprehension 
str_speeds = "38 42 20 40 39"
speeds = [int(s) for s in str_speeds.split()]
speeds # [38, 42, 20, 40, 39]

str_speeds2 = "38 42 20 40 a1 39"
speeds2 = [int(s) for s in str_speeds2.split() if s.isdigit()]
speeds2 # [38, 42, 20, 40, 39]

dic = {1:"apple",
       2:"banana",
       3:"orange",
       4:"kiwi"}
fru = {val:key for key, val in dic.items()}
fru # {'apple': 1, 'banana': 2, 'orange': 3, 'kiwi': 4}

li = ["DUCK", "CAT", "dog"]
ani = {x.lower() for x in li}
ani # {'cat', 'dog', 'duck'}


# Iterator
for c, l in enumerate(open("test.txt")):
       print(l, end=" ")
       if c == 3:
              break

              
# Generator
i = (x**2 for x in range(1, 10))
print(next(i)) # 1
print(next(i)) # 4
print(next(i)) # 9


# Higher-order Function
def logger(func):
       def inner(*args):
              print("argument :", args)
              return func(*args)
       return inner

def accumulate(a, b):
       return a+b

newfunc = logger(accumulate)
print(newfunc(1,2)) # argument : (1,2)
                    # 3
       
@logger # Decorator
def accumulate(a, b):
       return a+b


