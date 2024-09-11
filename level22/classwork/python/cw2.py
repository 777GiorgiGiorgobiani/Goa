# 2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ while loop ის გამოყენებით 1-დან მომხმარების შემოტანილ რიცხვამდე დაბეჭდეთ ყველა რიცხვი და თან გვერძე მიუწერეთ ლუწია თუ კენტი

num = int(input("enter a number: "))
num0 = 0

while num0 < num:
    num0 = num0 + 1
    if num0 % 2 == 0:
        print(num0, "is even!")
    else:
        print(num0, "is odd!")