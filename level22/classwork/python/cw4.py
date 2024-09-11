# 4) მომხამრებელს შევეკითხოთ სახელი და იქამდე არ შემოვუშვათ სახლში სანამ ის არიტყვის რომ ქვია სვარჩიკა მაყვალა

while True:
    name = input("State your name VIP: ")

    while name != "Svarchika Mayvala":
        name = input("You are not on the VIP list! State it again: ")
    print("You really are Svarchika Mayvala")
