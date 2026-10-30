"""
랜덤(random)

- 뭐가 나올지 알 수 없는 값
- 범위를 특정할 수 있어야 함

파이써은 기본 명령으로  랜덤을 제공하지 않는다
랜덤을 사용하고 싶다면 'import'를 써서 모듈울 불러와야한다

"""

#random 모듈을 준비한다
import random
#random을치고 (.) 을 찍고 명령이름을 호출하면 실행됨
#6미만 정수 +1
dice =  random.randrange(6)+1
print("dice:",dice)

#1이상7미만 정수
dice = random.randrange(1,7)
print("dice:",dice)

#1이상6이하정수
dice = random.randrange(1,6)
print("dice:",dice)

#1이상 6이하 실수 (추천)
number= random.uniform(1,6)
print("number:",number)



#주사위를10번던지세요

for i in range(10):
    dice= random.randint(1,6)
    print("dice:",dice)
