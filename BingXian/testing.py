




import time

def countdowntimer(seconds):
    while seconds != 0:
       mins = seconds // 60
       secs = seconds % 60
       timer = '{:02d}:{:02d}'.format(mins, secs)
       print(timer) 
       time.sleep(1)
       seconds -= 1
       return seconds
      
x = input("Enter the time in seconds: ")

    
countdowntimer(int(x))


