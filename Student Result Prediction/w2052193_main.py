# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20231943
# Date 22/11/2023
import w2052193_StudentVer
from graphics import *
# function to draw Text in histogram
def HistogramBarText(Text_X_axis,Bar,Result):
    # draws the text in histogram
    histoBarText = Text(Point(x, win.getHeight() - 80), Text_X_axis)
    histoBarText.setStyle("bold")
    histoBarText.setSize(17)
    histoBarText.setTextColor("grey")
    histoBarText.setFace("helvetica")
    histoBarText.draw(win)

    # draws the bars in the histogram
    histoBar = Rectangle(Point(x1, Bar), Point(x2, win.getHeight() - 100))
    histoBar.setFill(colours[i])
    histoBar.draw(win)

    # draws the bar names in histogram
    barText = Text(Point((x1 + 75), Bar - 15), Result)
    barText.setSize(17)
    barText.setStyle("bold")
    barText.setTextColor("grey")
    barText.setFace("helvetica")
    barText.draw(win)

validNumbers = [0,20,40,60,80,100,120]
check = ["y","q"]
Continue = "y"
progress = 0
moduleTrailer = 0
moduleRetriever = 0
exclude = 0
Data = open("Data.txt", "w")
Data.close()
DataList = []
versionCheck = ["1","2"]
while True:        # choose whether user is a student or a staff member
    version = input("For Student enter : 1\nFor Staff enter   : 2\n----------------------\n")
    if version not in versionCheck:
        print("Select a valid option")
        continue
    elif version == "1":
        w2052193_StudentVer.student()
        break
    elif version == "2":
        print("-- Staff --")
        while Continue == "y":
            try:
                while True:
                    PassCredit = int(input("Please enter your credits at Pass : "))         # get Credit input
                    if PassCredit in validNumbers:
                        DeferCredit = int(input("Please enter your credits at Defer : "))
                        if DeferCredit in validNumbers:
                            FailCredit = int(input("Please enter your credits at Fail : "))
                            if FailCredit in validNumbers:
                                total = PassCredit + DeferCredit + FailCredit
                                break
                            else:
                                print("Out of range\n")
                        else:
                            print("Out of range\n")
                    else:
                        print("Out of range\n")
                if total == 120 :                        # checking the outcome
                        if PassCredit == 120:
                            print("Progress")
                            progress += 1
                            outcome = "Progress"
                        elif PassCredit == 100:
                            print("Progress (module trailer)")
                            moduleTrailer += 1
                            outcome = "Progress (module trailer)"
                        elif (PassCredit + DeferCredit)>= FailCredit:
                            print("Do not progress - module retriever")
                            moduleRetriever += 1
                            outcome = "Module retriever"
                        elif (PassCredit + DeferCredit)<= FailCredit:
                            print("Exclude")
                            exclude += 1
                            outcome = "Exclude"
                        Results = [outcome,PassCredit,DeferCredit,FailCredit]
                        DataList.append(Results)
                        with open("Data.txt", "a") as Data:             # storing data in a text file
                            Data.write(f"{outcome} - {PassCredit},{DeferCredit},{FailCredit}\n")
                else:
                    print("Total incorrect")
                while True:                              # asking user whether to enter another set of values
                    Continue = input("\nWould you like to enter another set? \ny for Yes , q for Quit : ")
                    if Continue in check:
                        break
                    elif Continue not in check:          # prompt user to enter again if previous input out of range
                        print("Please enter y or q\n")
                        continue
            except ValueError:
                print("Integer required")
        print("\nData in list :")                            # printing the stored data
        for i in DataList:
            print(f"{i[0]}- {i[1]},{i[2]},{i[3]}")
        with open("Data.txt","r") as Data:
            print(f"\nData in Text file :\n{Data.read()}")

        # draws the window for the histogram
        win = GraphWin("Histogram", 730,600)
        totalOutcomes = [progress, moduleTrailer, moduleRetriever, exclude]
        colours = ["palegreen1", "darkseagreen", "yellow4", "rosybrown3"]
        histogramText = ["Progress", "Trailer", "Retriever", "Excluded"]
        maxValue = max(totalOutcomes)
        scale = (win.getHeight()-200)/maxValue                       # to determine the scale

        # determines the height for the histogram bars
        studentNum = (progress + moduleTrailer + moduleRetriever + exclude)
        progressBar = (win.getHeight()-100)-(progress*scale)       # 600 - 100 = 500
        moduleTrailerBar = (win.getHeight()-100)-(moduleTrailer*scale)
        moduleRetrieverBar = (win.getHeight()-100)-(moduleRetriever*scale)
        excludeBar = (win.getHeight()-100)-(exclude*scale)
        histoBars = [progressBar, moduleTrailerBar, moduleRetrieverBar, excludeBar]

        # sets the background colour in the window
        win.setBackground("Mint Cream")
        header = Text(Point(170,(win.getHeight()-100)-(maxValue*scale) - 60) ,"Histogram Results")
        header.setSize(20)
        header.setStyle("bold")
        header.setTextColor("grey")
        header.setFace("helvetica")
        header.draw(win)

        # line at the start of the histogram bars
        line = Line(Point(25, 500), Point(700, 500))
        line.setFill("grey")
        line.draw(win)

        x = 125
        x1 = 50
        x2 = 200
        # loop to draw text for the histogram x axis
        for i in range(4):
            HistogramBarText(histogramText[i],histoBars[i],totalOutcomes[i])
            x += 160
            x1 += 160
            x2 += 160

        # printing total number of outcomes
        count = Text(Point(190, 560), f"{studentNum} outcome(s) in total.")
        count.setSize(17)
        count.setStyle("bold")
        count.setTextColor("grey")
        count.setFace("helvetica")
        count.draw(win)
        win.getMouse()
        win.close()