# 3) მომხმარებელს შემოატანინეთ ორი რიცხვი ხოლო ამის შემდეგ for loop - ის გამოყენებით გამოიტანეთ ამ რიცხვებს შორის ჯამი და ნამრავლი.

num1 = int(input("number1: "))
num2 = int(input("number2: "))
sum = 0

for i in range(num1 * num2):
    sum = sum + i
print(sum)