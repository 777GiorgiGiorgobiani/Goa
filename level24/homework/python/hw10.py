# 5) 1-იდან 10-ის ჩათვლით არსებული ყველა რიცხვის კვადრატი გამოიტანეთ while ციკლის გამოყენებით.

count = 0
sum = 0

while count < 10:
    sum = count ** 2
    count = count + 1
    print(sum)
