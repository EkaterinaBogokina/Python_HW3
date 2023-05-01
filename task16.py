# Задача 16: Требуется вычислить, 
# сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

n = int (input("enter number of elements: "))
A_list = []
for i in range (1,n+1):
    A_list.append(i)
print (A_list)
x= int (input ("enter number "))
count_x = 0
for i in A_list:
    if x == i:
        count_x+=1
print (count_x)

