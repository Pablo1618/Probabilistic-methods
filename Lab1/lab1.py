import pandas as pd
#from itertools import permutations
import math

df = pd.read_csv('miasta.csv', sep='\s+')
print(df)

def distance(city1, city2, df):
    lat1, lon1 = df[df['Town'] == city1][['Latitude', 'Longitude']].values[0]
    lat2, lon2 = df[df['Town'] == city2][['Latitude', 'Longitude']].values[0]

    dx = lon2 - lon1
    dy = lat2 - lat1
    return math.sqrt(dx ** 2 + dy ** 2)

def citiesPermutations(lst, r):
    if r == 0:
        return [[]]
    else:
        permutations_list = []
        for i in range(len(lst)):
            for perm in citiesPermutations(lst[:i] + lst[i+1:], r-1):
                permutations_list.append([lst[i]] + perm)
        return permutations_list
    
def citiesCombinations(lst, r):
    if r == 0:
        return [[]]
    else:
        combinations_list = []
        for i in range(len(lst)):
            for comb in citiesCombinations(lst[i+1:], r-1):
                combinations_list.append([lst[i]] + comb)
        return combinations_list

def printRoad(lst):
    roadString = []
    for i in range(len(lst)):
        if i > 0:
            roadString.append(lst[i])
        else:
            roadString.append(lst[0])
    print(' => '.join(map(str, roadString)))

def calculateRoadLength(lst):
    roadLength = 0
    for i in range(1, len(lst)):
        roadLength += distance(lst[i-1], lst[i], df)
    return roadLength

def sumCitiesPopulation(lst):
    population = 0
    for i in range(0, len(lst)):
        population += df[df['Town'] == lst[i]]['Population'].values[0]
    return population

#citiesNames = df['Town'].tolist()[len(df)//7:]
citiesNames = df['Town'].tolist()[-4:]


# Określenie liczby miast do odwiedzenia
n = len(citiesNames)

# Wygenerowanie wszystkich permutacji
N = 4
permutations = citiesPermutations(citiesNames, N)
combinations = citiesCombinations(citiesNames, N)
permutationsAmount = 0


permutationRoadLengths = {}
for permutation in permutations:
    permutationsAmount+=1
    printRoad(permutation)
    road_length = calculateRoadLength(permutation)
    permutationRoadLengths[tuple(permutation)] = road_length
    print('{:.2f}'.format(road_length))
print(permutationsAmount)

for combination in combinations:
    print("Combination:", combination)
    shortestRoadLength = 99999
    shortestRoad = []
    for permutation in permutations:
        permutationRoadLength = permutationRoadLengths[tuple(permutation)]
        if all(city in permutation for city in combination) and permutationRoadLength< shortestRoadLength:
            shortestRoadLength = permutationRoadLength
            shortestRoad = permutation
            #print("   Permutation:", permutation)
    print("Shorest road: " + str(shortestRoad))
    print("Length: " + str(shortestRoadLength))



# Podzbiory K z N miast
# combinations = citiesCombinations(citiesNames, 3)
# bestCombination = None
# bestCombinationPopulation = 0
# fiftyPercentPopulation = sumCitiesPopulation(citiesNames) // 2
# for combination in combinations:
#     print(combination)
#     populationSum = sumCitiesPopulation(combination)
#     if(abs(populationSum - fiftyPercentPopulation) < abs(bestCombinationPopulation - fiftyPercentPopulation)):
#         bestCombinationPopulation = populationSum
#         bestCombination = combination

# print("-----------------------------------")
# print("50 percent of population: " + str(fiftyPercentPopulation))
# print("Best fit combination: " + str(bestCombination))
# print("Population of this combination: " + str(bestCombinationPopulation))