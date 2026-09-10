a = int(input("Enter your age: "))

# if elif else ladder
if(a >= 18):
    print('You are eligible to vote.')
    print('That is great!')

elif(a < 0):
    print("Please enter a valid age.")

else:
    print('You are not eligible to vote.')
    print('Sorry!')
