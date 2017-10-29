import time
t=time.time()
list=[2,4,6,8,10]
for i in list:
    print(i**2)
    print(i**3)
t2=time.time()
print(t)
print(t2)
print(t2-t)
