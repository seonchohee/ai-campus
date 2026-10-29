
"""영화관에서 관람객의 나이에 따라 할인율을 다르게 적용하는 프로그램을 구현하세요.
영화표의 기본 가격은 15,000원입니다.
사용자는 출생년도 4자리를 입력합니다.
계산된 나이에 따라 다음과 같이 할인율을 적용합니다.
65세 이상 : 50% 할인
20세~64세 : 할인 없음
14세~19세 : 20% 할인
8세~13세 : 40% 할인
7세 이하 : 100% 할인 (무료)

요구사항
출생년도를 입력받아 2026년 기준 한국 나이를 계산하세요.
if ~ elif ~ else를 사용하여 할인율을 결정하세요.
할인 금액을 계산하세요.
최종 결제 금액을 계산하세요.
기본 가격, 할인율, 할인 금액, 최종 결제 금액을 출력하세요.
"""



#입력
birth=int(input("출생년도:"))

#연산
age = 2026 - birth +1
base = 15000
#rate 조건에 따라 다르게 계산
if age>=65:
    rate=50
elif age>=20:
    rate=0
elif age>=14:
    rate=20
elif age>=8:
    rate=40
else:
    rate=100




discount=int(base * rate / 100)
price = base - discount





#출력

print(f"나이:{birth}세")
print(f"기본가격:{base}원")
print(f"할인율:{rate}%")
print(f"할인금액:{discount}원")
print(f"최종 결제 금액:{price}원")