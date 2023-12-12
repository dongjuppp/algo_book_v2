input_num = 950

result = 0

moneys = [500, 100, 50, 10]

for money in moneys:
    if input_num // money > 0:
        result += (input_num // money)
        input_num  %= money

print(result)