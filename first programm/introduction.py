"""My first program."""

print("Hello, my name is Python! Please type your name to continue our conversation.")

name = input("What's your name?")

print("Hello, " + name + "!")

answer = input("Have you programmed before?")

if answer == "Yes":

    print("Congratulations, " + name + "! It will be a little bit easier for you.")

elif answer == "No":

    print("Don`t worry, " + name + "! You will learn everything you need.")

else:

    print("Your input is incorrect!")
