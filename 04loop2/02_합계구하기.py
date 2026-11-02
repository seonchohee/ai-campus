"""
사용자가 입력한 숫자들을 계속 더해서 종료 시 합계와 평균을 출력하는 프로그램을 구현하세요
단, 사용자가 0을 입력하면 종료되며 0은 입력으로 간주하지 않습니다

숫자 입력 : (10)
숫자 입력 : (20)
숫자 입력 : (30)
숫자 입력 : (0)

합계 : 60
평균 : 20
"""
total,count = 0,0
number = 0

while True:
    number = int(input("숫자 입력 : "))


    if number < 0:
        continue

    #0 경우를 제외하고 카운트와 함께 계산
    if  number == 0:
        break
    #lese 없어도 lese 처럼 사용된다
    total += number
    count +=1

average = total / count

print(f"합계 = {total} ")
print(f"평균 : {average}")



"""
만약 그냥 헛 입력갚 (엔터를 제거 하고싶다면)

    text = input("숫자 입력 : ")
    if text == "":
        continue

    number = int(text)
    
"""