def words():
    text=input("Enter the words you want to compare(After every word please insert some space) ")

    longest=0

    for b in text.split():
        if len(b)>longest:
           longest=len(b)
    print("The longest word is", b ,"with a length of " , longest)
    return 0

words()
a=input("Enter any key to exit")

