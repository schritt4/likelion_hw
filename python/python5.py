import random
import time

print("5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메뉴를 추천해드려요.")
print("동일한 메뉴는 안돼요!")
print("")

total_num = 0
food_list = []

while total_num < 5:
    food = input("메뉴 추가: ")


    for i in range(total_num):
        if food == food_list[i]:
            print("이미 있는 메뉴예요! 다른 메뉴를 입력해주세요.")
            del food_list[i]
            food_list.append(food)
            print("현재 메뉴 수 =", total_num)
            print("")
            break
        else:
            pass

    if food not in food_list:
        food_list.append(food)
        total_num += 1
        print("현재 메뉴 수 =", total_num)
        print("")
    else:
        continue
      

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("")

print(food_list)
print("과연 오늘의 메뉴는?")
print("")

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("")

random_food = random.choice(food_list)
index_food = food_list.index(random_food)
print("오늘의 메뉴는 %d 번째 메뉴, %s 입니다."%(index_food+1, random_food))