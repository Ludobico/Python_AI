def minmax_input():
    num1 = int(input('숫자를 입력해라: '))
    num2 = int(input('숫자를 입력해라2: '))
    if num1 > num2:
        maxnum = num1
        minnum = num2
    else:
        maxnum = num2
        minnum = num1
    return minnum,maxnum

def primarydef(minnum,maxnum):
    count = 0
    for i in range(minnum,maxnum+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else: #소수인 경우 수행
            print('{}'.format(i),end=' ')
            count += 1
            if count % 10 == 0:
                print()
    if count % 10 != 0:
        print()
    return count

def pri_count(count):
    print('총소수의 갯수 = {}'.format(count))

if __name__ == '__main__':
    minnum,maxnum = minmax_input()
    count = primarydef(minnum,maxnum)
    pri_count(count)






