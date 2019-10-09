while(1):
    
    ans=input("Do you want to  (1/2):\n1.Multiply\t2.Exit ")
    if ans=="1": 
        m= ['a','b','c','d']
        print("Enter the four numbers that you want to multiply \n ---------------------------------------")
        m[0]=int(input("Enter the first number "))
        m[1]=int(input("Enter the second number "))
        m[2]=int(input("Enter the third number "))
        m[3]=int(input("Enter the fourth number "))
        mul= m[0]*m[1]*m[2]*m[3]
        print("---------------------------------------")
        print("The product of the input given is :",mul)
        
    elif ans!="1":
        import os
        exit (0)
    

