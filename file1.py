def greet(name):
    print("welcome to VU", name )
greet("Ken") 
greet("Pal")

#grading application
score=int(input("enter score:" ))
if score>= 90:
    print("grade A")
elif score >=80:
    print("grade B")   
elif score >= 70:
    print("grade C")    
elif score >=60:
    print("grade D")    
else:
    print("grade F")

    #lists an their methods
names= ["pal","odongo", "Saka","Geofrey","Tricia"]
names.pop(2)
print(names)
names.pop(3)
print(names)

#length of names
names_length=[len(names)for names in names]
print(names_length)

#list comprehension
names_upper=[names.upper()for names in names]
print(names_upper)

#[true,false]based on length of character of each name
for names in names:
    if len (names)%2==0:
        print(True)
    else:
        print(False)

