"""
네이버에서 "사다리게임"을 검색해서 나온 프로그램을
텍스트 버전으로 만드세요
"""

import random

names = ["피카츄", "라이츄", "파이리"]
items = ["얻어먹기", "밥사기", "술사기"]

# 셔플
random.shuffle(items)

# 결과화면
print(f"{names[0]} → {items[0]}")
print(f"{names[1]} → {items[1]}")
print(f"{names[2]} → {items[2]}")