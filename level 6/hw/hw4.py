# გაიმეორეთ გავლილი მასალა



from random import *        # random-ის მოდული 




# selection

age = int(input("what is your age: "))                  # ითხოვს მომხმარებლის ასაკს

if age < 13:                                            # თუ მომხმარებლის ასაკი 13 წელზე დაბალია მაშინ
    print("You are not allowed to view the content")    # პრინტავს მესიჯს
else:                                                   # თუ მომხმარებელი უპასუხებს 13-ზე დაბალ პასუხს მაშინ
    print("You are free to go")                         # პრინტავს მესიჯს



# while loop

level = 0                       # level ცვლადი
max_level = 100                 # max_level ცვლადი
while level < max_level:        # როდესაც level ნაკლებია max_level ცვლადზე აკეთებს ფუნქციას print(level)
    level = level + 10          # აქ ვუმატებთ ორიგინალ level-ის საფასურს 10-ს, ეს ასე გაგრძელდება სამადე არ მიწვდება max_level-ის საფასურს.
    print(level)                # ეს დაპრინტავს სანამდე level არ გაუტოლდება max_level-ს



# sequence

item_picker = randint(0, 4)                                                 # ირჩევს random ციფრს

items = ["Screw driver", "Drill", "Hammer", "Hacksaw", "Metal Saw"]         # ნივთების ლისტი
print(items[item_picker])                                                   # პრინტავს random-ად არჩეულ ნივთს



# for loop

cars = ["BMW", "Mercedes", "Ford", "Chevlorate", "Audi"]        # მანქანების ლისტი
for i in range(len(cars)):                                      # car-ის სიგრძე რამდენიც არის მაგხელა საფასურს აძლევს i ცვლადს ყოველ ლისტის იტერაციაზე
    print(cars[i])                                              # დაპრინტავს ყველაფერს ლისტში