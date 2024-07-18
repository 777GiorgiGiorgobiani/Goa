#  2) შექმენით პროგრამა რომელსაც შეეძლება დიალოგი თქვენთან (აირჩიეთ ნებისმიერი თემა) input გამოყენებით

print("pick one of the included hobbies:")
hobby = input("Programming, Gaming, Music, Art: ")

if hobby == "Programming":
    print("I love", hobby + ",")
    language = input("What is your favorite programming language? ")
    print(language, "is such a great programming language!")


elif hobby == "Gaming":
    print("I love", hobby + ",")
    fav_game = input("What is your favorite game? ")
    print("I also love", fav_game + "!", "we should play it together.")


elif hobby == "Music":
    print("I love", hobby + ",")
    fav_band = input("What is your favorite band? " )
    print("Hell yeah!", "we should go to a", fav_band, "concert!")
else:
    print("I love", hobby + ",")
    fav_artist = input("Who is your favorite artist? ")
    print("Interesting, I have seen", fav_artist + "'s", "Art, they are solid.")
