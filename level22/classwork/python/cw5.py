# 5) მომხმარებელს შეეკითხეთ ექაუნთძე შესასვლელი პაროლი, სანამ ის არ შემოიტანს სწორ პაროლს მას ხელახლა გაუმეორეთ რომ შემოიტანოს პაროლი თუ სწორად შემოიტანს დაბეჭდოს რომ ექაუნთზე შევიდა

password = 12345678

while True:
    enter_password = int(input("enter the password: "))
    while enter_password != password:
        enter_password = int(input("The password is wrong! Try again: "))
    print("You have entered your account")
