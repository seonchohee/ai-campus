"""
문자열 편집

문자열을 변형하거나 분리, 결합하여 새로운 문자열을 만들어내는것
* 문자열은 불변(immutable)이기 때문에 수정이 안됨

참고로 리스트는 가변(mutable)입니다.
"""

li = [30, 50, 20, 10, 40]
li.sort()
print("리스트", li)

txt = "Hello"
# txt.upper() # 대문자 만들기
txt = txt.upper()
print("대문자", txt)

txt = txt.lower()
print("소문자", txt)

# 불필요한 여백 제거
# - 여백이 아닌 첫글자의 앞 (왼쪽 여백)
# - 여백이 아닌 마지막 글자의 뒤 (오른쪽 여백)
url = "\u00A0\u00A0  www.naver.com          "
print(url)
print(url.strip())
print(url.lstrip())
print(url.rstrip())

url = "          www   .naver.com          "
print(url.strip())

# 문자열 치환
note = "I love chicken"
print(note.replace("chicken", "python"))

# 메소드 체이닝 - 연속으로 .을 찍어서 작업시키는 것
print(note.replace("love", "hate")
      .replace("chicken", "pizza"))