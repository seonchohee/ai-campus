"""
# 실습 문제 : 기본요금 판정기

파일명 : `00_condition/02_논리실습문제2.py`

PC방에서 고객의 이용시간에 따라 요금을 계산하는 프로그램을 만들고 있습니다.
1시간에 `1,000`원의 요금을 받고 있는데,
급한 출력 등으로 1시간 미만으로 이용하는 고객이 늘어나서 기본요금 제도를 도입하기로 했습니다.

고객의 시작, 종료시간과 분을 각각 입력받아서 1시간 미만으로 이용한 경우 `True`,
1시간 이상 이용한 경우 `False`로 판정하는 기본요금 판정기를 구현해보세요
"""
# 입력
in_hour = int(input("입장(시간) : "))
in_minute = int(input("입장(분) : "))
out_hour = int(input("퇴장(시간) : "))
out_minute = int(input("퇴장(분) : "))

# 연산
in_time = in_hour * 60 + in_minute
out_time = out_hour * 60 + out_minute
time = out_time - in_time
base = time < 60

# 출력
print("이용시간 : ", time, "분")
print("기본요금 대상 : ", base)