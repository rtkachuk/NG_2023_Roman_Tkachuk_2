def askUserIntValue(message):
    return int(input(message))

def answerUserAge(age):
    if age < 6:
        print ("Rano v shkolu")
    elif age > 5:
        print ("Bistro v shkolu!")
    else:
        print  ("KEK")
        
def main():
    answerUserAge(askUserIntValue("Сколько тебе лет? "))

main()