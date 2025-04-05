from functools import reduce
a=[1,2,3,4]
#reduce() applies this operation across the list
b=reduce(lambda x, y: x * y, a) # x=1*y=2 , x=2*y=3, x=6*y=4
print(b)