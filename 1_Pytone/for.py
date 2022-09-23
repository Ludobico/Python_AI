message = 'hello!'
messages = ['hello world', '강릉원주대학교 정보기술공학과']
numbers = (1,2,3)
polygon = {'triangle':2, 'rectangle':1, 'line': 0}
color = {'red', 'green', 'blue'}
for item in message:
    print(item)
print('1.------------------------')
for item in messages:
    print(item)
    for var in item:
        print(var)
print('2.------------------------')
for item in numbers:
    print(item)
print('3.------------------------')
for item in polygon:
    print(item,'=>', polygon[item])
print('4.------------------------')
for item in color:
    print(item)
print('5.------------------------')