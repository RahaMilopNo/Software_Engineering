import math  

def heron_area(a, b, c):
    s = (a + b + c) / 2  
    area = math.sqrt(s * (s - a) * (s - b) * (s - c)) 
    return area  
