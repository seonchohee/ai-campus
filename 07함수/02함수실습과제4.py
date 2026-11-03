"""
함수 실습 : 잔액과 거스름돈 개수 구하기
상품 금액과 지불한 금액을 이용해서 다음과 같은 영수증을 출력하는 함수를 만드세요

<구매 영수증>
-------------------
상품 가격 : 55750원
지불 금액 : 60000원
-------------------
거스름돈 : 4250원
 +-- 1000원짜리 4장
 +-- 100원짜리 2개
 +-- 50원짜리 1개


5만원짜리부터 개수를 검사하며, 줄 필요 없는 금액에 대해서는 출력하지 않습니다


상품 가격 : price
지불 금액 : payment
거스름돈 : change

"""

def print_receipt() :
    print("<구매 영수증>")
    print("-----------------------")
    price = int(input("상품의 가격: "))
    payment = int(input("지불 금액:"))
    change = (payment - price)
    print("-----------------------")
    print("거스름돈 :", change)

    count_50000 = change//50000
    change %= 50000
    count_10000 = change//10000
    change %= 10000
    count_5000 = change//5000
    change %= 5000
    count_1000 = change//1000
    change %= 1000
    count_500 = change//500
    change %= 500
    count_100 = change//100
    change %= 100
    count_50 = change//50
    change %= 50
    count_10 = change//10
    change %= 10

    if count_50000 > 0:
        print("+-- 50000원짜리", count_50000, "장")
    if count_10000 > 0:
        print("+-- 10000원짜리", count_10000, "장")
    if count_5000 > 0:
        print("+-- 5000원짜리", count_5000, "장")
    if count_1000 > 0:
        print("+-- 1000원짜리", count_1000, "장")
    if count_500 > 0:
        print("+-- 500원짜리", count_500, "개")
    if count_100 > 0:
        print("+-- 100원짜리", count_100, "개")
    if count_50 > 0:
        print("+-- 50원짜리", count_50, "개")
    if count_10 > 0:
        print("+-- 10원짜리", count_10, "개")


print_receipt()






