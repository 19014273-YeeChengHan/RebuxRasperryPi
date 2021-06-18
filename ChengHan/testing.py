
import time

# countdown timer 
def countdown(t):
    while t: # while t > 0 for clarity 
      mins = t // 60
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r") # overwrite previous line 
      time.sleep(1)
      t -= 1
    print('Blast Off!!!')

      
t = input("Enter the time in seconds: ")
    
countdown(int(t))