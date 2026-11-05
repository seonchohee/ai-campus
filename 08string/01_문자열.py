"""
문자열(string)

문자열은 여러 개의 문자가 순서대로 저장된 형태의 데이터
리스트처럼 인덱스를 가지고 슬라이싱이 가능

문자열은 불변이다 (immutable)
"""

a = ["H", "e", "l", "l", "o"]
b = "Hello"

print(type(a)) # list
print(type(b)) # str

# 형태는 다른데 명령이 매우 비슷합니다
print(len(a)) # list
print(len(b)) # str

print(a[0], a[1], a[2], a[3], a[4]) # list
print(b[0], b[1], b[2], b[3], b[4]) # str

print(a[0:4])
print(b[0:4])

# (Q) 끝에서 3글자
print(b[-3:])

print(b[::-1]) #거꾸로(-1칸씩)

c = "안녕하세요"
print(c[::-1])