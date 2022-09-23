import sqlite3

class Allgrade2:
    def mainmenu(self):
        print('**메뉴**')
        print('1. 성적정보 입력')
        print('2. 성적정보 출력')
        print('3. 성적정보 조회')
        print('4. 성적정보 수정')
        print('5. 성적정보 삭제')
        print('6. 프로그램 종료')

    def inputtype(self):
        dbconn = sqlite3.connect('grade.db')
        dbcursor = dbconn.cursor()
        self.dct = {}
        self.dct['hakbun'] = input('학번 입력 => ')
        self.dct['name'] = input('이름 입력 => ')
        try:
            self.dct['kor'] = int(input('국어 점수 입력 => '))
            self.dct['math'] = int(input('수학 점수 입력 => '))
            self.dct['eng'] = int(input('영어 점수 입력 => '))
        except ValueError:
            print('문자쓰지마라')
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
            dbcursor.execute('INSERT INTO GRADE (ID,NAME,KOR,MATH,ENG,SUM,AVG,GRADE)'
                             'VALUES (?,?,?,?,?,?,?,?)',
                             (self.dct['hakbun'],self.dct['name'],self.dct['kor'],
                             self.dct['math'],self.dct['eng'],self.dct['sum'],
                              self.dct['avg'],self.dct['grade']))
        dbconn.commit()
        dbcursor.close()
        dbconn.close()
        print('\n 성적입력함')

    def gradefunc(self):
        dbconn = sqlite3.connect('grade.db')
        dbcursor = dbconn.cursor()
        dbconn.row_factory = sqlite3.Row #fatch할때 결과를 튜플이 아니라 딕셔너리로 받음
        dbcursor.execute('SELECT * FROM GRADE')
        res = dbcursor.fetchall()
        count = 0
        allavg = dbcursor.execute('SELECT SUM(AVG)/COUNT(ID) FROM GRADE')
        allavg = dbcursor.fetchone()
        for row in res:
            print(str(row[0])+'\t'+str(row[1])+'\t'+str(row[2])+'\t'+str(row[3])
                  +'\t'+str(row[4])+'\t'+str(row[5])+'\t'+str(row[6])+'\t'+str(row[7]))
            count += 1
        print('총 학생 수:',count)
        print('평균 성적: ',allavg[0])
        dbcursor.close()
        dbconn.close()
    def f_search(self):
        dbconn = sqlite3.connect('grade.db')
        dbcursor = dbconn.cursor()
        self.hakbun = input('\n조회할 학번을 입력해라 : ')
        ressel = dbcursor.execute('SELECT * FROM GRADE')
        self.flag = 0
        for data in ressel:
            if data[0] == self.hakbun:
                print(str(data[0]) + '\t' + str(data[1]) + '\t' + str(data[2]) + '\t' + str(data[3])
                + '\t' + str(data[4]) + '\t' + str(data[5]) + '\t' + str(data[6]) + '\t' + str(data[7]))
                self.flag = 1
        if self.flag == 1:
            print('조회성공')
        else:
            print('조회실패')
        dbcursor.close()
        dbconn.close()
    def f_update(self):
        dbconn = sqlite3.connect('grade.db')
        dbcursor = dbconn.cursor()
        self.hakbun = input('\n수정할 학번을 입력해라 : ')
        self.flag = 0
        dbcursor.execute('SELECT * FROM GRADE')
        self.resup = dbcursor.fetchall()
        for data in self.resup:
            if (data[0] == self.hakbun):
                kor = int(input('국어점수를 입력해라 : '))
                math = int(input('수학점수를 입력해라 : '))
                eng = int(input('영어점수를 입력해라 : '))
                sum = kor + math + eng
                avg = sum / 3
                if avg >= 90:
                    grade = '수'
                elif 80 <= avg < 90:
                    grade = '우'
                elif 70 <= avg < 80:
                    grade = '미'
                elif 60 <= avg < 70:
                    grade = '양'
                else:
                    grade = '가'
                dbcursor.execute('UPDATE GRADE SET KOR=?,MATH=?,ENG=?,SUM=?,AVG=?,GRADE=? WHERE ID = ?',
                                 (kor,math,eng,sum,avg,grade,self.hakbun))
                dbconn.commit()
                dbcursor.close()
                dbconn.close()
                self.flag = 1
        if self.flag == 1:
            print('수정성공')
        else:
            print('\n수정할 학번 {0}가 없다\n'.format(self.hakbun))

    def f_delete(self):
        dbconn = sqlite3.connect('grade.db')
        dbcursor = dbconn.cursor()
        self.hakbun = input('\n삭제할 학번을 입력해라 : ')
        self.flag = 0
        dbcursor.execute('SELECT * FROM GRADE')
        self.resdel = dbcursor.fetchall()
        for data in self.resdel:
            if (data[0] == self.hakbun):
                dbcursor.execute('DELETE FROM GRADE WHERE ID = ?',(self.hakbun,))
                dbconn.commit()
                dbcursor.close()
                dbconn.close()
                self.flag = 1
        if self.flag == 1:
            print('삭제성공')
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
                test.inputtype()
            elif menu == 2:
                test.gradefunc()
            elif menu == 3:
                test.f_search()
            elif menu == 4:
                test.f_update()
            elif menu == 5:
                test.f_delete()
            elif menu == 6:
                print('\n 프로그램 종료')
                break
            else:
                print('메뉴를 다시 입력해라')