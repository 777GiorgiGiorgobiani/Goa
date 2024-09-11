# 5) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი დაბეჭდეთ მომხმარებლის შემოტანილ რიცხვამდე მხოლოდ ხუთის ჯერადი რიცხვები

# def func(num):
num = int(input("number: "))
for i in range(1, num + 1):
    if i % 5 == 0:
        print(i)

# func(int(input()))