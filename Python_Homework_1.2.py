total=0
count=0
while True:
    user_input=input()
    if user_input=="done":
        break
    total+=int(user_input)
    count+=1
print(f"The sum of input numbers is {total}")
print(f"The qantitiy of input numbers is {count}")
print(f"The average of input numbers is {total/count}")
    