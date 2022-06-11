#código de ordenação ensinado na aula da UNIVESP
#método Bubble Sort
#percorre várias vezes o conjunto
#compara o sucessor v[i} com v[i+1] se estiverem em lugar errado serão trocados e assim sucesivamente
#processo se repete n-1 vezes até que seja alcançada a devida ordenação

def bubble_sort(v):
  for i in range(len(v) - 1):
    for j in range(len(v) - i - 1):
      if (v[j] > [j+1]):
        v[j], v[j+1] = v[j+1], v[j]
    