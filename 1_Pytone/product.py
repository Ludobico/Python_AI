def mainmenu():
    print('**메뉴**')
    print('1. 제품정보 입력')
    print('2. 제품정보 출력')
    print('3. 제품정보 조회')
    print('4. 제품정보 수정')
    print('5. 제품정보 삭제')
    print('6. 프로그램 종료')

def inputtype(f_products):
    dct = {}
    dct['code'] = input('제품코드 입력 => ')
    dct['name'] = input('제품명 입력 => ')
    dct['amount'] = int(input('수량 입력 => '))
    dct['price'] = int(input('단가 입력 => '))
    dct['sum'] = dct['amount'] * dct['price']

    f_products.append(dct)
    print('\n 제품입력함')

def gradefunc(f_products):
    total_avg = 0
    print('\n\t\t\t  *** 제품 ***')
    print('===========================================================')
    print('제품코드   제품명  수량  단가  총액')
    print('===========================================================')
    for data in f_products:
        print('{0}    {1}  {2}  {3} {4}'
          .format(data['code'],data['name'],data['amount'],data['price'],
            data['sum']))

def f_search(f_products):
    code = input('\n조회할 제품코드를 입력해라 : ')
    for data in f_products:
        if(data['code'] == code):
            print('{0}    {1}  {2}  {3} {4}'
                  .format(data['code'], data['name'], data['amount'], data['price'],
                          data['sum']))
            break
        else:
            print('\n 조회할 코드 {0}가 없다.'.format(code))

def f_update(f_products):
    code = input('\n수정할 제품코드를 입력해라 : ')
    for data in f_products:
        if (data['code'] == code):
            data['code'] = input('제품코드 입력 => ')
            data['name'] = input('제품명 입력 => ')
            data['amount'] = int(input('수량 입력 => '))
            data['price'] = int(input('단가 입력 => '))
            data['sum'] = data['amount'] * data['price']

            print('\n제품코드 {0} 정보 수정 성공 \n'.format(data['code']))
            break
        else:
            print('\n수정할 제품코드 {0}가 없다\n'.format(code))

def f_delete(f_products):
    code = input('\n삭제할 제품코드를 입력해라 : ')
    for data in f_products:
        if (data['code'] == code):
            products.remove(data)
            print('\n제품코드 {0} 정보 삭제 성공 \n'.format(data['code']))
            break
        else:
            print('\n삭제할 제품코드 {0}가 없다.'.format(code))



if __name__ == '__main__':
    products = []

    while True:
        mainmenu()
        menu = int(input('\n 메뉴를 선택해라 : '))
        if menu == 1:
            inputtype(products)
        elif menu == 2:
            gradefunc(products)
        elif menu == 3:
            f_search(products)
        elif menu == 4:
            f_update(products)
        elif menu == 5:
            f_delete(products)
        elif menu == 6:
            print('\n 프로그램 종료')
            break
        else:
            print('메뉴를 다시 입력해라')
