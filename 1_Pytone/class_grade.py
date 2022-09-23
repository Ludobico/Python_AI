class Allgrade:
    def inputFunc(self):
        self.hakbun = input('학번을 입력해라: ')
        self.name = input('이름을 적어라: ')
        self.kor = int(input('국어점수를 적어라: '))
        self.eng = int(input('영어점수를 적어라: '))
        self.math = int(input('수학점수를 적어라: '))
        print('입력완료')
    def processFunc(self):
        self.tot = self.kor + self.eng + self.math
        self.avg = (self.kor + self.eng + self.math) / 3
        if self.avg >= 90:
            self.grade = '수'
        elif 90 > self.avg >= 80:
            self.grade = '우'
        elif 80 > self.avg >= 70:
            self.grade = '미'
        elif 70 > self.avg >= 60:
            self.grade = '양'
        else:
            self.grade = '가'
        print('총점,평균,등급 작업 완료')
    def outputFunc(self):
        print('================================================================')
        print('학번   이름  국어점수  영어점수      수학점수    총점수     평균    등급')
        print('{0}    {1}   {2}       {3}         {4}         {5}      {6:.2f}  {7}'
              .format(self.hakbun,self.name,self.kor,self.eng,self.math,self.tot,self.avg,self.grade))
        print('================================================================')
if __name__ == '__main__':
    test = Allgrade()
    test.inputFunc()
    test.processFunc()
    test.outputFunc()
