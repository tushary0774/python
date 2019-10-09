class rectangle:
    def __init__(self,length,breadth):
        self.length= length
        self.breadth= breadth

    def area(self):
        self.ans= int(self.length)*int(self.breadth)
        print("The area is: ",self.ans)


a=input("Enter the length ")
b=input("Enter the breadth ")
rec_1 = rectangle(a,b)

rec_1.area()
e=input("Enter any key to exit")
