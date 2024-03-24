#4 Встречалось ли число раньше. Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
numbers = input().split()  
seen_numbers = set()       

for num in numbers:
    if num in seen_numbers:
        print("YES")        
    else:
        print("NO")        
        seen_numbers.add(num)  
