"""
예외 처리의 마무리는 어떻게 할 수 있을까?

         →catch(이상)
try
                          →finally(최종)
          →elae(정상)

"""

try:
    age = int(input("나이 입력: "))

except Exception:
    print("입력이 잘못되었습니다")

# else:
#     print(f"입력 결과: {age}")

finally:
    print("프로그램을 종료합니다")