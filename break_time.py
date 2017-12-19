import webbrowser
import time

'''This program creates a browser to open to indicate that it is time
to take a break from the computer. I used the time and webbrowser module which
was imported from the python built in standard library.
'''

total_breaks = 3
break_count = 0

print("This program started at "+time.ctime())


while break_count < total_breaks:
    time.sleep(10)
    webbrowser.open("https://youtu.be/7BHu5Ongqow")
    break_count += 1
    


