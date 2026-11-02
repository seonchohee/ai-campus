"""
 #(Q)다섯개의 숫자를 저장한 뒤 합계,펼균,최대,최소 등을 구합시다
 #     저장하려면 5개의 변수가 필요하다
 # 오늘만 사는 코드 단점 개수&문제 가달라지면 재작성해야함
 # 하나의 리스트(list)로 처리할 수 있다
"""

# 오늘만 사는코드

a=50
b=60
c=70
d=75
e=81

total=a+b+c+d+e
average= total / 5

print(f"합계 = {total}")
print(f"평균 = {average}")



#새로운 방법

scores = [50,60,70,75,81]
print(scores)
#여러개의 데이터를 위치(순서)에 기반해서 관리한다
#scores(리모콘)----->[50][60][70][75][81]
#                  +---+----+---+---+---+
#                 +0  +1   +2  +3  +4  +5
print(scores[0]) #0지점 데이터
print(scores[1]) #1지점 데이터
print(scores[2]) #2지점 데이터
print(scores[3]) #3지점 데이터
print(scores[4]) #4지점 데이터
#print(scores[5]) #error(5번째가 아님에 유의)
print("-"*10)
print(scores[-1]) # 맨뒤에서 -1지점
print(scores[-2]) # 맨뒤에서 -2지점
print(scores[-3]) # 맨뒤에서 -3지점
print(scores[-4]) # 맨뒤에서 -4지점
print(scores[-5]) # 맨뒤에서 -5지점

#합계

# total = 0
# total +=[0]
# total +=[1]
# total +=[2]
# total +=[3]
# total +=[4]

# total=0
# for i in range(5):
#     total  += scores[i]

total = 0
for score in scores:
    total += score

print("합계",total)

# 랜덤과 결합
import random
print(random.choice(scores)) # 아무거나 뽑아서 출력





