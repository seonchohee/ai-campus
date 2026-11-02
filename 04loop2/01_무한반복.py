"""
while 반복

특정 조건을 만족하는 동안 실행되느 반복문
=특정 시점까지 실핼되는 반복문 (break:멈춤)

"""

import random

count = 0

while True: #무한 반복(언제나 실행해라
    dice = random.randint(1, 6)
    print(f"주사위 = {dice}")

    count += 1

    if dice == 6: #주사위가 6이 나오면 그만둬라 = 6이 나올때까지 던져라
        break

print(f"쥐사위를 총{count} 번 던졌습니다.")
