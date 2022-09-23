def mainmenu():
    print('**메뉴**')
    print('1. 성적정보 입력')
    print('2. 성적정보 출력')
    print('3. 성적정보 조회')
    print('4. 성적정보 수정')
    print('5. 성적정보 삭제')
    print('6. 프로그램 종료')
    # menu = int(input('메뉴를 선택해라: '))
    # return menu

def inputtype(f_students):
    dct = {}
    dct['hakbun'] = input('학번 입력 => ')
    dct['name'] = input('이름 입력 => ')
    dct['kor'] = int(input('국어 점수 입력 => '))
    dct['math'] = int(input('수학 점수 입력 => '))
    dct['eng'] = int(input('영어 점수 입력 => '))
    dct['sum'] = dct.get('kor') + dct.get('math') + dct.get('eng')
    dct['avg'] = dct.get('sum') / 3
    if dct['avg'] >= 90:
        dct['grade'] = '수'
    elif 80 <= dct['avg'] < 90:
        dct['grade'] = '우'
    elif 70 <= dct['avg'] < 80:
        dct['grade'] = '미'
    elif 60 <= dct['avg'] < 70:
        dct['grade'] = '양'
    else:
        dct['grade'] = '가'

    f_students.append(dct)
    print(f_students)
    print('\n 성적입력함')

def gradefunc(f_students):
    total_avg = 0
    print('\n\t\t\t  *** 성적표 ***')
    print('===========================================================')
    print('학번   이름  국어  영어  수학  총점  평균  등급')
    print('===========================================================')
    for data in f_students:
        total_avg += data['avg']
        print('{0}    {1}  {2}  {3}  {4}  {5}   {6} {7}'
          .format(data['hakbun'],data['name'],data['kor'],data['math'],
            data['eng'],data['sum'],round(data['avg'],2),data['grade']))

    print('총학생수 = {0}, 전체 평균 = {1}'.format(len(dct), total_avg / len(dct)))

def f_search(f_students):
    hakbun = input('\n조회할 학번을 입력해라 : ')
    for data in f_students:
        if(data['hakbun'] == hakbun):
            print('{0}    {1}  {2}  {3}  {4}  {5}   {6} {7}'
                .format(data['hakbun'], data['name'], data['kor'], data['math'],
                data['eng'], data['sum'], round(data['avg'], 2), data['grade']))
            break
        else:
            print('\n 조회할 학번 {0}가 없다.'.format(hakbun))

def f_update(f_students):
    hakbun = input('\n수정할 학번을 입력해라 : ')
    for data in f_students:
        if (data['hakbun'] == hakbun):
            data['kor'] = int(input('국어점수를 입력해라 : '))
            data['eng'] = int(input('수학점수를 입력해라 : '))
            data['math'] = int(input('영어점수를 입력해라 : '))
            data['tot'] = data['kor'] + data['eng'] + data['math']
            data['avg'] = data['tot'] / 3
            if data['avg'] >= 90:
                data['grade'] = '수'
            elif 80 <= data['avg'] < 90:
                data['grade'] = '우'
            elif 70 <= data['avg'] < 80:
                data['grade'] = '미'
            elif 60 <= data['avg'] < 70:
                data['grade'] = '양'
            else:
                data['grade'] = '가'

            print('\n학번 {0} 성적정보 수정 성공 \n'.format(data['hakbun']))
            break
        else:
            print('\n수정할 학번 {0}가 없다\n'.format(hakbun))

def f_delete(f_students):
    hakbun = input('\n삭제할 학번을 입력해라 : ')
    for data in f_students:
        if (data['hakbun'] == hakbun):
            students.remove(data)
            print('\n학번 {0} 성적정보 삭제 성공 \n'.format(data['hakbun']))
            break
        else:
            print('\n삭제할 학번 {0}가 없다.'.format(hakbun))



if __name__ == '__main__':
    students = []

    while True:
        mainmenu()
        menu = int(input('\n 메뉴를 선택해라 : '))
        if menu == 1:
            inputtype(students)
        elif menu == 2:
            gradefunc(students)
        elif menu == 3:
            f_search(students)
        elif menu == 4:
            f_update(students)
        elif menu == 5:
            f_delete(students)
        elif menu == 6:
            print('\n 프로그램 종료')
            break
        else:
            print('메뉴를 다시 입력해라')