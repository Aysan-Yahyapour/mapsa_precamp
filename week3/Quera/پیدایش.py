import random
def find(num1, num2, num3):
    
    # min_number = min(sorted_numbers)
    i = 1
    while i <= 4:
        sorted_numbers = sorted(num1, num2, num3)
        if i not in sorted_numbers:
            i += 1
    print(i)

find(1, 2, 3)

