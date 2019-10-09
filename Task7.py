def median ():
    print("Enter the values to find the median-")
    a=int(input("Value 1 "))
    b=int(input("Value 2 "))
    c=int(input("Value 3 "))
    if a>b:
        if a<c:
            m=a
        elif b>c:
            m=b
        else:
            m=c     
    else:
        if  a>c:
            m=a
        elif b<c:
            m=b
        else:
            m=c                      
    print("The median is ",m)         

median()
