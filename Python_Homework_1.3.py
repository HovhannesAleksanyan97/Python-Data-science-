list1=["a","e","i","o","u"]
user_input=input("Enter a letter")
if(user_input in list1):
    print(f"{user_input} is vowel")
elif(user_input=="y"):
    print(f"{user_input} is both vowel and consonant")
else:
    print(f"{user_input}is consonant")