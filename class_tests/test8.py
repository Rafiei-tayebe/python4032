a = int(input()) # 369121517
days = a // (24*60*60) 
a = a % (24*60*60) 
hours = a // (60*60)
a= a % (60*60)
minutes = a // 60
seconds = a % 60

print(days, "days", hours, "hours", minutes, "minutes", seconds, "seconds" )
