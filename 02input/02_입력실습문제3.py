"""
할인 가격 계산하기 (`02_입력실습문제3.py`)

상품의 원래 가격과 할인율을 입력받아 할인 금액과 최종 가격을 출력하세요.
(단, 금액은 소수점이 나올 수 없습니다)
계산식: 할인 금액 = 원래 가격 × 할인율 ÷ 100
"""

# 입력
price = int(input("금액 입력 : "))
rate = float(input("할인율 입력 : "))

# 연산
# discount = price * rate // 100
discount = int(price * rate / 100)
# result = price * (100-rate) // 100 #비추천
result = price - discount # 추천

# 출력
print("할인금액 : ", discount)
print("최종가격 : ", result)