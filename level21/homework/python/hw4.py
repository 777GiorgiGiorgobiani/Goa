# 4) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე შეამოწმებ რიცხვი ლუწია თუ კენტი დაბეჭდეთ რიცხვები და თან გვერძე მიუწერეთ ლუწია თუ კენტი

# def func(num):
num = int(input("number: "))
for i in range(1, num + 1):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

# func(int(input()))