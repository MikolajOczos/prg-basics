avg_speed = lambda distance,hours,minutes: distance/ ((minutes*(1/60))+hours)
distance = float(input("distance?"))
hours = float(input("Hours?"))

minutes = float(input("Minutes"))
dd=avg_speed(distance,hours,minutes)
print(dd)
