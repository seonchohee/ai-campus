"""
리스트에서 제공하는 명령들

- 리스트는 참조형 데이터(Reference Type)이다
- 단순한 데이터(ex : int, float, bool)와 다르게 다양한 기능들을 제공 (=메소드, method)
- 제공되는 다양한 기능들은 참조연산(.)을 이용해서 사용이 가능하다
- (ex) 휴대폰으로 사진을 찍는다 ----> 휴대폰.사진()
"""

a = [30, 20, 50, 20, 10, 20, 40]
print(a)

# 포함여부 검색 (ex : 20이 들어있나요? 안들어있나요?)
print(20 in a)
print(20 not in a)

# 삭제 (값 또는 위치로 삭제)
a.remove(20) #20을 지우세요 (좌측에서 첫번째 항목이 지워짐)
print(a)

# (Q) 30을 전부다 지우려면?
while 30 in a:
    a.remove(30)

# 위치로 삭제
print("현재", a)
del a[0] # 맨 앞 위치를 제거
print("맨앞제거", a)
# del a[len(a)-1]
del a[-1] #맨 뒤 위치를 제거
print("맨뒤제거", a)

# a.sort() # 정렬하라 (오름차순)
a.sort(reverse=True) #반대로 정렬해라 (내림차순)
print(a)

a.reverse() # 뒤집어라
print(a)