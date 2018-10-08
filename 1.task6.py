#print ("enter marks")
marks = int(input("enter marks"))
if (marks<25):
    print("f")
elif (marks>=25)& (marks<45):
    print("e")
elif (marks>=45)& (marks<50):
    print("d")
elif (marks>=50)& (marks<60):
    print("c")
elif (marks>=60)& (marks<80):
    print("b")
else:
    print("a")