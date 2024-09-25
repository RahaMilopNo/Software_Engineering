import time  
from datetime import datetime  

def five_seconds():
    for _ in range(5):  
        current_time = datetime.now().strftime("%H:%M:%S")  
        print(f"Текущее время: {current_time}") 
        time.sleep(1)  

if __name__ == '__main__':  
    five_seconds()  
