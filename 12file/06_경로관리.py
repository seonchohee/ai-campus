"""
경로관리

파일의 내용이 아닌 파일의 위치나 형태 등을 관리할 수 있는 도구
pathlib 내부에 있는 Path라는 모듈을 사용하여 처리
"""

from pathlib import Path

target = Path("nicknames.txt")
# target = Path("test")

# 파일의 정보 확인
print(target.name) #파일명
print(target.stem) #확장자를 제외한 파일명
print(target.suffix) #확장자
print(target.parent) #상위폴더 (없으면 .)
print(target.absolute()) #절대경로

# 파일의 유형 확인
# - 컴퓨터에서는 파일과 폴더가 동급이다
# - 대다수의 프로그래밍 언어에서는 같은 데이터로 취급한다
print("있어?", target.exists())
print("파일?", target.is_file())
print("폴더?", target.is_dir())

# 폴더 생성
dir = Path("dump")
dir.mkdir(exist_ok=True)

# 폴더 삭제 (비어있는 경우만 삭제되며, 내용물이 있으면 다른명령필요)
dir.rmdir()