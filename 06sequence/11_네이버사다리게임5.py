"""
네이버에서 "사다리게임"을 검색해서 나온 프로그램을
텍스트 버전으로 만드세요
"""

import random

names = []
items = []

people = 4

# 입력
for i in range(people):
    name = input("이름 입력 : ")
    names.append(name)

for i in range(people):
    item = input("항목 입력 : ")
    items.append(item)

# 셔플
random.shuffle(items)

# 결과화면
for i in range(people):
    print(f"{names[i]} → {items[i]}")