print("Welcome to Quiz Game ")
playing = input("Do you want to play? ")
print(playing)
if playing.lower() != "yes":
    print("Looks like you don't want to play. Bye, Have a nice day.")
    quit()
print("let's play")
score = 0


answer = input("What is the capital of Bangladesh? ")
if answer.lower() == "dhaka":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("How many district in Bangladesh? ")
if answer.lower() == "64" or answer.lower() == "sixty four":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("What is the mother language of Bangladesh? ")
if answer.lower() == "bengali" or answer.lower() == "bangla":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("How many division in Bangladesh? ")
if answer.lower() == "8" or answer.lower() == "eight":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
print("Your Score Is ",score)
print("You Got "+ str((score/4)*100)+ "%")    
