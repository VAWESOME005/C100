class HeightPredictor(object):
    def __init__(self, name, age, dadHeight, momHeight):
        self.name = name
        self.age = age
        self.dadHeight = dadHeight
        self.momHeight = momHeight
    
    def heightCalc(self):
        beforeAverage = self.dadHeight + self.momHeight 
        Average = beforeAverage/2
        print("Your predicted height is... ", Average)

Vishesh = HeightPredictor("Vishesh", 13, 72, 62)
Vishesh.heightCalc()
