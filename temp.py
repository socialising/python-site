#class to..
class Temperature:
    def __init__(self,fahrenheit,celsius):
       self.Fahrenheit=fahrenheit
       self.celsius=celsius
    def convert_fahrenheit(self):
        return (self.Fahrenheit-32)*5/9
    def convert_celsius(self):
        return (self.celsius*5/9)+32
T=Temperature(45,34)
print(T.convert_fahrenheit()) 
print(T.convert_celsius())     