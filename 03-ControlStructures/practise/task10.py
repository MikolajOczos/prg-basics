dog_years = float(input("How old is the dog in dog years?"))
human_years = 0
if dog_years <= 2:
    human_years = (dog_years*10.5)
else :
    human_years = 21 + (dog_years - 2)*4
    
print(f"The dog has {human_years} human years")

