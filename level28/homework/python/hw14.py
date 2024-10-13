# 14) შექმენით სია სადაც შეტანილი გექნებათ 30-იდან 50-ის ჩათვლით კენტი რიცხვები. შემდეგ დაპტინტეთ სამი უმცირესი ელემენტის ჯამი.

nums = [31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

highest = sorted(nums, reverse=True)[0]

nums2 = []

for i in nums:
    if i < highest:
        nums2.append(i)
        if len(nums2) == 3:
            break



print(sum(nums2))