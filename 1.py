#2 Количество совпадающих чисел. Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
def func1(l1,l2): return len(set(l1).intersection(set(l2)))

l1 = input().split()
l2 = input().split()
print(func1(l1,l2))
