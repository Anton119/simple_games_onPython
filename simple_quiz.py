## quiz consisted of 5 questions about Russia
print("Welcome to the quiz about Russia!")
score = 0
player = input("Are you ready to start? ")
if player.lower() == "yes":
    print("Okay! Let's start!")
else:
    quit()
answer = input("What is the official name of Russia? ")
if answer.lower() == "the russian federation":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
answer = input("Is Russia the biggest country in the world? ")
if answer.lower() == "yes":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
answer = input("What is the capital of Russia? ")
if answer.lower() == "moscow":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
answer = input("What is the abbreviation of the country existed untill 1991 on the territory of modern Russia? ")
if answer.upper() == "USSR":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
answer = input("Do Russians use rubles or dollars paying inside the country? ")
if answer.lower() == "rubles":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
print(f"Congratulations, you've got {score} scores out of 5!")
    
