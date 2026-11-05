"""
실습 과제
파일명 : 02_나이구하기.py

사용자에게 YYYY-MM-DD 형태의 날짜를 입력 받아 다음을 구하세요

한국 나이 (korean_age)
만 나이 (global_age)

한국나이는 연도만으로 계산하며, 만 나이는 연월일 다 필요하지만 계산 편의상 연도와 월 정보만 추출해서 계산하도록 변경하겠습니다. 만 나이는 12개월당 한 살인걸로 간주합니다.

프로그램에서 발생하는 예외 상황들이 모두 처리될 수 있도록 코드를 구현하세요

365일기준으로 구하기 x, 12개월 기준으로 구하기 O
"""


import re

date = input("생년월일을 입력하세요: ")
result = date.split("-")
year = int(result[0])

print(result)

current_year = 2026
age = current_year - year
korean_age = age + 1

month = int(result[1])
current_month = 11

