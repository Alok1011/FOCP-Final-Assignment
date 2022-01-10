from os import system
import random

# A random operator is choosen and the format of the email is checked. 
def email_check(email):
    random_name=["Jerry","Scooby","Finn","Drake","Mikey","jane","blake"]
    index_count=0

    if email.count("@") == 1:
        for i in range(len(email)):
            if email[i] == "@" :
                index_count=i

    if email[index_count+1:]!="pop.ac.uk":
        print("The domain you entered is not valid!")
    else:
        name=email[:index_count].capitalize()
        print("Hi!",name,"Thank you, and Welcome to PopChat!")
        print("My name is "+random_name[random.randint(0,6)]+", and it will be my pleasure to help you.")
        question_answer(name)

# The function is used to check the question and reply accordingly.
def question_answer(name):
    que=["library","wifi","deadline","routine","coffee","teacher"]
    ans=["The library is closed today.","WiFi is excellent across the campus.","Your deadline has been extended by two working days.","The Routine will be sent to you via your email.","Java is open until 8pm this evening.","He will be there!"]
    while True:
        ran_num=0

        question=input("-->")
        random_network_fail(name)
        
        # Used to print the answer according to the question asked from the list.
        for i in range(6):
            if que[i] in question.lower():
                print(ans[i])
                ran_num=1
                break
        
        if ran_num == 0:
            # Used to check if the user wants to exit or not.
            if ("bye" in question.lower()) or ("exit" in question.lower()) or ("done" in question.lower()) or ("help" in question.lower()):
                print("Thanks",name,"for using PopChat. See you again soon!")
                exit()

            # If the answer is not available then a random answer is given.
            else:
                ran_ans=["Hmm","oh, i see","Tell me more","That is interesting.","Is it so?","Let me see"]
                print(ran_ans[random.randint(0,5)])

# Used for a random network error.
def random_network_fail(name):
    if random.randint(1,10) == 1:
        print("*** NETWORK ERROR ***")
        print("Thanks",name,"for using PopChat. See you again soon!")
        exit()

system("cls")
print("Welcome to Pop Chat \nOne of our operators will be pleased to help you today.")

email=input("Please enter your Poppleton email address:")
email_check(email)