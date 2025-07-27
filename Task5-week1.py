# Create a program that converts a given time in seconds to hours, minutes, and seconds.
time=eval(input("Enter time: "))
hours= time // 3600
rem=time % 3600
min=rem // 60 
sec=rem % 60

print (f"Time is {hours} hrs {min} m {sec} s")
