def input_num():
    num1 = int(input('숫자를 입력해라: '))
    num2 = int(input('숫자를 입력해라2: '))
    return num1,num2

def minmax_num(num1,num2):
    if num1 > num2:
        maxnum = num1
        minnum = num2
    else:
        maxnum = num2
        minnum = num1
    return minnum,maxnum

def gugudan(minnum,maxnum):
    print()
    for dan in range(minnum, maxnum + 1):
        print('** {0}단 '.format(dan), end='')
    print()
    for i in range(1,10):
        for dan in range(minnum, maxnum + 1):
            print('{0} * {1} = {2}'.format(dan, i , dan * i),end = ' ')
        print()


if __name__ == '__main__':
    num1, num2 = input_num()
    minnum, maxnum = minmax_num(num1, num2)
    gugudan(minnum,maxnum)