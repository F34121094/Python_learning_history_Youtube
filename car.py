class Car:
    def __init__(self,make,model,year,color):#使用class時，給他四個參數
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):    #這裡的是行為方法
        print("This "+self.model+" is driving")
    def stop(self):
        print("This "+self.model+" is stop")