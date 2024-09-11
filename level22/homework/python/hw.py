# 2) პითონში აქამდე რაც კი გვისწავლია ყველაფრის გამოყენებით გააკეთეთ მაქსიმალურად დახვეწილი რეგისტრაციის ფუნქციონალი, ეცადეთ რაც შეიძლება დახვეწოთ და გააუმჯობესოთ დაუმატოთ ბევრი ფუნქციონალები და ასე შემდეგ, აუცილებლად გამოიყენეთ ლუპები
while True:
    def registration():                                                                         
        print("Please Register!")
        fail_amount = 0
        bank_online = False
        while fail_amount <= 3 or bank_online == False:
            if fail_amount == 3:
                bank_online = False
                print("The bank account has been locked")
                break
            full_name = input("Your name: ")
            new_password = input("Enter new password: ")                        
            repeat_password = input("Repeat the password: ")
            password_length = len(new_password)
            has_upper = False
            for i in new_password:                                                                  
                if i.isupper():
                    bank_online = True
                    has_upper = True 
                    break
            if repeat_password != new_password:                                                     
                print("The passwords did not match!")
                bank_online = False
                fail_amount = fail_amount + 1
            elif password_length < 8:                                                               
                print("Password can't be less than 8 symbols")
                bank_online = False
                fail_amount = fail_amount + 1
            elif has_upper != True:                                                                 
                print("Password should have an uppercase letter")
                fail_amount = fail_amount + 1
            elif bank_online != False:
                bank_online = True
                break
        return bank_online

    print(registration())