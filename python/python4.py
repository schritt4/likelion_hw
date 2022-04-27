fruit = {}

while True:
    fruit_type = input("Enter a fruit type (q to quit): ")
    
    if fruit_type == "q":
        break
    else:
        fruit_weight = input("Enter the weight in kg: ")
        fruit[fruit_type] = fruit_weight

print(fruit)

    
