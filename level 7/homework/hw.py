# 1) მომხმარებელს input-ის გამოყენებით უნდა შემოატანინოთ მონაცემთა ტიპი და შემდეგ უნდა დაპრინტოთ მომხმარებლის შეტანილი მონაცემთა ტიპი example: თუ მომხმარებელმა შემოიტანა string-ი მაშინ უნდა გამოიტანოს <class string> 


user_age = int(input("how old are you?: "))         # აქ ცვლად user_age-ს მიეცემა საფასური input ფუნქციის გამოყენებით. input არის ფუნქცია რომელიც მომხმარებელს აძლევს უფლებას შემოიტანოს რაიმე ინფორმაცია პროგრამაში
print(user_age)
print(type(user_age))                               # ჩვენ აქ print ფუნქციისა და type ფუნქციის საშვალებით ტერმინალზე გამოგვაქვს ნუთუ როგორი დატა ტიპი არის ცვლადი user_age

user_name = input("what is your name?: ")
print(user_name)
print(type(user_name))

floatrng = float(input("pick a random number: "))   # აქ float აიძულებს რომ რაც მომხმარებელმა შემოიტანა კოდში გადააქციოს float საფასურად
print(floatrng)
print(type(floatrng))