import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program starts on " + time.ctime())
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open_new('https://www.youtube.com/watch?v=izGwDsrQ1eQ')
    break_count += 1
    
