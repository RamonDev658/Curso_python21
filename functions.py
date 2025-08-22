#Functions

#Range 
import time


lista = list(range(5))
lista = list(range(1,6))
lista = list(range(6, 0, -1))


print(lista)

for i in range(5, 0, -1):
    print(i, end='\r')
    time.sleep(1)
