import re
s = 1
def inpname():
    name=input("Hi,Enter your name:")#.lower()
    check = re.search("^[a-zA-Z]{3,}$", name)
    #print (check)
    return check,name
check1,name=inpname()

def inpmobile():
    mobile=input("Hi,Enter your mobile number:")#.lower()
    check = re.search("^[6-9][0-9]{9}", mobile)
    #print (check)
    return check,mobile
check2,number=inpmobile()

while(s):
    if (check1!=None and check2!=None):
        print(f" Hi {name},\n Your mobile number is {number}")
        s=0
    else:
        if check1==None:
            print("please Enter your name correctly")
            check1, name = inpname()
        else :
            print("please Enter your mobile number correctly")
            check2, number = inpmobile()
