# 자준한돈과 거스름돈구하기
#50000원내고 빵3500원 3개 우유6000원2개 사탕300원4개샀음

bread_price = 3500
bread_count = 3
milk_price = 6000
milk_count = 3
candy_price = 300
candy_count = 4
pay = 50000

bread_total = bread_price * bread_count
milk_total = milk_price * milk_count
candy_total = candy_price * candy_count

total = bread_total + milk_total + candy_total
chang = pay - total

print(total)
print(chang)

