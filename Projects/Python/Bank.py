# project bank 

def registration():                                                                         # აქ ვქმნით ფუნქციას registration რომელიც შეიცავს რეგისტრაციის კოდს
    print("Please Register!")
    full_name = input("Your name: ")
    new_password = input("Enter new password: ")                        
    repeat_password = input("Repeat the password: ")
    password_length = len(new_password)
    bank_online = False
    has_upper = False
    for i in new_password:                                                                  # ეს ამოწმებს ნუთუ არის თუ არა კოდში uppercase ასო/ასოები
        if i.isupper():
            bank_online = True
            has_upper = True 
            break
    if repeat_password != new_password:                                                     # თუ repeat_password არ უდრის new_password ატყობინებს მომხმარებელს
        print("The passwords did not match!")
        bank_online = False
    elif password_length < 8:                                                               # თუ პაროლში 8-ზე ნაკლები სიმბოლოა ატყობინებს მომხარებელს
        print("Password can't be less than 8 symbols")
        bank_online = False
    elif has_upper != True:                                                                 # ეუბნება მომხმარებელს რომ uppercase ასო აკლია
        print("Password should have an uppercase letter")
    elif bank_online != False:
        bank_online = True
    return bank_online

friend_name = ""

def add_friend():                                                                           # მეგობრების დამატების ფუნქცია
    transfer_list = ["Dad","Mom","Best friend","Sister","Brother","Girlfriend","Casino","Different Bank account",]
    transfer_list.append(friend_name)
    return transfer_list



def show_balance():                                                                         # ეს არის ფუნქცია რომელიც გვიჩვენებს მომხმარებლის ბალანსს
    print(f"here is your balance>  ${balance:2f}.") 


def cash_in():                                                                              # ფუნქცია რომელიც უფლებას გვაძლევს ბანკში შევიტანოთ ფული
    cash = float(input("How much money do you want to put in  "))
    if cash < 0:
        print ("you cant cash in a negative amount")
        return 0 
    else: 
        return cash


 
def withdraw():                                                                             # ფუნქცია რომელიც ბანკიდან ფულის გამოტანას გვაკეთებინებს
    cash=float(input("How much money do you want to withdraw  "))
    if cash > balance:
        print("you dont have that much money")
        return 0
    elif cash < 0:
        print("amount should be greater than 0 ")
        return 0
    else:
        return cash
    

def trans_friends():                                                                        # სხვა ექაუნთებში გადარიცხვის ფუნქცია
    print(add_friend())
    select_transfer = int(input("Who do you want to transfer money to?: ")) - 1
    if select_transfer < 0:
        print("none existant")
        return 0
    elif select_transfer > len(add_friend()):
        print("You don't know that much people")
        return 0

    if select_transfer == select_transfer:
        transfer_amount = float(input(f"How much money do you want to transfer to {add_friend()[select_transfer]}: "))
        if transfer_amount > balance:
            print("You dont have that much cash")
            return 0
        elif transfer_amount < 0 :
            print("You cant transfer a negative amount")
            return 0
        else:
            return transfer_amount


balance = 0 
bank_online = False


while bank_online == False:
    bank_online = registration()


while bank_online:
    print("""

          Wellcome to the [cyber Bank]""")
    print("""
1  >show balance
2  >cash in 
3  >witdraw
4  >transfers
5  >add a friend 
6  >exit
""")
    operation = (input("which operation would you like?  > "))
    if operation == '1':
        show_balance()



    elif operation == "2":
        balance = balance + cash_in()



    elif operation == "3":
        balance= balance - withdraw()

    elif operation == "4":
        balance = balance - trans_friends()

    if operation == "5":
        friend_name = input("Who would you like to add?: ")


    elif operation == "6":
        print("""
              
            
              

            Come again!
              
              


              """)
        bank_online = False 


    else:
        print("")