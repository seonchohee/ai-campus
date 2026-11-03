"""
슬라이싱

리스트를 원하는 구간으로 잘라내는 것을 말함
위치를 이용하여 잘라냄
[ 시작 : 종료 : 간격 ] 와 같이 표시
"""

names = ["피카츄", "라이츄", "파이리", "꼬부기", "버터플"]
print(names)
print(names[1]) #라이츄(슬라이싱x)
print(names[1:3]) # 1부터 3 전까지 (range와 같은 형태)
print(names[0:3])# 앞에서 3개
print(names[:3])# 앞에서 3개
print(names[1:]) # 1부터 끝까지

# (Q) 뒤에서 3개만
print(names[-3:])

# 한칸씩 띄고 자르기
print(names[::2])

# 역순으로 가져오기
print(names[::-1])