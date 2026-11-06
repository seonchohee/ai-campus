"""
딕셔너리 조회

"""


# 이름과 정수를 같이 저장하기 위한 딕셔너리 생성
datq = {
    "홍길동" : 70,
    "임꺽정" : 75,
    "장보고" : 60,
    "이순신" : 90


}

#[1] key만 출력
print("<key출력>")
for key in data:
    # print (key)
    print(key, data[key])

#[2] value만 출력 (권장하지않음)
print("<value>")
for value in data.values():
    print(value)

# key value를 한번에 출력
print("<한 번에 조회>")
for key, value in data.items():
    print(key, value)

