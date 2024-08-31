# 1) 1-დან 100-მდე დაითვალეთ ხუთის ჯერადი რიცხვების ჯამი

result = 0

for i in range(101):
    if i % 5 == 0:
        result = result + i
print(result)