class Cars:

    def __init__(self,name,color,year):
        self.name = name
        self.color = color
        self.year = year

    def run(self):
        print("The car is running" + self.name)
    def stop(self):
        print("The car stopped" + self.color + self.name)
        