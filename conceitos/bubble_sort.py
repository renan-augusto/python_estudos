#código de ordenação ensinado na aula da UNIVESP
#método Bubble Sort
#percorre várias vezes o conjunto
#compara o sucessor v[i} com v[i+1] se estiverem em lugar errado serão trocados e assim sucesivamente
#processo se repete n-1 vezes até que seja alcançada a devida ordenação
import random

def bubble_sort(v): 
    n = len(v) 
    for i in range(n): 
        for j in range(n - i - 1): 
            if v[j] > v[j + 1]: 
                v[j], v[j + 1] = v[j + 1], v[j]
l = random.sample(range(100), 20)
print(l)
print(l(type))
ordered_list = bubble_sort(l)
print(ordered_list)