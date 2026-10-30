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

# for i in range(2,101,2)도 가능은 하다
for i in range(1,101):
    if i % 2 == 0:
     print(i)

for i in range(1, 101):
    if i % 10 == 7:
        print(i)

#추가문제
#1~100 사이에 5가 들어있는 숫자만 출력

for i in range(1, 101):
    if i % 10== 5 or i // 10 == 5:
       print("5가 들어간 숫자:",i)


#두번째방법

find = 5
for i in range(1, 101):
    ten = i // 10 == find
    one = i % 10 == find
    if ten or one:
        print(find, "가 들어간 숫자 :", i)




