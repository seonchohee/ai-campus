"""
일회용 카드를 발급하기 위한 요금을 계산하는 프로그램을 구현하세요

누구나 카드보증금 500원은 내야 합니다
사용자는 출생년도 4자리를 입력합니다
계산된 나이에 따라 요금이 달라집니다
65세 이상은 요금이 무료입니다
20세~64세는 1550원입니다
14세~19세는 900원입니다
8세~13세 450원
7세 이하는 무료입니다

최종적으로 금액이 나와야 합니다 (내역이 나오면 더좋고)
"""




#강사님풀이


# 입력
birth = int(input("출생년도(4자리) : "))

# 연산
age = 2026 - birth + 1
card = 500
# base = 0 or 450 or 900 or 1550

if age >= 20 and age < 65:
    base = 1550
elif age >= 14 and age < 20:
    base = 900
elif age >= 8 and age < 14:
    base = 450
else:
    base = 0

result = base + card

# 출력
print(f"카드보증금 : {card}원")
print(f"기본요금 : {base}원")
print(f"총 이용요금 : {result}원")
