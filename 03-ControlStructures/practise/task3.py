###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = False # False - switch off, True - switch on
light_switch2 = False
bulbs_on = 0

count = input("Is the first switch on? Y/N?")
count1 = input("Is the second switch on? Y/N?")

if count == 'Y':
    light_switch1 = True
else:
    light_switch1 = False
if count1 == "Y":
    light_switch2 = True
else:
    light_switch2 = False

if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2
print(f"The amount of lit bulbs is {bulbs_on}")