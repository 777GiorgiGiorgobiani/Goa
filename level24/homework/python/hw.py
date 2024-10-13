# 1) for ციკლის მეშვეობით შეასრულეთ ყველა მათემატიკური ოპერაცია 0-დან 100-მდე რიცხვებზე

sum = 0

act = input("what do you want the number to do?: ")

for i in range(int(input("pick a number: "))):
    if act == "-":
        sum = sum - i
    elif act == "+":
        sum = sum + i
    elif act == "*":
        sum = sum * i
    elif act == "/":        
        sum = sum / i
print(sum)