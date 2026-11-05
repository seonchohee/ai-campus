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


try:
    birth = input("생년월일 입력 (YYYY-MM-DD): ")

    regexp = r"^(19|20)[0-9]{2}-((01|03|05|07|08|10|12)-(0[1-9]|[12][0-9]|3[01])|(04|06|09|11)-(0[1-9]|[12][0-9]|30)|02-(0[1-9]|[12][0-9]))$"

    check = re.fullmatch(regexp, birth)

    if check is None:
        raise ValueError

    result = birth.split("-")

    year = int(result[0])
    month = int(result[1])


    current_year = 2026
    current_month = 11


    if year > current_year:
        raise ValueError

    if year == current_year and month > current_month:
        raise ValueError


    korean_age = current_year - year + 1
    global_age = current_year - year

    if month > current_month:
        global_age -= 1



    print("한국 나이:", korean_age)
    print("만 나이:", global_age)

except Exception:
    print("잘못된 생년월일입니다.")