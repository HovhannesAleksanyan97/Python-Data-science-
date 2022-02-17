list1=["a","c","e","g"]
list2=["b","d","f","h"]
list3=[1,3,5,7]
list4=[2,4,6,8]

user_input1=input("Enter the first coordinate of the chess square")
user_input2=int(input("Enter the second coordinate of the chess square"))
if user_input1 in list1 and user_input2 in list3 or (user_input1 in list2 and user_input2 in list4):
    print("Square is black")
elif user_input1 in list1 and user_input2 in list4 or (user_input1 in list2 and user_input2 in list3):
    print("Square is white")
else:
    print("Invalid input")
