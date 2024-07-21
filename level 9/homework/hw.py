# შექმენით დროში მოგზაურობის პროგრამა, რომელიც მომხმარებელს შეეკითხება მის ამჟამინდელ ასაკს, ამჟამინდელ წელს, რამდენი წლით სურს დროში მოგზაურობა, შემდეგ კი პროგრამა დაბეჭდავს დროში მოგზაურობის შემდეგ რომელი წელი იქნება და რამდენი წლის იქნება მომხმარებელი დროში მოგზაურობის შემდეგ

user_age = int(input("Age: "))
current_year = int(input("What's the current year?: "))
goBack = int(input("By how many years do you want to go back?: "))

print("You are", user_age, "years old,", "the current year is", str(current_year) + ".", "You want to go back in time by", goBack, "years.")


decision = input("Are you sure you want this? (You may not be able to come back to the present...): ")


if decision == "yes":
    decision = True
    print("You are now in the year of", current_year - goBack, "and you are", user_age - goBack, "years old.")


else:
    decision = False
    print("You are still", user_age, "years old and in the year of", str(current_year) + ".")