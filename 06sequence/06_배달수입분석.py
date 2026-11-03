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





"""
강사님 풀이


income = [
    3500, 8000, 1500, 11500, 6000,
    9500, 2000, 7000, 12000, 4500
]

# 1. income의 합계
total_income = 0
# for i in range(len(income)):
#     total_income += income[i]
for money in income:
    total_income += money
print(f"오늘 총 수입 : {total_income}")

total_income = sum(income)
print(f"오늘 총 수입 : {total_income}")

# 2. 평균 (평균은 명령이 없다)
total_average = total_income // len(income)
print(f"건 평균 수입 : {total_average}")

# 3. 평균보다 큰 금액만 출력
print("<평균보다 큰 금액건>")
for money in income:
    if money > total_average:
        print(f"금액 : {money}")

# 4. 5,000원 이상인 건수 (=카운트)
more5000 = 0
for money in income:
    if money >= 5000:
        more5000 += 1

print(f"5000원 이상은 총 {more5000}건 입니다")

# 5. 최대 금액건과 최소 금액건의 차이
# - 최대값 : 첫 데이터를 기준으로 삼고 더 큰 값이 존재할 때마다 갱신시켜서 전체를 반복
# - 최소값 : 첫 데이터를 기준으로 삼고 더 작은 값이 존재할 때마다 갱신시켜서 전체를 반복

max_income = income[0] # 맨 앞 금액이 가장 크다고 치자
for money in income: # 전체를 반복하면서
    # print(money, max_income)
    if money > max_income: # 더 큰 금액을 발견하면
        max_income = money # 값을 바꾼다
print(f"최대 금액은 {max_income}원 입니다")

max_income = max(income)
print(f"최대 금액은 {max_income}원 입니다")

min_income = income[0] # 맨 앞 금액이 가장 작다고 치자
for money in income: # 전체를 반복하면서
    if money < min_income: # 더 작은 금액을 발견하면
        min_income = money # 값을 바꾼다
print(f"최소 금액은 {min_income}원 입니다")

min_income = min(income)
print(f"최소 금액은 {min_income}원 입니다")

diff = max_income - min_income
print(f"최대금액과 최소금액의 차이는 {diff}원 입니다")

# 6. 10%를 공제한 금액
rate = 10
fuel = total_income * rate // 100
print(f"유류비 = {fuel}원")

real_income = total_income - fuel
print(f"실제수입 = {real_income}원")

# 7. 목표(50,000원) 달성 여부
if real_income >= 50000:
    print(f"목표 달성! 초과 금액 {real_income - 50000}원")
else :
    print(f"목표 미달.. 부족 금액 {50000 - real_income}원")

# abs - 절대값(absolute value), 부호를 제거시켜줌
gap = abs(real_income - 50000)
if real_income >= 50000:
    print(f"목표 달성! 초과 금액 {gap}원")
else :
    print(f"목표 미달.. 부족 금액 {gap}원")


# (질문) 등수를 구한다면? 등수만 저장될 리스트가 하나 더 있어야함
# income = [3500, 8000, 1500, 11500, 6000]
# ranking = [4, 2, 5, 1, 3]

ranking = []

for target in income:
    # target = income[0]
    rank = 1
    for money in income:
        if target < money:
            rank += 1
    ranking.append(rank)

print(ranking)
"""