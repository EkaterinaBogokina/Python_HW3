# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
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

next_number = A_list[0]
for i in A_list:
    if abs(i - x) < abs(next_number- x):
        next_number = i
print ("ближайшее число", next_number)
