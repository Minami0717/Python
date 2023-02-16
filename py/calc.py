class Calculator:
    def __init__(self,n = []):
        self.n = n
        
    def sum(self):
        result = 0
        for i in self.n:
            result += i
        return result

    def avg(self):
        result = 0
        for i in self.n:
            result += i
        return result / len(self.n)
