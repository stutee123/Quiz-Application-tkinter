
from tkinter import *
from PIL import ImageTk,Image
import random

root=Tk()
root.title("Quiz Game")
root.geometry('700x600')
root.config(background='white')
root.resizable(0,0)

def nextPage():
    
    imageLabel.destroy()
    textLabel.destroy()      
    introLabel.destroy()
    instructionLabel.destroy()
    startButton.destroy()
    mainGame()

def mainGame():
#for python
    def pythonQuiz():
        questions = [
            "Which is not a data type?",
            "What will be the output of \nthe following Python code snippet? \n\n not(10<20) and not(10>30)",
            "What will be the output of \nthe following Python code snippet?\n\nX=”hi”\nprint(“05d”%X)",
            "What will be the output of \nthe following Python code?\n\ni = 1\nwhile True:if i%2 == 0:\nbreak\nprint(i)\ni += 2",
            "What will be the output of the following Python code?\n\ndef f1():\nx=15\nprint(x)\nx=12\nf1()",
            "Which is a tuple?",
            "What is the answer to this expression, 22 % 3 is?",
            "Which one of the following has \nthe highest precedence in the expression?",
            "Which of the following statements create a dictionary?",
            "Which gives the length of a list?"
        ]

        answers = [
            ["1. Lists","2. sets","3. Dictionary","4. class"],
            ["1. True","2. False","3. error","4. no output"],
            ["1.  00000hi","2. 000hi","3. hi000","4. error"],
            ["1. 1","2. 1 3 5 7 ...","3. 1 2 3 4 ...","4. none of the mentioned"],
            ["1. error","2. 12","3. 15","4. 1512"],
            ["1. [1,2,3]","2. (1,2,3)","3. {1,2,3}","4. {}"],
            ["1. 7","2. 1","3. 0","4. 5"],
            ["1. exponential","2. addition","3. multiplication","4. parentheses"],
            ["1. d = {}","2. d = {“john”:40, “peter”:45}","3. d = {40:”john”, 45:”peter”}","4. All of the mentioned"],
            ["1. len()","2. size()","3. none","4. 1 and 2"],
        ]
        global realans
        realans = [3,1,3,3,2,1,1,3,3,0]
      
        global userAnswers
        userAnswers = []
        global list
        list = []
        def randomQuesGenerator():
            while(len(list) < 5):
                x=  random.randint(0,9)
                if x in list:
                    continue
                else:
                    list.append(x)
        randomQuesGenerator()

        def showresult(score):
            questionLabel.destroy()
            radioButton1.destroy()
            radioButton2.destroy()
            radioButton3.destroy()
            radioButton4.destroy()
            backButton.destroy()
            
            labelimage=Label(root,background="white")
            labelimage.pack(pady=(60,0))
            labelresulttext=Label(root, font=("Frabklin Gothic", 16, "bold"), background="white")
            labelresulttext.pack(pady=(30,0))
            exitButton=Button(root, text="Exit",font=("Book antiqua", 10,"bold"),border=1,background="red", foreground="white", command=quit)
            exitButton.pack(pady=(20,0))
            if score>=20:
                imgwin = ImageTk.PhotoImage(Image.open("win.png"))
                labelimage.config(image=imgwin)
                labelimage.image=imgwin
                labelresulttext.config(text="CONGRATULATIONS!! You won.")
            else:
                imgwin = ImageTk.PhotoImage(Image.open("lose.png"))
                labelimage.config(image=imgwin)
                labelimage.image=imgwin
                labelresulttext.config(text="SORRY!! Try again.")

        def calc():
            global list,userAnswers,realans
            x = 0
            score = 0
            for i in list:
                if userAnswers[x]==realans[i]:
                    score+=5
                x+=1
            showresult(score)
            
        global ques
        ques = 1
        def selected():
            global ques,userAnswers,radiovar, questionLabel, radioButton1, radioButton2, radioButton3, radioButton4
            x = radiovar.get()
            radiovar.set(-1)
            userAnswers.append(x)
            if ques < 5:
                questionLabel.config(text=questions[list[ques]])
                radioButton1['text'] = answers[list[ques]][0]
                radioButton2['text'] = answers[list[ques]][1]
                radioButton3['text'] = answers[list[ques]][2]
                radioButton4['text'] = answers[list[ques]][3]
                ques += 1
            else:
                calc()

        def startQuiz():
            global questionLabel, radiovar, radioButton1, radioButton2, radioButton3, radioButton4

            questionLabel = Label(root, text=questions[list[0]], font=("Frabklin Gothic", 14), justify="center",background="white",foreground="dark blue")
            questionLabel.pack(pady=(70,0))

            radiovar = IntVar()
            #radiovar.set(-1)

            radioButton1 = Radiobutton(root, text=answers[list[0]][0], background="white", font=("Frabklin Gothic", 14),value=0,variable=radiovar,command=selected)
            radioButton1.pack(pady=(30,0))

            radioButton2 = Radiobutton(root, text = answers[list[0]][1], background="white", font=("Frabklin Gothic", 14),value=1,variable=radiovar,command=selected)
            radioButton2.pack(pady=(20,0))

            radioButton3 = Radiobutton(root, text = answers[list[0]][2], background="white", font=("Frabklin Gothic", 14),value=2,variable=radiovar,command=selected)
            radioButton3.pack(pady=(20,0))

            radioButton4 = Radiobutton(root, text = answers[list[0]][3],background="white", font=("Frabklin Gothic", 14),value=3,variable=radiovar,command=selected)
            radioButton4.pack(pady=(20,0))
        startQuiz()

        def back():

            questionLabel.destroy()
            radioButton1.destroy()
            radioButton2.destroy()
            radioButton3.destroy()
            radioButton4.destroy()
            backButton.destroy()
            programmingChoice()
            
        backButton=Button(root, text="Back",command=back)
        backButton.pack(pady=(40,0))
        

    def python():
            textLabel2.destroy()
            pythonButton.destroy()
            javaButton.destroy()
            seButton.destroy()
            oopButton.destroy()
            cppButton.destroy()
            exitButton.destroy()
            pythonQuiz()
            
    def againNextPage():
        return
#for java
    def javaQuiz():
        questions = [
            "Which of the following is not a \nJava features?",
            " _____ is used to find and fix\n bugs in the Java programs.",
            "Which of the following is a valid long literal?",
            "Evaluate the following Java expression:\n\n if x=3, y=5, and z=10:\n++z + y - y + z + x++",
            "Which of the following creates a List\n of 3 visible items and multiple selections abled?",
            "Which of the following is a reserved\n keyword in Java?",
            "int values[ ] = {1,2,3,4,5,6,7,8,9,10};  \nfor(int i=0;i< Y; ++i)  \nSystem.out.println(values[i]);  \nFind the value of value[i]?",
            "Which of the following is not OOPS concept\n in Java?",
            "What is the return type of a method that \ndoes not return any value?",
            "Which method can be defined only\n once in a program?"
        ]

        answers = [
            ["1. Dynamic","2. Architecture neutral","3. Use of poiners","4. object-oriented"],
            ["1. JVM","2. JRE","3. JDK","4. JDB"],
            ["1. ABH8097","2. L990023","3. 904423","4. 0xnf029L"],
            ["1. 24","2. 23","3. 20","4. 25"],
            ["1. new List(false, 3)","2. new List(3, true)","3. new List(true, 3)","4. new List(3, false)"],
            ["1. object","2. strictfp","3. main","4. system"],
            ["1. 10","2. 11","3. 15","4. None of the above"],
            ["1. inheritance","2. encapsulation","3. polymorphism","4. compilation"],
            ["1. int","2. float","3. void", "4. double"],
            ["1. main method","2. finalize method","3. static method","4. none"],
        ]
        global realans
        realans = [2,3,3,0,1,1,3,3,2,0]
        
        global userAnswers
        userAnswers = []
        global list
        list = []
        def randomQuesGenerator():
            while(len(list) < 5):
                x=  random.randint(0,9)
                if x in list:
                    continue
                else:
                    list.append(x)
        randomQuesGenerator()

        def showresult(score):
            questionLabel.destroy()
            radioButton1.destroy()
            radioButton2.destroy()
            radioButton3.destroy()
            radioButton4.destroy()
            backButton.destroy()
            
            labelimage=Label(root,background="white")
            labelimage.pack(pady=(60,0))
            labelresulttext=Label(root, font=("Frabklin Gothic", 16, "bold"), background="white")
            labelresulttext.pack(pady=(30,0))
            exitButton=Button(root, text="Exit",font=("Book antiqua", 10,"bold"),border=1,background="red", foreground="white", command=quit)
            exitButton.pack(pady=(20,0))
            if score>=20:
                imgwin = ImageTk.PhotoImage(Image.open("win.png"))
                labelimage.config(image=imgwin)
                labelimage.image=imgwin
                labelresulttext.config(text="CONGRATULATIONS!! You won.")
            else:
                imgwin = ImageTk.PhotoImage(Image.open("lose.png"))
                labelimage.config(image=imgwin)
                labelimage.image=imgwin
                labelresulttext.config(text="SORRY!! Try again.")

        def calc():
            global list,userAnswers,realans
            x = 0
            score = 0
            for i in list:
                if userAnswers[x]==realans[i]:
                    score+=5
                x+=1
            showresult(score)
            
        global ques
        ques = 1
        def selected():
            global ques,userAnswers,radiovar, questionLabel, radioButton1, radioButton2, radioButton3, radioButton4
            x = radiovar.get()
            radiovar.set(-1)
            userAnswers.append(x)
            if ques < 5:
                questionLabel.config(text=questions[list[ques]])
                radioButton1['text'] = answers[list[ques]][0]
                radioButton2['text'] = answers[list[ques]][1]
                radioButton3['text'] = answers[list[ques]][2]
                radioButton4['text'] = answers[list[ques]][3]
                ques += 1
            else:
                calc()

        def startQuiz():
            global questionLabel, radiovar, radioButton1, radioButton2, radioButton3, radioButton4

            questionLabel = Label(root, text=questions[list[0]], font=("Frabklin Gothic", 14), justify="center",background="white",foreground="dark blue")
            questionLabel.pack(pady=(70,0))

            radiovar = IntVar()
            #radiovar.set(-1)

            radioButton1 = Radiobutton(root, text=answers[list[0]][0], background="white", font=("Frabklin Gothic", 14),value=0,variable=radiovar,command=selected)
            radioButton1.pack(pady=(30,0))

            radioButton2 = Radiobutton(root, text = answers[list[0]][1], background="white", font=("Frabklin Gothic", 14),value=1,variable=radiovar,command=selected)
            radioButton2.pack(pady=(20,0))

            radioButton3 = Radiobutton(root, text = answers[list[0]][2], background="white", font=("Frabklin Gothic", 14),value=2,variable=radiovar,command=selected)
            radioButton3.pack(pady=(20,0))

            radioButton4 = Radiobutton(root, text = answers[list[0]][3],background="white", font=("Frabklin Gothic", 14),value=3,variable=radiovar,command=selected)
            radioButton4.pack(pady=(20,0))
        startQuiz()

        def back():

            questionLabel.destroy()
            radioButton1.destroy()
            radioButton2.destroy()
            radioButton3.destroy()
            radioButton4.destroy()
            backButton.destroy()
            programmingChoice()
            
        backButton=Button(root, text="Back",command=back)
        backButton.pack(pady=(40,0))
       
        

    def java():
            textLabel2.destroy()
            pythonButton.destroy()
            javaButton.destroy()
            seButton.destroy()
            oopButton.destroy()
            cppButton.destroy()
            exitButton.destroy()
            javaQuiz()
#for software engineering
    def seQuiz():
        questions = [
            "RAD Software process model stands for _____ .",
            "COCOMO stands for ______ .",
            "Which factors affect the probable \nconsequences if a risk occur?",
            "Which of the following is not defined\n in a good Software Requirement \nSpecification (SRS) document?",
            "Mention any two indirect measures of \nproduct.",
            "Software Requirement Specification (SRS)\n is also known as specification \nof _______.",
            "Abbreviate the term PERT.",
            "Which is the characteristics of\n Software risk?",
            "Which model depicts the profile \nof the end users of a computer system?",
            " Abbreviate the term SRS."
        ]

        answers = [
            ["1. Rapid Application Development.","2. Relative Application Development.","3. Rapid Application Design.","4.  Recent Application Development."],
            ["1. COnsumed COst MOdel ","2. COnstructive COst MOdel","3. COmmon COntrol MOdel","4. COmposition COst MOdel"],
            ["1. Risk avoidance","2. Risk monitoring","3. Risk timing","4. Contingency planning"],
            ["1. Functional requirement","2. Nonfunctional requirement","3. Goals of implementation","4. Algorithm for software implementation"],
            ["1. Quality","2. Efficiency","3. Accuracy","4. Both 1. and 2."],
            ["1. White box testing","2. Acceptance testing","3. Integrated testing","4. Black box testing"],
            ["1. Program Evolution & Review Technique","2. Process Evolution & Review Tool","3. Project Evalution & Request Technique","4. None of the above"],
            ["1. Uncertainity","2. Loss","3. Both 1. and 2.","4. None of the above"],
            ["1. User model","2. Requirements model","3. Design model", "4. State model"],
            ["1. Software Requirement Specification","2.  Software Refining Solution","3. Software Resource Source","4. none"],
        ]
        global realans
        realans = [0,1,2,3,3,3,0,2,0,0]
        
        global userAnswers
        userAnswers = []
        global list
        list = []
        def randomQuesGenerator():
            while(len(list) < 5):
                x=  random.randint(0,9)
                if x in list:
                    continue
                else:
                    list.append(x)
        randomQuesGenerator()

        def showresult(score):
            questionLabel.destroy()
            radioButton1.destroy()
            radioButton2.destroy()
            radioButton3.destroy()
            radioButton4.destroy()
            backButton.destroy()
            
            labelimage=Label(root,background="white")
            labelimage.pack(pady=(60,0))
            labelresulttext=Label(root, font=("Frabklin Gothic", 16, "bold"), background="white")
            labelresulttext.pack(pady=(30,0))
            exitButton=Button(root, text="Exit",font=("Book antiqua", 10,"bold"),border=1,background="red", foreground="white", command=quit)
            exitButton.pack(pady=(20,0))
            if score>=20:
                imgwin = ImageTk.PhotoImage(Image.open("win.png"))
                labelimage.config(image=imgwin)
                labelimage.image=imgwin
                labelresulttext.config(text="CONGRATULATIONS!! You won.")
            else:
                imgwin = ImageTk.PhotoImage(Image.open("lose.png"))
                labelimage.config(image=imgwin)
                labelimage.image=imgwin
                labelresulttext.config(text="SORRY!! Try again.")

        def calc():
            global list,userAnswers,realans
            x = 0
            score = 0
            for i in list:
                if userAnswers[x]==realans[i]:
                    score+=5
                x+=1
            showresult(score)
            
        global ques
        ques = 1
        def selected():
            global ques,userAnswers,radiovar, questionLabel, radioButton1, radioButton2, radioButton3, radioButton4
            x = radiovar.get()
            radiovar.set(-1)
            userAnswers.append(x)
            if ques < 5:
                questionLabel.config(text=questions[list[ques]])
                radioButton1['text'] = answers[list[ques]][0]
                radioButton2['text'] = answers[list[ques]][1]
                radioButton3['text'] = answers[list[ques]][2]
                radioButton4['text'] = answers[list[ques]][3]
                ques += 1
            else:
                calc()

        def startQuiz():
            global questionLabel, radiovar, radioButton1, radioButton2, radioButton3, radioButton4

            questionLabel = Label(root, text=questions[list[0]], font=("Frabklin Gothic", 14), justify="center",background="white",foreground="dark blue")
            questionLabel.pack(pady=(70,0))

            radiovar = IntVar()
            #radiovar.set(-1)

            radioButton1 = Radiobutton(root, text=answers[list[0]][0], background="white", font=("Frabklin Gothic", 14),value=0,variable=radiovar,command=selected)
            radioButton1.pack(pady=(30,0))

            radioButton2 = Radiobutton(root, text = answers[list[0]][1], background="white", font=("Frabklin Gothic", 14),value=1,variable=radiovar,command=selected)
            radioButton2.pack(pady=(20,0))

            radioButton3 = Radiobutton(root, text = answers[list[0]][2], background="white", font=("Frabklin Gothic", 14),value=2,variable=radiovar,command=selected)
            radioButton3.pack(pady=(20,0))

            radioButton4 = Radiobutton(root, text = answers[list[0]][3],background="white", font=("Frabklin Gothic", 14),value=3,variable=radiovar,command=selected)
            radioButton4.pack(pady=(20,0))
        startQuiz()

        def back():

            questionLabel.destroy()
            radioButton1.destroy()
            radioButton2.destroy()
            radioButton3.destroy()
            radioButton4.destroy()
            backButton.destroy()
            programmingChoice()
            
        backButton=Button(root, text="Back",command=back)
        backButton.pack(pady=(40,0))
       
        

    def se():
            textLabel2.destroy()
            pythonButton.destroy()
            javaButton.destroy()
            seButton.destroy()
            oopButton.destroy()
            cppButton.destroy()
            exitButton.destroy()
            seQuiz()
            

#for object oriented programming
    def oopQuiz():
        questions = [
            " Which of the following best \ndefines a class?",
            "Who invented OOP?",
            "Which is not feature of OOP in \ngeneral definitions?",
            "How many classes can be defined \nin a single program?",
            "Which of the two features match \neach other?",
            "Which feature allows open recursion,\n among the following?",
            "Which feature can be implemented \nusing encapsulation?",
            "Which among the following violates \nthe principle of encapsulation almost always?",
            "Which among the following can show \npolymorphism?",
            " Which type of function among the \nfollowing shows polymorphism?"
        ]

        answers = [
            ["1. Parent of an object","2. Instance of an object","3. Blueprint of an object","4. Scope of an object"],
            ["1. Alan Kay","2.  Andrea Ferro","3. Dennis Ritchie","4. Adele Goldberg"],
            ["1. Code reusability","2. Modularity","3. Redundant data","4. Efficient code"],
            ["1. Only 1","2. 100","3. 999","4. as many as you want"],
            ["1. Inheritance and Encapsulation","2. Encapsulation and Polymorphism","3. Encapsulation and Abstraction","4. Abstraction and Polymorphism"],
            ["1. Use of this pointer","2. Use of pointers","3. Use of pass by value","4. Use of parameterized constructor"],
            ["1. Inheritance","2. Abstraction","3. Polymorphism","4. Overloading"],
            ["1. Local variables","2. Global variables","3. Public variables","4. Array variables"],
            ["1. Overloading ||","2. Overloading +=","3. Overloading <<", "4.  Overloading &&"],
            ["1. Inline function","2. Virtual function","3. Undefined functions","4. Undefined functions"],
        ]
        global realans
        realans = [2,0,2,3,2,0,1,1,2,1]
        
        global userAnswers
        userAnswers = []
        global list
        list = []
        def randomQuesGenerator():
            while(len(list) < 5):
                x=  random.randint(0,9)
                if x in list:
                    continue
                else:
                    list.append(x)
        randomQuesGenerator()

        def showresult(score):
            questionLabel.destroy()
            radioButton1.destroy()
            radioButton2.destroy()
            radioButton3.destroy()
            radioButton4.destroy()
            backButton.destroy()
            
            labelimage=Label(root,background="white")
            labelimage.pack(pady=(60,0))
            labelresulttext=Label(root, font=("Frabklin Gothic", 16, "bold"), background="white")
            labelresulttext.pack(pady=(30,0))
            exitButton=Button(root, text="Exit",font=("Book antiqua", 10,"bold"),border=1,background="red", foreground="white", command=quit)
            exitButton.pack(pady=(20,0))
            if score>=20:
                imgwin = ImageTk.PhotoImage(Image.open("win.png"))
                labelimage.config(image=imgwin)
                labelimage.image=imgwin
                labelresulttext.config(text="CONGRATULATIONS!! You won.")
            else:
                imgwin = ImageTk.PhotoImage(Image.open("lose.png"))
                labelimage.config(image=imgwin)
                labelimage.image=imgwin
                labelresulttext.config(text="SORRY!! Try again.")

        def calc():
            global list,userAnswers,realans
            x = 0
            score = 0
            for i in list:
                if userAnswers[x]==realans[i]:
                    score+=5
                x+=1
            showresult(score)
            
        global ques
        ques = 1
        def selected():
            global ques,userAnswers,radiovar, questionLabel, radioButton1, radioButton2, radioButton3, radioButton4
            x = radiovar.get()
            radiovar.set(-1)
            userAnswers.append(x)
            if ques < 5:
                questionLabel.config(text=questions[list[ques]])
                radioButton1['text'] = answers[list[ques]][0]
                radioButton2['text'] = answers[list[ques]][1]
                radioButton3['text'] = answers[list[ques]][2]
                radioButton4['text'] = answers[list[ques]][3]
                ques += 1
            else:
                calc()

        def startQuiz():
            global questionLabel, radiovar, radioButton1, radioButton2, radioButton3, radioButton4

            questionLabel = Label(root, text=questions[list[0]], font=("Frabklin Gothic", 14), justify="center",background="white",foreground="dark blue")
            questionLabel.pack(pady=(70,0))

            radiovar = IntVar()
            #radiovar.set(-1)

            radioButton1 = Radiobutton(root, text=answers[list[0]][0], background="white", font=("Frabklin Gothic", 14),value=0,variable=radiovar,command=selected)
            radioButton1.pack(pady=(30,0))

            radioButton2 = Radiobutton(root, text = answers[list[0]][1], background="white", font=("Frabklin Gothic", 14),value=1,variable=radiovar,command=selected)
            radioButton2.pack(pady=(20,0))

            radioButton3 = Radiobutton(root, text = answers[list[0]][2], background="white", font=("Frabklin Gothic", 14),value=2,variable=radiovar,command=selected)
            radioButton3.pack(pady=(20,0))

            radioButton4 = Radiobutton(root, text = answers[list[0]][3],background="white", font=("Frabklin Gothic", 14),value=3,variable=radiovar,command=selected)
            radioButton4.pack(pady=(20,0))
        startQuiz()

        def back():

            questionLabel.destroy()
            radioButton1.destroy()
            radioButton2.destroy()
            radioButton3.destroy()
            radioButton4.destroy()
            backButton.destroy()
            programmingChoice()
            
        backButton=Button(root, text="Back",command=back)
        backButton.pack(pady=(40,0))
       
        

    def oop():
            textLabel2.destroy()
            pythonButton.destroy()
            javaButton.destroy()
            seButton.destroy()
            oopButton.destroy()
            cppButton.destroy()
            exitButton.destroy()
            oopQuiz()
            
#for C++
    def cppQuiz():
        questions = [
            "Delaration a pointer more than\n once may cause ____",
            "An expression A.B in C++ means ____",
            "A C++ code line ends with ___",
            "Which one is not a correct \nvariable type in C++?",
            "Which of the following is used \nfor comments in C++?",
            "Which function is used to read \na single character from the console in C++?",
            "Which of the following is called \ninsertion/put to operator?",
            "A language which has the capability \nto generate new data types are called ________________",
            "Which of the following is called \naddress operator?",
            "Which of the following is the correct \nsyntax of including a user defined \nheader files in C++?"
        ]

        answers = [
            ["1. Error","2. Trap","3. Abort","4. Null"],
            ["1. A is member of object B ","2. B is member of Object A","3. Product of 1. and 2.","4. none"],
            ["1. A Semicolon (;)","2. A Fullstop(.)","3. A Comma (,)","4. A Slash (/)"],
            ["1. Float","2. real","3. int","4. double"],
            ["1. // comment","2.  /* comment */","3. both // comment or /* comment */","4.  // comment */"],
            ["1. cin.get(ch)","2. getline(ch)","3. read(ch)","4. scanf(ch)"],
            ["1. <<","2. >>","3. >","4. <"],
            ["1. Extensible","2. Overloaded","3. Encapsulated","4. Reprehensible"],
            ["1. *","2. &","3. _", "4. %"],
            ["1. #include <userdefined.h>","2. #include <userdefined>","3. #include “userdefined”","4. #include [userdefined]"],
        ]
        global realans
        realans = [1,1,0,1,2,0,0,0,1,2]
        
        global userAnswers
        userAnswers = []
        global list
        list = []
        def randomQuesGenerator():
            while(len(list) < 5):
                x=  random.randint(0,9)
                if x in list:
                    continue
                else:
                    list.append(x)
        randomQuesGenerator()

        def showresult(score):
            questionLabel.destroy()
            radioButton1.destroy()
            radioButton2.destroy()
            radioButton3.destroy()
            radioButton4.destroy()
            backButton.destroy()
            
            labelimage=Label(root,background="white")
            labelimage.pack(pady=(60,0))
            labelresulttext=Label(root, font=("Frabklin Gothic", 16, "bold"), background="white")
            labelresulttext.pack(pady=(30,0))
            exitButton=Button(root, text="Exit",font=("Book antiqua", 10,"bold"),border=1,background="red", foreground="white", command=quit)
            exitButton.pack(pady=(20,0))
            if score>=20:
                imgwin = ImageTk.PhotoImage(Image.open("win.png"))
                labelimage.config(image=imgwin)
                labelimage.image=imgwin
                labelresulttext.config(text="CONGRATULATIONS!! You won.")
            else:
                imgwin = ImageTk.PhotoImage(Image.open("lose.png"))
                labelimage.config(image=imgwin)
                labelimage.image=imgwin
                labelresulttext.config(text="SORRY!! Try again.")

        def calc():
            global list,userAnswers,realans
            x = 0
            score = 0
            for i in list:
                if userAnswers[x]==realans[i]:
                    score+=5
                x+=1
            showresult(score)
            
        global ques
        ques = 1
        def selected():
            global ques,userAnswers,radiovar, questionLabel, radioButton1, radioButton2, radioButton3, radioButton4
            x = radiovar.get()
            radiovar.set(-1)
            userAnswers.append(x)
            if ques < 5:
                questionLabel.config(text=questions[list[ques]])
                radioButton1['text'] = answers[list[ques]][0]
                radioButton2['text'] = answers[list[ques]][1]
                radioButton3['text'] = answers[list[ques]][2]
                radioButton4['text'] = answers[list[ques]][3]
                ques += 1
            else:
                calc()

        def startQuiz():
            global questionLabel, radiovar, radioButton1, radioButton2, radioButton3, radioButton4

            questionLabel = Label(root, text=questions[list[0]], font=("Frabklin Gothic", 14), justify="center",background="white",foreground="dark blue")
            questionLabel.pack(pady=(70,0))

            radiovar = IntVar()
            #radiovar.set(-1)

            radioButton1 = Radiobutton(root, text=answers[list[0]][0], background="white", font=("Frabklin Gothic", 14),value=0,variable=radiovar,command=selected)
            radioButton1.pack(pady=(30,0))

            radioButton2 = Radiobutton(root, text = answers[list[0]][1], background="white", font=("Frabklin Gothic", 14),value=1,variable=radiovar,command=selected)
            radioButton2.pack(pady=(20,0))

            radioButton3 = Radiobutton(root, text = answers[list[0]][2], background="white", font=("Frabklin Gothic", 14),value=2,variable=radiovar,command=selected)
            radioButton3.pack(pady=(20,0))

            radioButton4 = Radiobutton(root, text = answers[list[0]][3],background="white", font=("Frabklin Gothic", 14),value=3,variable=radiovar,command=selected)
            radioButton4.pack(pady=(20,0))
        startQuiz()

        def back():

            questionLabel.destroy()
            radioButton1.destroy()
            radioButton2.destroy()
            radioButton3.destroy()
            radioButton4.destroy()
            backButton.destroy()
            programmingChoice()
            
        backButton=Button(root, text="Back",command=back)
        backButton.pack(pady=(40,0))
       
        

    def cpp():
            textLabel2.destroy()
            pythonButton.destroy()
            javaButton.destroy()
            seButton.destroy()
            oopButton.destroy()
            cppButton.destroy()
            exitButton.destroy()
            cppQuiz()
            




    #for second page (where choosing option is provided)
    def programmingChoice():

        global textLabel2
        global pythonButton
        global javaButton
        global seButton
        global oopButton
        global cppButton
        global exitButton
       
        textLabel2=Label(root,text="Choose any, you want to test your knowledge.",font=("Book antiqua", 16,"bold"),background="white")
        textLabel2.pack(pady=(20,0))
        pythonButton=Button(root,text="Python",background="light blue",border=1,pady=5,padx=50,font=("Book antiqua", 20,"bold"),command=python)
        pythonButton.pack(pady=(60,0))
        javaButton=Button(root,text="Java",background="light green",border=1,pady=5,padx=40,font=("Book antiqua", 20,"bold"),command=java)
        javaButton.pack(pady=(20,0))
        seButton=Button(root,text="Software Engineering" ,background="orange",border=1,pady=5,font=("Book antiqua", 20,"bold"),command=se)
        seButton.pack(pady=(20,0))
        oopButton=Button(root,text="OOP" ,background="light green",border=1,pady=5,padx=40,font=("Book antiqua", 20,"bold"),command=oop)
        oopButton.pack(pady=(20,0))
        cppButton=Button(root,text="C/C++" ,background="light blue",border=1,pady=5,padx=50,font=("Book antiqua", 20,"bold"),command=cpp)
        cppButton.pack(pady=(20,0))
        exitButton=Button(root, text="Exit",font=("Book antiqua", 10,"bold"),border=1,background="red", foreground="white", command=quit)
        exitButton.pack(pady=(20,0))
    programmingChoice()

#for main page
img = ImageTk.PhotoImage(Image.open("quiz.png"))
imageLabel=Label(root, image=img, background='white')
imageLabel.pack(pady=(70,0))
textLabel=Label(root, text="Broaden your knowlege.",font=("Book antiqua", 20,"bold"), background ='white')
textLabel.pack(pady=(0,50))

img2 = ImageTk.PhotoImage(Image.open("button.png"))
startButton=Button(root,image=img2,background='white', border=0,command=nextPage)
startButton.pack()
introLabel=Label(root, text="Want to test your knowledge about Programming?\n Test your knowledge here.\n Widen your Horizon.\n Click above 'Let's go >>' to start.",font=("Book antiqua", 12), background="white")
introLabel.pack(pady=(80,0))
instructionLabel=Label(root, text="You will get to choose the level.\n Good Luck!!",background="light blue")
instructionLabel.pack(pady=(30,0))
  
root.mainloop()