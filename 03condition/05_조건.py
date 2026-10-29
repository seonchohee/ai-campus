"""
조건(condition)

특정 상황을 만족해야 실행되는 형태의 구문

if 판정식 :
    True일 때 실행될 코드

아닌 경우도 처리하고 싶다면 if의 뒤에 else 추가 가능

if 판정식 :
    True일 때 실행될 코드
else :
    False일 때 실행될 코드
"""

age = 25

if age >= 20 :
    print("성인입니다")
    print("입장바랍니다")

# if age < 20 :
else :
    print("미성년자입니다")
    print("입장하실 수 없습니다")