


"""다섯명의 학생 점수를 입력받아 합격자와 불합격자의 수를 출력하세요
(합격의 기준은 60점 이상이며, 사람들은 0~100 사이의 숫자만 입력합니다) """

count_pass = 0
crint_fail = 0

for i in range(5):
    score = int(input("점수를입력하시오:"))

    if score >= 60:
        count_pass += 1
    else:
        crint_fail += 1


print(f"합격자 수:{count_pass}명")
print(f"불합격자수:{crint_fail}명")


#60에서100사이를 합격자로 출력
#0에서59 사이에 점수를 불합격자로 출력







