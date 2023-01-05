
message = '''Ahoy There, Me Hearties! ٩(•̮̮̃-̃)۶🏴‍☠️
We're in 🔍 search for a new captain who is good in multiplying 'cause we're in quest to answer the multiplication 
questions that magical dragon 🐉 asks, so it can multiply our treasures 💰 like how we wanted.  

If you think you need more practice, we suggest you choose to train first. 💪

If you think you're ready to multiple that treasure we found, you can proceed to ace the dragon's test! ✊ \n '''
print(message)

print(end="Enter a number you want to learn: ")

num = int(input())
print("\nMultiplication Table of " + str(num) + "\n")

for i in range(1, 11):
    print(str(num) + " x " + str(i) + " = " + str(num*i))

print("\nAvast Ye, lad! Loot that information, we gonna need that! More, more, we gotta learn some more!🔎")
