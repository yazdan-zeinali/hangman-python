import random
 
programs = ("python", "php", "javascript", "c", "perl", "c++", "java", "ruby", "c#", "html", "fortran" , "css")
 
answer = random.choice(programs)
 
correct = answer
rumble="" 
while answer:
    position = random.randrange(len(answer))
    rumble += answer[position]
    answer = answer[:position] + answer[(position + 1):]
 
print("welcome to hangman!!! . lets guess programing language") 
guess = input("Guess This Programming Language:")
guess = guess.lower()
 
while (guess != correct) or (guess == ""):
    print("That is not the correct answer")
    guess = input("Guess This Programming Language:")
    guess = guess.lower()
    
 
if guess == correct:
    print("Congratulation You Win!")
    input("\n\n Press enter to exit")
