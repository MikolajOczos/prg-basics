###
# Reads from file, line by line
i = 1
with open('countries.txt', 'r') as file:
    for line in file:
        print(i,line, end="")
        i = i + 1
        