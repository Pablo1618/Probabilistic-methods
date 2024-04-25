import pandas as pd
import math
import random
import time

# def multiplicative_generator(a, c, m, n, seed):
#     numbers = []
#     x = int(seed + time.time())
    
#     for _ in range(n):
#         x = (a * x + c) % m
#         numbers.append(x) 

#     return numbers

# a = 69069
# c = 1
# m = 2**32 
# n = 10000


# def shift_register_generator(p, q, n, seed):

#     register = [0,1,0,1,1,0,1]
#     numbers = []
#     #seed = int(seed + time.time()) #int(time.time())
#     #register = [int(x) for x in bin(seed)[2:]]

#     for _ in range(n):
#         new_bit = register[-p] ^ register[-q]
#         numbers.append(new_bit)
#         register.append(new_bit)
#         register.pop(0)

#     return numbers

def shift_register_generator(p, q, n, seed, m):
    register = [1,1,0,1,0,1,0]
    numbers = []
    #seed = int(seed + time.time()) #int(time.time())
    #register = [int(x) for x in bin(seed)[2:]]

    for _ in range(n * 32): # Generowanie n * 32 bitów
        new_bit = register[-p] ^ register[-q]
        numbers.append(new_bit)
        register.append(new_bit)
        register.pop(0)

    # Konwersja sekwencji bitów na 32-bitowe liczby całkowite
    int_numbers = []
    for i in range(0, len(numbers), 32): # Przetwarzanie n liczb całkowitych
        binary_chunk = ''.join(map(str, numbers[i:i+32]))
        int_number = int(binary_chunk, 2)
        int_numbers.append(int_number % m)

    return int_numbers[:n] # Zwraca n pierwszych liczb całkowitych

p = 3
q = 7
n = 100000
m = 2**32

def show_distribution(numbers, sectors, max_number):
    sector_difference = max_number // sectors
    distribution = [0]*sectors

    for number in numbers:
        if number < max_number:
            index = number // sector_difference
            distribution[index] += 1

    for i in range(sectors):
        left = sector_difference * i
        right = sector_difference * i + sector_difference
        print(f"Liczba liczb w przedziale {left} - {right}: {distribution[i]}")



#numbers = multiplicative_generator(a, c, m, n, 8484)
numbers = shift_register_generator(p, q, n, 2394, m)

print(numbers)

mean = sum(numbers) / len(numbers)
print("Srednia: ", mean)

show_distribution(numbers, 10, m)

#variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
#print("Wariancja: ", variance)



# def isPointInCircle(x,y, xO,yO, R):
#     distance_squared = (x - xO)**2 + (y - yO)**2
#     if distance_squared <= R**2:
#         return True
#     else:
#         return False

# x1, y1, R1 = 0, 0, 1
# x2, y2, R2 = 1, 0, 1

# num_samples = 10000
# count = 0
# x = [2 * num - 1 for num in multiplicative_generator(a, c, m, num_samples, 9761)]
# y = [2 * num - 1 for num in multiplicative_generator(a, c, m, num_samples, 5896)]

# for i in range(num_samples):
    
#     if isPointInCircle(x[i], y[i], x1, y1, R1) and isPointInCircle(x[i], y[i], x2, y2, R2):
#         count += 1

# ratio = count / num_samples
# common_area = ratio / 0.785 * math.pi
# print(count)
# print(ratio)
# print(common_area)



#wyznaczyc prawdopodobienstwa, ze wypadnie sekwencja K orlow dla zadanych N,K np. N=20, K=5
# def didSequenceHappen(sequence, K):
#     found = 0
#     for i in range(len(sequence)):
#         if(sequence[i]==1):
#             found += 1
#             if(found==K):
#                 return True
#         else:
#             found = 0
#     return False

# N = 20
# K = 4
# num_simulations = 10000

# p = 3
# q = 7
# sequence_length = N
# total_occurrences = 0

# for seed in range(num_simulations):
#     sequence = shift_register_generator(p, q, sequence_length, seed)
#     if(didSequenceHappen(sequence, K) == True):
#         total_occurrences += 1

# probability = total_occurrences / num_simulations

# print(f"Prawdopodobieństwo wypadnięcia sekwencji {K} orłów w ciągu {N} rzutów monetą: {probability}")