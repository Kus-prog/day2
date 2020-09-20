#count no of digit

def countdigit(n):
    count=0
    while(n!=0):
     n=n//10
     count=count+1
    return(count)


n=int(input("enter the number:"))
count=countdigit(n)
print("number of digit are:=%d"%count)

