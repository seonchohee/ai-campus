"""
리스트에 데이터를 미리 넣어두는게 아니라 원할 때 추가
"""

# 비어있는 리스트를 준비
scores = []

# 데이터 추가 (append - 맨뒤에 데이터를 추가)
# scores[0] = 10 # +0지점에 10을 넣으세요 (수정할 때만 가능)
scores.append(10)
scores.append(20)
scores.append(30)
scores.append(40)
scores.append(50)

print(scores)

# list의 길이를 확인
print(len(scores))