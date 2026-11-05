"""
# 함수 실습

파일명 : `02_함수실습.py`

다음 작업을 수행하는 함수를 만드세요

2. 분식집에서 사용할 수 있는 함수 생성
  - `show_menu` 함수를 만들어서 메뉴판을 출력
  - `show_price` 함수를 만들어서 떡볶이, 튀김, 순대 개수에 따른 계산 금액 출력

> show_menu 함수의 예상 결과
```
###################
# KH 분식집
###################
# 떡볶이 3,000원
# 튀김   2,000원
# 순대   3,500원
###################
```

이 함수를 구현하기 위해 필요한 값들을 함수에 변수로 선언한 뒤 처리해보세요
"""

def show_menu():
    print("###################")
    print("# KH 분식집")
    print("###################")
    print("# 떡볶이 3,000원")
    print("# 튀김   2,000원")
    print("# 순대   3,500원")
    print("###################")

show_menu()
show_menu()
show_menu()



"---------------------------------------------------------------------------------"

def show_price(rice, fried, sundae):
    # 이 함수에서만 사용할 변수를 얼마든지 만들 수 있다
    # 지역 변수(local variable)
    rice_total = rice * 3000
    fried_total = fried * 2000
    sundae_total = sundae * 3500
    total = rice_total + fried_total + sundae_total
    print(f"< 영수증 >")
    print(f"-------------------")
    if rice > 0 :
        print(f"떡볶이 {rice}인분 - {rice_total}원")
    if fried > 0:
        print(f"튀김 {fried}인분 - {fried_total}원")
    if sundae > 0:
        print(f"순대 {sundae}인분 - {sundae_total}원")
    print(f"--------------------")
    print(f"총 {total}원")

show_price(2, 1, 1)
print()
show_price(1, 0, 0)