print("Enter the 3 sides of the triangle")
sidea=input("Enter side 1 ")
sideb=input("Enter side 2 ")
sidec=input("Enter side 3 ")
print("-----------------------------------------------------------")

if sidea==sideb==sidec:
     print("The triangle is equilateral")
elif sidea==sideb!=sidec:
     print("The triangle is isosceles ")     
elif sideb==sidec!=sidea:
     print("The triangle is isosceles ")     
elif sidea==sidec!=sideb:    
     print("The triangle is isosceles ")        
else:
    print("The triangle is scalene")


