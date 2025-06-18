from colorama import Fore, Style


def play_quiz():

    questions =(Fore.BLUE+"What is the capital of France?",
            Fore.BLUE+"Which planet is known as the Red Planet?",
            Fore.BLUE+"Who wrote the play 'Romeo and Juliet'?",
            Fore.BLUE+"What is the chemical symbol for water?",
            Fore.BLUE+"In what year did the Titanic sink?")

    options =((Fore.CYAN+"A) Berlin", Fore.CYAN+"B) London", Fore.CYAN+"C) Paris", Fore.CYAN+"D) Madrid"),
          (Fore.CYAN+"A) Earth", Fore.CYAN+"B) Mars", Fore.CYAN+"C) Jupiter", Fore.CYAN+"D) Venus"),
          (Fore.CYAN+"A) Charles Dickens", Fore.CYAN+"B) William Shakespeare", Fore.CYAN+"C) Mark Twain", Fore.CYAN+"D) Jane Austen"),
          (Fore.CYAN+"A) CO2", Fore.CYAN+"B) H2O", Fore.CYAN+"C) O2", Fore.CYAN+"D) NaCl"),
          (Fore.CYAN+"A) 1912", Fore.CYAN+"B) 1905", Fore.CYAN+"C) 1920", Fore.CYAN+"D) 1898"))

    answers =("C","B","B","B","A")

    question_num=0
    score=0
    

    yourname =input(Fore.YELLOW+"Hi! What's your name? ").upper()
    print(Fore.RED+f"Welcome to this quiz game {yourname}")
    print(Fore.YELLOW+"---------------------------------------")
    print(Fore.RED+"-----------Let's get started-----------")
    

    for question in questions:
        print(Fore.YELLOW+"---------------------------------------")
        print(Fore.BLUE+f"Q{question_num+1} {question}")
        for option in options[question_num]:
            print(option)

        guess= input("Enter the correct answer: (A, B, C, D)").upper()
        
        valid_ans=("A","B","C","D")
        
        while True:
            if guess in valid_ans:
                break
            print("Invalid option, Please select A, B, C or D")
            guess= input(Fore.YELLOW+"Enter the correct answer: (A, B, C, D)").upper()


        if guess ==answers[question_num]:
            print(Fore.GREEN+"Correct answer")
            score+=1

        else:
            print(Fore.RED+"Incorrect") 
            print(Fore.GREEN+f"The correct answer is {answers[question_num]}")   
        question_num+=1  



    print(Fore.YELLOW+"---------------------------------------")
    print(Fore.YELLOW+"---------------RESULT------------------")   
    print(Fore.YELLOW+"---------------------------------------")

    print(Fore.MAGENTA+f"Correct answers= {score}")
    print(Fore.MAGENTA+f"Your score= {score}/5")
    percent =(score/len(questions))*100
    print(Fore.MAGENTA+f"Your score percentage is :{percent}%")      

    if percent==100:
        print(Fore.CYAN+"Perfect")
    elif percent>=80:
        print(Fore.CYAN+"Well done")
    elif percent>=50:
        print(Fore.CYAN+"It's Okay! Do better next time")
    else:
        print(Fore.CYAN+"Better luck next time")   

while True:
    play_quiz()

    play_again =input(Fore.YELLOW+"do you wanna play again? yes/no ").lower()
    if play_again=="yes":
        play_quiz()
    else:
        print(Fore.MAGENTA+"Thank you")    
        break     

