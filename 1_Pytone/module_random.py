import random

print(random.random()) # 0과 1 사이의 난수
print('------------------------------------------------')
print(random.uniform(1,10)) # 1과 10사이의 난수
print('------------------------------------------------')
print(random.randint(1,10)) # 1과 10사이의 정수형 난수
print('------------------------------------------------')
print(random.randrange(0,100,2)) # 0부터 100사이 짝수중(2증가) 하나
print('------------------------------------------------')
print(random.choice('abcdefghij'))
print('------------------------------------------------')
print(random.sample([1,2,3,4,5],3))
print('------------------------------------------------')
items = [1,2,3,4,5,6,7]
random.shuffle(items)
print(items)