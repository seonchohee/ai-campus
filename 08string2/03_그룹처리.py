"""
그룹 처이와 OR 계산
"""

import re

input = "사과"

#ragexp = "사과 또는 바나나"
ragexp = "r^(사과|포도|바나나)$"

result = re.findall(ragexp, input)

if result is not None:
    print("참 잘했어요")
else:
    print("허용되지 않은 입력")