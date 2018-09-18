import random
import time

username = 'begin'
#program asks for username
while(username):
    username = ''
    username = input("Username: ")
    if(username != ''):
        startQuestion = input("Do you want to begin the game {} (y/n)?".format(username))
        if(startQuestion == "y"):
                #program needs to randomize questions
                questionAnswer = 0
                userAnswer = 0
                #loop the questions while error < 10 and correct answer < 10
                errors = 0
                corrects = 0
                while errors < 10 and corrects < 10:
                    starttime = time.time()
                    operation = random.randint(0, 3)
                    firstNum = random.randint(10, 99)
                    secondNum = random.randint(10, 99)
                    #for addition
                    if(operation == 0):
                        questionAnswer = firstNum + secondNum
                        print ("What is {} {} {}?".format(firstNum, ' + ', secondNum))
                        userAnswer = int(input("Answer: "))
                        if(userAnswer == questionAnswer):
                            print("Your answer is CORRECT!")
                            corrects += 1
                        else:
                            print("Your answer is WRONG!")
                            errors += 1
                    #for subtraction
                    elif(operation == 1):
                        if(firstNum > secondNum):
                            questionAnswer = firstNum - secondNum
                            print ("What is {} {} {}?".format(firstNum, ' - ', secondNum))
                            userAnswer = int(input("Answer: "))
                            if(userAnswer == questionAnswer):
                                print("Your answer is CORRECT!")
                                corrects += 1
                            else:
                                print("Your answer is WRONG!")
                                errors += 1
                        else:
                            operation = random.randint(0,3)
                            firstNum = random.randint(10, 99)
                            secondNum = random.randint(10, 99)
                    #for multiplication
                    elif(operation == 2):
                        if(firstNum or secondNum != 1):
                            questionAnswer = firstNum * secondNum
                            print ("What is {} {} {}?".format(firstNum, ' x ', secondNum))
                            userAnswer = float(input("Answer: "))
                            if(userAnswer == questionAnswer):
                                print("Your answer is CORRECT!")
                                corrects += 1
                            else:
                                print("Your answer is WRONG!")
                                errors += 1
                        else:
                            operation = random.randint(0,3)
                            firstNum = random.randint(10, 99)
                            secondNum = random.randint(10, 99)
                    #for division
                    elif(operation == 3):
                        secondNum = random.randint(2,9)
                        firstNum = random.randint(100,999)
                        if(firstNum % secondNum > 0 and firstNum or secondNum != 1):
                            questionAnswer = firstNum / secondNum
                            print ("What is {} {} {}?".format(firstNum, ' / ', secondNum))
                            userAnswer = float(input("Answer: "))
                            if(userAnswer == questionAnswer):
                                print("Your answer is CORRECT!")
                                corrects += 1
                            else:
                                print("Your answer is WRONG!")
                                errors += 1
                        else:
                            operation = random.randint(0,3)
                            firstNum = random.randint(100,999)
                            secondNum = random.randint(2,9)
                print("Thanks for playing.")
                endtime = time.time() - starttime
                minutes = 0
                seconds = 0
                if(endtime > 0.100):
                    seconds += 1
                if(seconds > 60):
                    seconds = 0
                    minutes += 1
                totaltime = str(minutes) + ':' + str(seconds)
                result = {
                    'Username: ': username,
                    'Time: ': totaltime,
                    'Score: ': corrects,
                    'Errors: ': errors
                    }
                print (result)
        else:
            print("Goodbye.")
    else:
        leaderboard = []
        for i in range(0,10):
            result['Username','Time','Score','Errors'] = i
            leaderboard.append(result)
        print (leaderboard)
        
