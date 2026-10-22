import matplotlib.pyplot as plt

# Dados de exemplo (substitua pelos seus dados reais)
tamanhos = ['Pequeno', 'Médio', 'Grande']
tempos_bubble_sort = [0.1, 0.3, 0.7]  # Substitua pelos seus tempos
tempos_selection_sort = [0.2, 0.4, 0.6]
tempos_insertion_sort = [0.15, 0.35, 0.55]
tempos_quick_sort = [0.05, 0.25, 0.5]
tempos_merge_sort = [0.08, 0.28, 0.48]

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(tamanhos, tempos_bubble_sort, label='Bubble Sort', marker='o')
plt.plot(tamanhos, tempos_selection_sort, label='Selection Sort', marker='o')
plt.plot(tamanhos, tempos_insertion_sort, label='Insertion Sort', marker='o')
plt.plot(tamanhos, tempos_quick_sort, label='Quick Sort', marker='o')
plt.plot(tamanhos, tempos_merge_sort, label='Merge Sort', marker='o')

# Adicionando título e rótulos
plt.title('Comparação do Tempo de Execução dos Algoritmos de Ordenação')
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Tempo de Execução (segundos)')

# Adicionando legenda
plt.legend()

# Mostrando o gráfico
plt.show()
