seconds = int(input("Please enter the number of seconds:"))

hours = seconds // 3600 # 3600 seconds = 1 hours
seconds = seconds % 3600
minutes = seconds // 60 # 60 seconds = 1 minute
seconds = seconds % 60
print(hours, ":", sep="", end="")
tens = minutes // 10
ones = minutes % 10
print(tens, ones, ":", sep="", end="")
tens = seconds // 10
ones = seconds % 10
print(tens, ones, sep ="")