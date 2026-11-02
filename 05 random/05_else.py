"""
반복문에도 else를 쓸수있다.
"""

# 숫자 10 번 입력받기 (단,0 입력시종료)


for i in range(10):
    number = int(input("숫자 입력: "))

    if number == 0:
        break

else:
    print("정상 종료되었습니다")




