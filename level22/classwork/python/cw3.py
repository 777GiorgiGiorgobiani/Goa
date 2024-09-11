# 3) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ while loop ის გამოყენებით 1-დან მომხმარების შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ ხუთის ჯერადი რიცხვები

num = int(input("enter a number: "))
num0 = 0

while num0 < num:
    num0 = num0 + 1
    if num0 % 5 == 0:
        print(num0, "can be divideed by five!")