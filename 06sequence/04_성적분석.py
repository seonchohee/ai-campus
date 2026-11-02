"""
5명의 시험성적을 입력받은 뒤 반복문과 조건문을 사용하여 다음을 구현하세요.

합격(60점 이상) 학생의 점수만 출력하세요
성적 우수자(90점 이상) 학생의 점수만 출력하세요
합격 인원수와 성적 우수자의 인원수를 각각 구하여 출력하세요
처음 입력한 학생의 등수를 구하여 출력하세요

"""

scores = []

count = 0
excellent_count = 0
rank = 1

for i in range(5):
    score = int(input("점수 입력: "))
    scores.append(score)


for score in scores:
    if score >= 60:
        print(score)
        count += 1
for score in scores:
    if score >= 90:
        print(score)
        excellent_count += 1

first_score = scores[0]

for score in scores:
    if score > first_score:
        rank += 1



print("합격 인원:", count,"명")
print("우수자 자:", excellent_count,"명")
print("첫 번째 학생 등수:", rank,"등")



"""
#강사님 풀이

print("<60점 이상 합격자의 점수>")
for score in scores:
    if score >= 60:
        print("점수", score)

# 2
print("<90점 이상 우수자의 점수>")
for score in scores:
    if score >= 90:
        print("점수", score)

# 3
print("<60점 이상 합격자의 인원수>")
count60 = 0
for score in scores:
    if score >= 60:
        count60 += 1

print(f"{count60}명")

# 4
print("<90점 이상 우수자의 인원수")
count90 = 0
for score in scores:
    if score >= 90:
        count90 += 1
print(f"{count90}명")



"""

