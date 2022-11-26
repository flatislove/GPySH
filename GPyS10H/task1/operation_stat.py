class MinStat:
    numbers:list
    min_value:int

    def __init__(self):
        self.numbers=[]
        self.min_value=0
    
    def add_number(self,nums):
        self.numbers.append(nums)

    def calculate(self):
        if len(self.numbers)>0:
            min=self.numbers[0]
            for value in self.numbers:
                if value<min: min=value
            self.min_value=min
        else: self.min_value=None
    
    def result(self):
        self.calculate()
        return self.min_value

class MaxStat:
    numbers:list
    max_value:int

    def __init__(self):
        self.numbers=[]
        self.max_value=0
    
    def add_number(self,nums):
        self.numbers.append(nums)

    def calculate(self):
        if len(self.numbers)>0:
            max=self.numbers[0]
            for value in self.numbers:
                if value>max: max=value
            self.max_value=max
        else: self.max_value=None
    
    def result(self):
        self.calculate()
        return self.max_value

class AverageStat:
    numbers:list
    average_value:float

    def __init__(self):
        self.numbers=[]
        self.average_value=0
    
    def add_number(self,nums):
        self.numbers.append(nums)
    
    def calculate(self):
        if len(self.numbers)>0:
            sum=0
            for i in self.numbers:
                sum+=i
            self.average_value=sum/len(self.numbers)
        else: self.average_value=None

    def result(self):
        self.calculate()
        return self.average_value