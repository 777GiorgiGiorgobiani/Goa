# 5) შექმენით სია რომელშიც გექნებათ ოცი სხვადასხვა რიცხვი შემდეგ კი დაბეჭდეთ მხოლოდ 20 ზე მეტი რიცხვები ისე რომ იყოს თან სამის ჯერადი გამოიყენეთ for loop

nums = [18, 19, 20, 21, 22, 23, 24, 25, 26, 30, 40, 60, 90]

for i in nums:
    if i > 20 and i % 3 == 0:
        print(i)