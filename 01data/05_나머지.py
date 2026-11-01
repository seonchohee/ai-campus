# 나머지 연산 (%)

print(10 % 3)
print(10 % 5) # 나누어 떨어진다 (=배수 확인)

# (ex) 지폐 개수 구하기
#(//는 몫)
money = 37600
won10000 = money // 10000
# money = money % 10000 #덮어쓰기
money %= 10000 #줄여서
won5000 = money // 5000
money %= 5000
won1000 = money // 1000
money %= 1000
won500 = money // 500
money %= 500
won100 = money // 100

print("만원짜리", won10000)
print("오천원짜리", won5000)
print("천원짜리", won1000)
print("오백원짜리", won500)
print("백원짜리", won100)