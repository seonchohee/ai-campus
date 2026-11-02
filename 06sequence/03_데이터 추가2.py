"""
리스트에 데이터를 미리 넣어두는게 아니라 원할 때 추가
"""

# 비어있는 리스트를 준비
scores = []

# 데이터 추가 (append - 맨뒤에 데이터를 추가)
for i in range(5): #5번
    number = int(input("숫자 입력 : "))
    scores.append(number)

print(scores)

# list의 길이를 확인
print(len(scores))