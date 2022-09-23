# try:
#     a = [1,2,3,]
#     print(a[4])
#     print(a[0]/0)
#
# except ZeroDivisionError:
#     print('0으로 나누지 마라')
# except IndexError:
#     print('인덱스 잘 써라')
# except:
#     print('etc error')

# 예외타입
# ValueError 유효하지 않은 값을 마주 했을 때
# TypeError  잘못된 유형의 값으로 작업이 수행될 경우
# NameError 사용하려는 변수의 이름이 아직 정의되어 있지 않을 때
# ZeroDivisionError 나눗셈 연산에서 어떤 수를 나누는 수가 0일 때
# OverflowError 산술 연산의 결과가 너무 클 때
# IndexError

# def divide(m, n):
#     try:
#         result = m / n
#     except ZeroDivisionError:
#         print('0으로 나누지 마라')
#     except:
#         print('ZeroDivisionError 이외의 에러다')
#     else:
#         return result
#     finally:
#         print('나눗셈 연산이다.')
#
# if __name__ == '__main__':
#     result = divide(3,2)
#     print(result)
#     print()
#     result = divide(3,0)
#     print(result)
#     print()
#     result = divide(None, 2)
#     print(result)

#raise 구문
# def userid(lang):
#     if lang == 'python':
#         raise Exception('파이썬')
#     print(lang)
#
# if __name__ == '__main__':
#     try:
#         userid('java')
#         userid('python')
#     except Exception as e:
#         print(e.args[0])

#사용자 정의 예외처리
class jumsuException(Exception):
    def __init__(self, msg):
        self.message = msg
def input_jumsu():
    jumsu = int(input('점수 입력 =>'))
    if jumsu < 0:
        raise jumsuException('0이상만 가능')
    elif jumsu > 100:
        raise jumsuException('100이하만 가능')
    else:
        return jumsu
if __name__ == '__main__':
    try:
        jumsu = input_jumsu()
    except jumsuException as e:
        print(e.args[0]) #self.message를 가르킴
    else:
        print('점수는 %d다.' % jumsu)