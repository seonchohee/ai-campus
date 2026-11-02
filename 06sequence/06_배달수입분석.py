"""

배달기사가 하루 동안 총 8건의 배달을 완료했습니다.
각 배달의 수입은 배달 거리와 관계없이 주문마다 다르게 지급됩니다.

8건의 배달 수입을 차례대로 입력받아 리스트에 저장하고, 반복문과 조건문을 사용하여 다음 기능을 구현하세요.

요구사항
하루 동안 벌어들인 총 배달 수입을 계산하여 출력하세요.
배달 1건당 평균 수입을 계산하여 출력하세요.
평균 수입보다 높은 배달 건의 수입만 출력하세요.
배달 수입이 5,000원 이상인 건수를 구하여 출력하세요.
배달 수입이 가장 높은 건과 가장 낮은 건의 금액 차이를 계산하세요.
배달기사는 하루 수입의 10%를 오토바이 유지비로 사용합니다. 유지비를 제외한 실제 수입을 계산하세요.
하루 목표 수입이 50,000원이라면 목표까지 얼마나 부족한지 또는 얼마나 초과했는지 출력하세요.

명령 찾아서 사용하는 것과 직접 계산하여 구하는 것의 차이를 확인해보세요



"""



daily = []

for i in range(8):
    money = int(input("배달 수입  : "))
    daily.append(money)


daily_total = 0

for money in daily:
    daily_total += money

print("총 배달 수입 :", daily_total)


daily_average = int(daily_total / len(daily))

print("평균 수입 :", daily_average)


print("<평균보다 높은 배달 수입>")

for money in daily:
    if money > daily_average:
        print("수입 :", money)


count = 0

for money in daily:
    if money >= 5000:
        count += 1

print("5,000원 이상인 배달  :", count)


high = daily[0]
low = daily[0]

for money in daily:
    if money > high:
        high = money

    if money < low:
        low = money

difference = high - low

print("최고 수입 :", high)
print("최저 수입 :", low)
print("최고와 최저의 차이 :", difference)


maintenance = int(daily_total * 0.1)
real_income = daily_total - maintenance

print("오토바이 유지비 :", maintenance)
print("실제 수입 :", real_income)


target = 50000

if daily_total < target:
    print("목표까지 부족한 금액 :", target - daily_total)

elif daily_total > target:
    print("목표보다 초과한 금액 :", daily_total - target)

else:
    print("목표 수입 달성")
