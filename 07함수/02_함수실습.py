"""
함수 실습
파일명 : 02_함수실습.py

다음 작업을 수행하는 함수를 만드세요

정수 하나를 전달받아 해당하는 숫자의 구구단을 출력하는 gugudan이라는 함수
"""

def gugudan(num):
    for i in range(1, 10):
        print(f"{i}X{num} = {i * num}")
for dan in range(2,10):
    gugudan(dan)


"""
강사님 :

def gugudan(dan):
    print(f"<구구단 {dan}단>")
    print(f"{dan} x 1 = {dan * 1}")
    print(f"{dan} x 2 = {dan * 2}")
    print(f"{dan} x 3 = {dan * 3}")
    print(f"{dan} x 4 = {dan * 4}")
    print(f"{dan} x 5 = {dan * 5}")
    print(f"{dan} x 6 = {dan * 6}")
    print(f"{dan} x 7 = {dan * 7}")
    print(f"{dan} x 8 = {dan * 8}")
    print(f"{dan} x 9 = {dan * 9}")

gugudan(2)
gugudan(3)
gugudan(12)
"""

