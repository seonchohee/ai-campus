"""
# 함수 실습 : 반환값이 존재하는 함수 만들기

다음 요구사항에 맞는 함수를 `05.반환값실습.py`에 구현하세요

1. `rect`라는 이름으로 직사각형의 넓이를 구하여 반환하는 함수를 만든 뒤 높이 `7`, 너비 `5`인 직사각형의 넓이를 구해 출력하세요
2. `triangle`이라는 이름으로 삼각형의 넓이를 구하여 반환하는 함수를 만든 뒤 높이 `5`, 너비 `3`인 삼각형의 넓이를 구해 출력하세요
3. `age`라는 이름으로 출생년도 4자리로 한국 나이를 구하는 함수를 만든 뒤 `2000`년생의 나이를 구해 출력하세요
4. `subway`라는 이름으로 출생년도 4자리를 전달받아 나이에 따른 지하철 요금을 구하여 반환하세요.
  - 기본 카드 보증금 500원
  - 8세 미만 이용료 무료
  - 8~13세 450원
  - 14~19세 900원
  - 20~64세 1550원
  - 65세 이상 무료
"""

# --------------------------------
# rect 함수
# --------------------------------
def rect(width, height):
    area = width * height
    return area

# --------------------------------
# triangle 함수
# --------------------------------
def triangle(width, height):
    # area = width * height / 2
    area = rect(width, height) / 2 #다른 함수를 호출
    return area

# --------------------------------
# age 함수
# --------------------------------
def age(birth_year):
    result = 2026 - birth_year + 1
    return result

# --------------------------------
# subway 함수
# --------------------------------
def subway(birth_year):
    korean_age = age(birth_year)
    card = 500
    if korean_age < 8 or korean_age >= 65:
        return card
    elif korean_age <= 13:
        return card + 450
    elif korean_age <= 19:
        return card + 900
    else:
        return card + 1550

# --------------------------------
# main 코드
# --------------------------------
print(rect(7, 5))

a = triangle(7, 5)
print(a)

print(age(2000))
print(age(2005))
print(age(2010))

print(subway(2000))
print(subway(2005))
print(subway(2010))