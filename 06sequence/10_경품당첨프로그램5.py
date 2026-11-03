"""
# 실습 문제 : 경품 당첨 프로그램

참가자의 이름을 리스트에 입력받은 뒤 1, 2, 3등 당첨인원 수를 설정하면 각각의 등수에 대한 당첨인원이 화면에 출력되도록 구현하는 프로그램을 만들고 싶습니다.

```
총 인원수 입력 : 6
이름 입력 : 민수
이름 입력 : 지수
이름 입력 : 지혜
이름 입력 : 철수
이름 입력 : 지후
이름 입력 : 연아

1등 수 입력 : 1
2등 수 입력 : 1
3등 수 입력 : 2

<당첨 결과>
1등 : [지후]
2등 : [지혜]
3등 : [연아, 철수]
미당첨 : [민수, 지수]
```
"""

names = [
    "김민준", "이서연", "박지훈", "최유진", "정현우",
    "강수빈", "조성민", "윤지아", "장도윤", "한예린"
]

# 1, 2, 3등을 모두 추첨
import random
first = []
second = []
third = []

first_size = 1 # 1등 수
second_size = 1 # 2등 수
third_size = 2 # 3등 수

for i in range(first_size): # 1등 추첨
    select = random.choice(names)
    names.remove(select)
    first.append(select)

for i in range(second_size): # 2등 추첨
    select = random.choice(names)
    names.remove(select)
    second.append(select)

for i in range(third_size): # 3등 추첨
    select = random.choice(names)
    names.remove(select)
    third.append(select)

print(f"1등 당첨자 : {first}")
print(f"2등 당첨자 : {second}")
print(f"3등 당첨자 : {third}")
print(f"미당첨자 : {names}")