month=input("Enter the month you want in days(January,February,March,April,May,June,July,August,September,October,November,December) : \n")
Odd= "January"

if month=="February":
    print("The month of ",month," has 28/29 days\n")
elif month in("January" , "March","May","July","August","October","December"):
    print("The month of ",month," has 31 days\n")    
elif month in("April","June","September","November"):
    print("The month of ",month," has 30 days\n")
else:
    print("Please Enter A Valid Month")
exit=input("Enter Any Key to exit ")    

   