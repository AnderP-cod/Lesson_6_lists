print("given_list = [False, 0, 'str', '123', 'hello', '%', 1.2, 1] вивести тип кожного значення через while")

given_list = [False, 0, 'str', '123', 'hello', '%', 1.2, 1]

while True:
    print(type(given_list[0]))
    print(type(given_list[1]))
    print(type(given_list[2]))
    print(type(given_list[3]))
    print(type(given_list[4]))
    print(type(given_list[5]))
    print(type(given_list[6]))
    print(type(given_list[7]))
    break

print()
print()
print("4 створити 2 списка вивести на екран: найбільше та найменше число кожного списка спільні значення з двох списків")

list1 = [1 , 5 , 2]
list2 = [5 , 32.32 , 3]
print(list1,"\n",list2)
print(max(list1), min(list1))
print(max(list2), min(list2))


print()
print()

print("2 Повернути суму чисел усіх елементів списку")


list3 = [1 , 5 , 2]
list4 = [5 , 3]
print(list3,"\n",list4)
print(sum(list3) , sum(list4))
