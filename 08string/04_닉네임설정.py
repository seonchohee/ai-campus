"""
# 문자열 실습 : 닉네임 설정 프로그램 (04_닉네임설정.py)

사용자에게 원하는 닉네임을 입력받아 설정하는 프로그램을 구현하세요

### 요구사항
- `운영자`, `admin`과 같은 단어는 포함시킬 수 없습니다.
- 닉네임은 최소 2글자 이상 최대 10글자 이하로 설정해야 합니다
"""

# 닉네임 입력
nickname = input("사용할 닉네임 : ")

# 판단
condition1 = "운영자" not in nickname
condition2 = "admin" not in nickname
# condition3 = 2 <= len(nickname) <= 10
condition3 = len(nickname) >= 2 and len(nickname) <= 10
can_use = condition1 and condition2 and condition3

# 출력
if can_use:
    print("닉네임 설정이 완료되었습니다")
else:
    print("사용할 수 없는 닉네임 형태입니다")