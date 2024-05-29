class Car:
    name=None
    maxSpeed=None
    year=None
    
    def __init__(self,name,maxSpeed,year):
        self.name=name
        self.maxSpeed=maxSpeed
        self.year=year
    
    def drive(self):
        print("The "+self.name+" is driving")
    
    def stop(self):
        print("The "+self.name+" is stopping")
