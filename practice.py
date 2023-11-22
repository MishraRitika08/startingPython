def grade(m):
    if(m>80 and m<=100):
        print("Outstanding")
    elif(m>60 and m<=80):
        print("Good")
    elif(m>=40 and m<=60):
        print("average")
    else:
        print("Fail")


res = grade(6)
print(res) 
