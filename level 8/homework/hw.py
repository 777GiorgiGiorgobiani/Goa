# 1) მომხმარებელს შემოატანინეთ ორი რიცხვი, შემდეგ კი შეადარეთ ეს ორი რიცხვი ერთმენთს, მიღებული მნიშვნელობა შეინახეთ ცვლადში და შემდეგ დაბეჭდეთ მისი მონაცემთა ტიპი და მნიშვნელობა

num1 = int(input("pick a random number: "))
num2 = int(input("pick a random number: "))
equation1 = num1 < num2
equation2 = num1 > num2
print(equation1)
print(equation2)
print(type(equation1))
print(type(equation2))