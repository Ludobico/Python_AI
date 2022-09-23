# print('hello, world')
#
# a = 10
# print(id(a))
#
# b = [{1: '123'},{2: 'qwewqe'}]
# print(type(b))
#
# print('hello' + 'Python')
# print('hello', 'Python')
# print('[%10d]' %123)
# print('이름은 {}입니다.'.format('이기자'))
# print('{1} 점수는 {0}점입니다. {0}점'.format(100, '수학'))
# print('[{:15,}]'.format(1234567890))
#
# abc = [10,20,30,40,50,60,'sad','qwe','zxc']
# print('asdsad',abc.index(20))
# print('asd{}asd'.format(abc.index('sad')))

# grade = float(input('총 평점을 입력해라: '))
#
# if grade >= 4.3:
#     print('니는 장학금이다\n축하')
# else:
#     print('ㄲㅈ')

# data = int(input('숫자를 입력해라:'))
#
# if data % 2 == 0:
#     print('짝수다')
# else:
#     print('홀수다')

# score = int(input('총점을 입력해라: '))
# if score >= 90:
#     print('수')
# elif 80 <= score < 90:
#     print('우')
# elif 70 <= score < 80:
#     print('미')
# elif 60 <= score < 70:
#     print('양')
# else:
#     print('가')

# count = 1 #초기식
# total = 0
# while count <= 100: #조건식
#     total = total + count #반복처리할 내용
#     count = count + 1 #증감식
# print('1부터 100까지의 합은:', total)

# count = 1
# result = 0
# while count <= 100:
#     result = result + count
#     count = count + 1
# else:
#     print('덧셈 끝남')
# print('1부터 100까지의 합은:', result)

# a = [1,2,3,4]
# result = [num * 3 for num in a if num % 2 == 0]
# print(result)

# def exp_2(a):
#     return a*a
#
# print(list(map(exp_2, [1,2,3])))

# import math
#
# print(math.sin(math.pi))

# def message(val):
#     print('hello, {0}'.format(val))
#
# if __name__ == '__main__':
#     message('python')
#     message('java')
#     message('c++')

#가변 매개변수
# def add(a, *b):
#     hap = a
#     for val in b:
#         hap += val
#     return hap
#
#
# print(add(10, 20, 30))
# print(add(10, 20, 30, 40))
#
# def func(*b):
#     a = 0
#     for i in b:
#         a += i
#     return a
#
# print(func(10,20,30))

#정의되지 않은 매개변수
# def add(a, **b):
#     hap = a
#     for val in b:
#         hap += b[val]
#     return hap
#
#
# print(add(10, mbc=20, kbs=30))

#스코프
# def circle_area(r):
#     result = 3.14 * (r ** 2)
#     return result
#
# if __name__ == '__main__':
#     radius = 3
#     area = circle_area(radius)
#     print('반지름: {0}, 면적: {1}'.format(radius, area))

# pi = 3.1415
#
# def circle_area_with_pi(r):
#     pi = 3.14
#     result = pi * (r ** 2)
#     return result
#
# def circle_area_without_pi(r):
#     result = pi * ( r ** 2)
#     return result
#
# def sum_areas():
#     results = [circle_area_with_pi(3), circle_area_without_pi(3)]
#     return sum(results)
#
# if __name__ == "__main__":
#     print('PI: ', pi)
#     print('반지름:',3, '면적:',circle_area_with_pi(3))
#     print('반지름:',3, '면적:',circle_area_without_pi(3))
#     print(sum_areas())

#람다 함수
# add = lambda a, b : a + b #람다 함수 정의
# print(add(10,20))

# def circle_area(radius, print_format):
#     area = 3.14 * (radius ** 2)
#     print_format(area)
#
# if __name__ == '__main__':
#     circle_area(3, lambda x: print('결과값:', round(x, 1)))
#     circle_area(3, lambda x: print('결과값:', round(x, 2)))

#클래스 정의
# class person:
#     def __init__(self, hakbun, irum):
#         self._hakbun = hakbun
#         self._irum = irum
#         print('객체 생성')
#     def setHakbun(self, hakbun):
#         print('학번 변경 {0} =>'.format(self._hakbun),end='')
#         self._hakbun = hakbun
#         print(' {0}'.format(self._hakbun))
#     def setIrum(self, irum):
#         print('이름 변경 {0} =>'.format(self._irum), end='')
#         self._irum = irum
#         print('{0}'.format(self._irum))
#     def printData(self):
#         print('===========================================')
#         print('학번: ',self._hakbun, '이름: ',self._irum)
#         print('===========================================')
#     def __del__(self):
#         print('객체 소멸')
#
# if __name__ == '__main__':
#     mainhakbun = input('학번을 입력해라: ')
#     mainirum = input('이름을 입력해라: ')
#     obj = person(mainhakbun, mainirum)
#     obj.setHakbun('A001')
#     obj.setIrum('이기자')
#     obj.printData()

# class car:
#     def __init__(self):
#         self.price = 2000
#         self._speed = 0
#         self.__color = 'red'
#     def get_color(self):
#         return self.__color
#     def set_color(self, color):
#         self.__color = color
#
# if __name__ == '__main__':
#     my_car = car()
#     print(my_car.price)
#     print(my_car._speed)
#     print(my_car.get_color())
#     my_car.set_color('blue')
#     print(my_car.get_color())

# class car:
#     def __init__(self):
#         self._price = 0
#         self._speed = 0
#         self._color = None
#     def get_price(self):
#         return self._price
#     def set_price(self,value):
#         self._price = value
#     def get_speed(self):
#         return self._speed
#     def set_speed(self,value):
#         self._speed = value
#     def get_color(self):
#         return self._color
#     def set_color(self,value):
#         self._color = value
#
# if __name__ == "__main__":
#     my_car = car()
#     my_car.set_price(2000)
#     my_car.set_speed(20)
#     my_car.set_color('red')
#     print('가격:',my_car.get_price())
#     print('속도:',my_car.get_speed())
#     print('색상:',my_car.get_color())

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getName(self):
        print('내 이름은 {0}이다.'.format(self.name))
    def getAge(self):
        print('내 나이는 {0}이다.'.format(self.age))

class student(person):
    def __init__(self,name,age,grade):
        super().__init__(name, age)
        self.grade = grade
    def getGrade(self):
        print('제 학점은 {0}입니다.'.format(self.grade))

if __name__ == '__main__':
    obj = student('이기자',27,3.3)
    obj.getName()
    obj.getAge()
    obj.getGrade()
