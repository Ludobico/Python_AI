class Allgrade2:
    def mainmenu(self):
        print('**메뉴**')
        print('1. 성적정보 입력')
        print('2. 성적정보 출력')
        print('3. 성적정보 조회')
        print('4. 성적정보 수정')
        print('5. 성적정보 삭제')
        print('6. 프로그램 종료')

    def inputtype(self,students):
        self.dct = {}
        self.dct['hakbun'] = input('학번 입력 => ')
        self.dct['name'] = input('이름 입력 => ')
        try:
            self.dct['kor'] = int(input('국어 점수 입력 => '))
            self.dct['math'] = int(input('수학 점수 입력 => '))
            self.dct['eng'] = int(input('영어 점수 입력 => '))
        except ValueError:
            print('문자쓰지마라')
            test.inputtype(students)
        else:
            self.dct['sum'] = self.dct.get('kor') + self.dct.get('math') + self.dct.get('eng')
            self.dct['avg'] = self.dct.get('sum') / 3
            if self.dct['avg'] >= 90:
                self.dct['grade'] = '수'
            elif 80 <= self.dct['avg'] < 90:
                self.dct['grade'] = '우'
            elif 70 <= self.dct['avg'] < 80:
                self.dct['grade'] = '미'
            elif 60 <= self.dct['avg'] < 70:
                self.dct['grade'] = '양'
            else:
                self.dct['grade'] = '가'

            students.append(self.dct)
            print('\n 성적입력함')

    def gradefunc(self,students):
        self.total_avg = 0
        print('\n\t\t\t  *** 성적표 ***')
        print('===========================================================')
        print('학번   이름  국어  영어  수학  총점  평균  등급')
        print('===========================================================')
        for data in students:
            self.total_avg += data['avg']
            print('{0}    {1}  {2}  {3}  {4}  {5}   {6} {7}'
              .format(data['hakbun'],data['name'],data['kor'],data['math'],
                data['eng'],data['sum'],round(data['avg'],2),data['grade']))

        print('총학생수 = {0}, 전체 평균 = {1}'.format(len(students), self.total_avg / len(students)))

    def f_search(self,students):
        self.hakbun = input('\n조회할 학번을 입력해라 : ')
        for data in students:
            if(data['hakbun'] == self.hakbun):
                print('{0}    {1}  {2}  {3}  {4}  {5}   {6} {7}'
                    .format(data['hakbun'], data['name'], data['kor'], data['math'],
                    data['eng'], data['sum'], round(data['avg'], 2), data['grade']))
                break
            else:
                print('\n 조회할 학번 {0}가 없다.'.format(self.hakbun))

    def f_update(self,students):
        self.hakbun = input('\n수정할 학번을 입력해라 : ')
        for data in students:
            if (data['hakbun'] == self.hakbun):
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
                print('\n수정할 학번 {0}가 없다\n'.format(self.hakbun))

    def f_delete(self,students):
        self.hakbun = input('\n삭제할 학번을 입력해라 : ')
        for data in students:
            if (data['hakbun'] == self.hakbun):
                students.remove(data)
                print('\n학번 {0} 성적정보 삭제 성공 \n'.format(data['hakbun']))
                break
            else:
                print('\n삭제할 학번 {0}가 없다.'.format(self.hakbun))



if __name__ == '__main__':
    students = []

    while True:
        test = Allgrade2()
        test.mainmenu()
        try:
            menu = int(input('\n 메뉴를 선택해라 : '))
        except ValueError:
            print('문자쓰지 마라')
        else:
            if menu == 1:
                test.inputtype(students)
            elif menu == 2:
                test.gradefunc(students)
            elif menu == 3:
                test.f_search(students)
            elif menu == 4:
                test.f_update(students)
            elif menu == 5:
                test.f_delete(students)
            elif menu == 6:
                print('\n 프로그램 종료')
                break
            else:
                print('메뉴를 다시 입력해라')