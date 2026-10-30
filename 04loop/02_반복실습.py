"""

AI Campus를 5번 출력
1부터 100까지 정수를 출력
1부터 100까지 중에서 짝수만 출력
1부터 100까지 중에서 7로 끝나는 숫자만 출력

"""


for i in range(5):
    print("AI Campus")

for i in range(1,101):
    print(i)


for i in range(1,101):
    if i % 2 == 0:
     print(i)

for i in range(1, 101):
    if i % 10 == 7:
        print(i)

