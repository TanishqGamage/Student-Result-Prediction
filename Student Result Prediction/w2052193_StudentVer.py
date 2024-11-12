# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20231943
# Date 22/11/2023

#   STUDENT VERSION

def student():
    print("-- Student --")
    validNumbers = [0,20,40,60,80,100,120]  # list of valid numbers
    progress = 0
    moduleTrailer = 0
    moduleRetriever = 0
    exclude = 0
    try:
        while True:
            PassCredit = int(input("Please enter your credits at Pass : "))  # get Credit input
            if PassCredit in validNumbers:
                DeferCredit = int(input("Please enter your credits at Defer : "))
                if DeferCredit in validNumbers:
                    FailCredit = int(input("Please enter your credits at Fail : "))
                    if FailCredit in validNumbers:
                        total = PassCredit + DeferCredit + FailCredit
                        break
                    else:
                        # prints 'out of range' if entered number not in list
                        print("Out of range\n")
                else:
                    print("Out of range\n")
            else:
                print("Out of range\n")
        if total == 120:  # checking the outcome
            if PassCredit == 120:
                print("\nProgress")
                progress += 1     # increments progress count
            elif PassCredit == 100:
                print("\nProgress (module trailer)")
                moduleTrailer += 1
            elif (PassCredit + DeferCredit) >= FailCredit:
                print("\nDo not progress - module retriever")
                moduleRetriever += 1
            elif (PassCredit + DeferCredit) <= FailCredit:
                print("\nExclude")
                exclude += 1
        else:
            print("Total incorrect")
    except ValueError:
        print("Integer required")