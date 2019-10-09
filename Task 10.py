class rectangle:
    def __init__(self,length,breadth):
        self.length= length
        self.breadth= breadth

    def area(self):
        self.ans= int(self.length)*int(self.breadth)
        print("The area is: ",self.ans)


rec_1 = rectangle(5,5)

rec_1.area()