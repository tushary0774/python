num=[18,19,2,20,13,41,20,90]
print("The numbers are \t",num)
x=0
odd=0
even=0
for x in num:  
    if x % 2==0:
        even=even+1
    else:
        odd=odd+1
    x+=1   

print("Odd Numbers are:",odd)
print("Even numbers are",even)
a=input("Enter any key to exit")
