list_anything = []

while True:
    answer = input("Enter anything: ")
    if answer == "q":
        break
    else:
        list_anything.append(answer)

print(list_anything)