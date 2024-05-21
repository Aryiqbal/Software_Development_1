#I declare that my work contains no examples of misconduct, such as plagarism.
#Student ID: W1820867
#Date:29/11/2021

Option = " "
Pass = 0
Defer = 0
Fail = 0
Credits = [0,20,40,60,80,100,120]

#Counters
PCount = 0
PMTCount = 0
DNPMRCount = 0
ECount = 0

#Outputs
P = ("Progress")
PMT = ("Progress (module trailer)")
DNPMR = ("Do not Progress - module retriever")
E = ("Exclude")
while Option != "q":
    
#Checks if the users input is valid
    a= True

    while a:
        try:
            Pass=int(input('Enter your total Pass credits:'))
        except ValueError:
            print("integer required")
            continue
        else:
            if Pass not in Credits:
                print("Integer out of range")
            elif Pass in Credits:
                break

    while a:
        try:
            Defer=int(input("Enter your total Defer credits?"))
        except ValueError:
                print("integer is required")
                continue
        else:
           if Defer not in Credits:
               print("integer out of range")
           elif Defer in Credits:
                break
       
    while a:
        try:
            Fail=int(input("Enter your total Fail credits: "))
        except ValueError:
            print("integer is required")
            continue
        else:
            if Fail not in Credits:
                print("integer out of range")
            elif Fail in Credits:
                break
            
#Checks if the total is equal to 120
    total = Pass + Defer + Fail
    if total != 120:
        print("Total incorrect")
        
#Checks the grades and predicts total grade
    if Pass == 120 and Defer == 0 and Fail == 0:
        print(P)
        PCount = PCount + 1
    elif Pass == 100 and Defer == 20 and Fail == 0:
        print(PMT)
        PMTCount = PMTCount + 1
    elif Pass == 100 and Defer == 0 and Fail == 20:
        print(PMT)
        PMTCount = PMTCount + 1
    elif Pass == 80 and Defer == 40 and Fail == 0:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 80 and Defer == 20 and Fail == 20:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 80 and Defer == 0 and Fail == 40:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 60 and Defer == 60 and Fail == 0:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 60 and Defer == 40 and Fail == 20:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 60 and Defer == 20 and Fail == 40:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 60 and Defer == 0 and Fail == 60:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 40 and Defer == 80 and Fail == 0:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 40 and Defer == 60 and Fail == 20:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 40 and Defer == 40 and Fail == 40:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 40 and Defer == 20 and Fail == 60:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 40 and Defer == 0 and Fail == 80:
        print(E)
        ECount = ECount + 1
    elif Pass == 20 and Defer == 100 and Fail == 0:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 20 and Defer == 80 and Fail == 20:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 20 and Defer == 60 and Fail == 40:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 20 and Defer == 40 and Fail == 60:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 20 and Defer == 20 and Fail == 80:
        print(E)
        ECount = ECount + 1
    elif Pass == 20 and Defer == 0 and Fail == 100:
        print(E)
        ECount = ECount + 1
    elif Pass == 0 and Defer == 120 and Fail == 0:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 0 and Defer == 100 and Fail == 20:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 0 and Defer == 80 and Fail == 40:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 00 and Defer == 60 and Fail == 60:
        print(DNPMR)
        DNPMRCount = DNPMRCount + 1
    elif Pass == 0 and Defer == 40 and Fail == 80:
        print(E)
        ECount = ECount + 1
    elif Pass == 0 and Defer == 20 and Fail == 100:
        print(E)
        ECount = ECount + 1
    elif Pass == 0 and Defer == 0 and Fail == 120:
        print(E)
        ECount = ECount + 1
        
#options for the user to carry on/quit & histogram
    loop_condition= str(input("Plese enter 'y' for yes or 'q' to quit and view results? "))
    while (loop_condition != "y" or loop_condition != "q"):

        if loop_condition =='y':
           break
       
        elif loop_condition =='q':
            totalCount = PCount + ECount + PMTCount + DNPMRCount
            print("_" *50)
            print("Horizontal Histogram")
            print("Progress" , PCount, "  :", "*" * PCount)
            print("Trailer", PMTCount, "   :", "*" * PMTCount)
            print("Retriever", DNPMRCount, "   :" , "*" * DNPMRCount)
            print("Excluded", ECount, "   :", "*" * ECount)
            print("")
            print (totalCount, "outcomes in total")
            print("-"*50)
            quit()

        else:
            continue
        

