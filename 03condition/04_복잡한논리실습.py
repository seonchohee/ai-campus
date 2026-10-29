"""
# 실습 문제 : 건강검진 대상자 판정

파일명 : `03_condition/04_복잡한논리실습.py`

올해 국가 지정 건강검진 대상자 기준은 다음과 같습니다.

- 짝수년도 출생
- 30세 이상

사용자에게 출생년도 4자리를 입력받아 대상자라면 `True`, 아니라면 `False`를 출력해보세요
"""

birth = int(input("출생년도 4자리 입력 : "))
even = birth % 2 == 0
print("짝수년생인가요?", even)

age = 2026 - birth + 1
over30 = age >= 30
print("30세이상인가요?", over30)

# judge = even == True and over30 == True
judge = even and over30
print("건강검진대상자 : ", judge)