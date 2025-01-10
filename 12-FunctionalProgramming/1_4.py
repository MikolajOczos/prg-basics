people = ["SMITH Lucy", "JONES Janet", "LEE Jerry", "JACKSON Peter", 
          "JOHNSON Rick", "LEWIS Terry", "CLARKE Robin"]
list_of_people = ""
filltuh = lambda people:  people.startswith("J")
xd=list(filter(filltuh,people))
print(xd)


