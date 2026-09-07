largest= None
smallest= None 
total=0
even_count=0
odd_count=0
for i in range(10):
    num=int(input(f"enter number{i+1}:"))
    total=total+num
    if largest is None:
        largest=num
        smallest=num
    else:
        if num>largest:
            largest=num
            smallest=num
        else:
            if num>largest:
                largest=num
            if num< smallest:
                smallest=num    

    if num % 2 == 0: 
        even_count+=1 
    else:
        odd_count += 1
average = total/10
print("\n---result---")   
print(f"largest number: {largest}")   
print(f"smallest number:{smallest}")  
print(f"sum of all numbers: {total}")
print(f"average:{average}")
print(f"even numbers: {even_count}") 
print(f"odd numbers: {odd_count}")            