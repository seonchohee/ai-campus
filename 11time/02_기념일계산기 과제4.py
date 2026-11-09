"""
# 실습 과제 : 기념일 계산기

파일명 : `02_기념일계산기.py`

다음 요구사항에 맞는 기념일 계산기를 구현하세요

사용자가 입력한 연, 월, 일 정보를 토대로 기념일을 순차적으로 출력
(문자열 입력으로 해도 상관없습니다)

```
연도 입력 : (2026)
월 입력 : (3)
일 입력 : (19)

또는

날짜 입력 : (2026-03-19)

D + 100 : yyyy-MM-dd
D + 200 : yyyy-MM-dd
D + 300 : yyyy-MM-dd
D + 365 : yyyy-MM-dd
D + 400 : yyyy-MM-dd
D + 500 : yyyy-MM-dd
D + 600 : yyyy-MM-dd
D + 700 : yyyy-MM-dd
D + 730 : yyyy-MM-dd
```

- 사용자가 입력한 날짜부터 계산해서 100일단위와 1주년 단위(365일)를 계산해서 가까운 일자부터 출력
- 처음에는 1년만 보이게 하시고 나중에는 `10`년 또는 사용자가 원하는 만큼의 연도를 보여주세요
"""


# 연, 월, 일을 따로 설정해서 날짜를 수동으로 더해 출력
year = int(input("연도 입력 : "))
month = int(input("월 입력 : "))
day = int(input("일 입력 : "))

# 날짜 생성
from datetime import date, timedelta

# 기준일 설정
d_day = date(year, month, day)
print("설정된 기준일", d_day)

# 더해야 할 날짜를 계산
# li = [100, 200, 300, 365, 400, 500, 600, 700, 730]
li = []
period = int(input("기간(연) 입력 : ")) #기간(연)
for i in range(1, 365*period+1):
    # 100의 배수이거나 365의 배수라면
    if i % 100 == 0:
        li.append(i)
    elif i % 365 == 0:
        li.append(i)

# 출력은 365의 배수와 아닌것으로 구분하여 출력 (오차 있음)
for i in li:
    after = d_day + timedelta(days = i)
    if i % 365 == 0:
        print(f"{i // 365}주년", after)
    else:
        print(f"{i}일 뒤", after)