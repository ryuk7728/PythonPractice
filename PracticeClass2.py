class House:
    
    name=None
    area=None
    bhk=None

    def __init__(self,name,area,bhk):
        self.name=name
        self.area=area
        self.bhk=bhk

    def live(self):
        print("You are living in",self.name)
    
    def exit(self):
        print("You are exiting",self.name)
        