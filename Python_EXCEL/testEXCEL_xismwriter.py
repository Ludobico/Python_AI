import xlsxwriter

#엑셀문서로 출력하기 위한 용도(읽기 불가)

workbook = xlsxwriter.Workbook('xlsxwriter1.xlsx')
ws = workbook.add_worksheet('테스트') #워크시트 추가

ws.write('A1','korea')
ws.write( 3,3,'test1')
ws.write( 4,4,'test2')
ws.write('B1', 10)
ws.write('B2', 20)
ws.write('B3', '=sum(B1:B2)')
ws.write('A2','fighting')

workbook.close()
