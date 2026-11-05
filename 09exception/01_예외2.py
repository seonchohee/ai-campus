"""
예외 처리 ()

예외 상황이 안생기게 할 수는 없으니 plan b 를 미리 준비해두자
만약 하나의 plan b로 모두 처리하고싶다면?
exception을 사용한다(예외의 적정 최상위의 형태)
"""

try:#plan a
    price = int(input("술값:"))
    people = int(intput("인원:"))

    money = price // people
    change = price % people

    print("1인당",money)
    print("남은돈",change)
except exception: # 통합 plan b
    prinit("프로그램에서 오류가 발생했습니다.")


#except zerodivisionerror: #plan b-1(인원수가 0일 떄)
   # print("인원수는 0일 수 없습니다.")
#except valueerro: #plan b-2 (잘못된 입력시)
   # print("소수점이 없는 숫자만 입력하세요.")