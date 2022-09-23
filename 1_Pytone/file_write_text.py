# fp = open('text.txt', 'wt', encoding='utf-8')
# fp.write('%d\n' % 1)
# fp.write('%.2f\n'  %3.14)
# fp.write('hello world\n')
# fp.write('ㅎㅇ')
# fp.close()

##read 사용
# fp1 = open('text.txt', 'rt', encoding='utf-8')
# contents = fp1.read()
# print(contents)
# fp1.close()

#readline 사용
# fp2 = open('text.txt', 'rt', encoding='utf-8')
# line = fp2.readline() ##한줄씩 읽음
# print(line.strip()) ##strip이 있으면 맨 끝에 \n을 제거함
# line = fp2.readline()
# print(line.strip())
# line = fp2.readline()
# print(line.strip())
# line = fp2.readline()
# print(line.strip())
# fp2.close()

#readline while문 사용
# fp3 = open('text.txt', 'rt', encoding='utf-8')
#
# while True:
#     line = fp3.readline()
#     if line == '':
#         break
#     print(line.strip()) # 또는 print(line, end='')
# fp3.close()

#readlines 사용
# fp4 = open('text.txt','rt',encoding='utf-8')
# lines = fp4.readlines()
# print(lines) # ['1\n', '3.14\n', 'hello world\n', 'ㅎㅇ']
# fp4.close()

#readlines for문 사용
# fp5 = open('text.txt', 'rt', encoding='utf-8')
# lines = fp5.readlines()
# linecount = 0
#
# for forline in lines:
#     print(forline, end='')
#     linecount += 1
# print('\n총 개행 수 :',linecount)
# fp5.close()
