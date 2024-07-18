#   4) აქამდე ნასწავლი მასალის გამოყენებით ივარჯიშეთ ძალიან ბევრი და მოიფიქრეთ რაიმე პროგრამა რომელსაც გააკეთებთ

name = input("what's your name?: ")
user_age = int(input("how old are you?: "))
club_list = ["Goga", "Givi", "Luka", "Zura", "Saba"]
if user_age >= 18:
    club_list.append(name)
    print("Welcome to the club! here is the list of current guests:", club_list)
else:
    print("You are not allowed in!")