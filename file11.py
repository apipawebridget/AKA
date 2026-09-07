# Student Marks Management System

# 1. Initial dictionary - fixed syntax (: not =)
marks = {
    "John": 78,
    "Mary": 92,
    "Peter": 65,
    "Sarah": 85,
    "David": 55
}

print("=== CURRENT MARKS ===")
for name, mark in marks.items():
    print(f"{name}: {mark}")

# 2. Ask user to enter student name and mark, and add new student
print("\n--- Add New Student ---")
new_name = input("Enter new student name: ")
new_mark = int(input(f"Enter mark for {new_name}: "))
marks[new_name] = new_mark
print(f"{new_name} added!")

print("\n=== UPDATED MARKS ===")
for name, mark in marks.items():
    print(f"{name}: {mark}")

# 3. Update the mark of an existing student
print("\n--- Update Student Mark ---")
update_name = input("Enter name of student to update: ")

if update_name in marks:
    updated_mark = int(input(f"Enter new mark for {update_name}: "))
    marks[update_name] = updated_mark
    print(f"{update_name}'s mark updated to {updated_mark}")
else:
    print(f"{update_name} not found!")

print("\n=== AFTER UPDATE ===")
for name, mark in marks.items():
    print(f"{name}: {mark}")

# 4. Remove a student from dictionary
print("\n--- Remove Student ---")
remove_name = input("Enter name of student to remove: ")

if remove_name in marks:
    marks.pop(remove_name)
    print(f"{remove_name} removed!")
else:
    print(f"{remove_name} not found!")

# Final display
print("\n=== FINAL STUDENT MARKS ===")
for name, mark in marks.items():
    print(f"{name}: {mark}")

print(f"\nTotal students: {len(marks)}")

#sets
fruits=set()#empty set
fruits="mangoes","berries","apples"
print(len(fruits))

#
x={2,4,6,8,10}
y={1,2,3,5,7,10}

common_to_sets=x.intersection(y)
print(common_to_sets)

diff=x.difference(y)
print(diff)

union_ses=x.union(y)

sym_diff=x.symmetric_difference(y)
print(sym_diff)

x.intersection_update(y)# modifies the original set
print(x)
x.symmetric_difference(y)
x.difference_update(y)

#is [superst,subseet,intersection]
print(x.isdisjoint(y))
print(x.issubset(y))
print(x.issuperset(y))
a=set(range(1,11))
b=set([x forx in range(1,11)if x%2==0])
print(a.issubset(b))

copied=a.copy()
print(copied)
a.clear()#deletes all elements in a set
print(a)

#assignment
cities=["Mbale", "Gulu", "Mbarara", "Jinja","Mbale"]
#remove duplicates
cities=list(dict.fromkeys(cities))
print(cities)