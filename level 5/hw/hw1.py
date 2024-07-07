# გააკეთეთ 3 ცალი სწორი კოდი და 3 ცალი არასწორი კოდი და უნდა ახსნათ რატომ არის ეს კოდი სწორი და რატომ არის ეს კოდი არასწორი

# I - ის ცვლადები

apartment1 = 128
apartment2 = 342
apartment3 = 423
apartment4 = 658
apartment5 = 727
apartment6 = 912

# სწორი I

print("These are the available apartments: ", str(apartment1) + ",", str(apartment2) + ",", str(apartment3) + ",", str(apartment4) + ",", str(apartment5) + ",", str(apartment6) + ".")

# არასწორე I - ეს error-ი იმიტომ არის რადგან აქ ჩვენ integer-ს არ ვაქცევთ string-ად, ჩვენ არ შეგვიძლია მივუმატოთ integer-ი string-ს.
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

print("These are the available apartments: ", apartment1 + ",", apartment2 + ",", apartment3 + ",", apartment4 + ",", apartment5 + ",", apartment6 + ".")


# სწორი II

car = "bmw"
car2 = "mercedes"
print("I love", car)
print("I love", car2)

# არასწორე II - კოდი შეჩერდება 32 ხაზზე. ეს არასწორეა რადგან პროგრამა კოდს კითხულობს ხაზ-ხაზად, ფუნქცია print იძახებს ცვლადებს car3 და car4, მაგრამ ეს ინფორმაცია ჯერ პროგრამას არ წაუკითხავს ამიტომაც უცნობი ცვლადებია.
# NameError: name 'car3' is not defined.

print("I love", car3)
print("I love", car4)
car3 = "audi"
car4 = "ford"


# სწორი III

game_over_msg = "Game Over"
print(game_over_msg)

# არასწორე III - ეს არის უბრალო სინტაქსური შეცდომა
# SyntaxError: invalid syntax

game over msg = "Game Over"
print(game over msg)


# სინტაქსური error-ების მაგალითები:

# სწორი

print("Hello World")
print("A yellow fox jumped over the fence")
print("I love printing messages")
print("Metallica is a great band")

# არასწორე

print Hello World     # SyntaxError: Missing parentheses in call to 'print'.
print(A yellow fox jumped over the fence)     # SyntaxError: invalid syntax.
Print("I love printing messages")       # NameError: name 'Print' is not defined
print(Metallica is a great band")       # SyntaxError: unterminated string literal