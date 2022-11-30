import random
number=int(input('Введите целое положительное число: '))
number=abs(number)

arr=[]
for i in range(number):
    arr.append(int(random.randint(-1, 1)*100+random.randint(1, 10)))
print(arr)

for i in range(number):
    if arr[i]<0:
        arr.insert(i+1, 0)
print(arr)