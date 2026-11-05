"""
문자열의 주요명령
- 같다, 다르다는 숫자와 동일 (== , !=)
"""

song = "떳다 떳다 비행기\n날아라 날아라"
email = "testuser@naver.com"

# 포함 검사
# - email에 @가 들어있는가?
print("@" in email)
print("naver" in email)

# - email에 @가 몇 번 들어갔는가?
print(email.count("@"))
print(song.count("@"))

# - email에 @가 어디에 있나요?
print(email.find("@"))
print(song.find("@")) # 없으면 -1

# - email이 naver.com으로 끝나나요?
print(email.endswith("naver.com"))
print(email.endswith("@"))

# - email이 @로 시작하나요?
print(email.startswith("@"))