import numpy as np
import matplotlib.pyplot as plt

def convert_text(text):
    processed_text = text

    vocal = ['a', 'e', 'i', 'o', 'u', 'n']
    acentos = ['á', 'é', 'í', 'ó', 'ú', 'ñ']

    characteres = [',', '.', '!', '¡', '¿', '?', '-', ':', ';', '—', '»', '«', '(', ')']

    for char in characteres:
        processed_text = processed_text.replace(char, '')

    for i in range(len(acentos)):
        processed_text = processed_text.replace(acentos[i], vocal[i])

    processed_text = processed_text.replace("\n"," ")
    processed_text = processed_text.replace(" ","")
    processed_text = processed_text.upper()

    return processed_text

def process(path):
    file = open(path, 'r', encoding='utf-8')
    text = file.read()

    return convert_text(text)

def displacements(text, n):
    moved_texts = []
    len_text = len(text)

    for i in range(n):
        moved_text = []
        for j in range(len_text):
            moved_text.append(text[(i + j) % len_text])
        moved_texts.append(moved_text)

    moved_texts = np.array(moved_texts)
    return moved_texts

def matches(text, n):
    displacement = displacements(text, n)
    match = np.zeros(len(text), dtype=int)

    for i in range(len(text)):
        column = displacement[:, i]
        cunique, counts = np.unique(column, return_counts=True)
        match[i] = np.max(counts)
    return max(match)

def visualize(n_generations, fitness_evolution, average_fitness_evolution, key_length_evolution):
    _, axs = plt.subplots(1, 3, figsize=(15, 5))

    axs[0].plot(range(n_generations), fitness_evolution)
    axs[0].set_ylabel('Fitness')
    axs[0].set_title('Fitness evolution')

    axs[1].plot(range(n_generations), average_fitness_evolution)
    axs[1].set_ylabel('Fitness')
    axs[1].set_title('Mean fitness evolution')

    axs[2].plot(range(n_generations), key_length_evolution)
    axs[2].set_ylabel('Length')
    axs[2].set_title('Mean key lenght evolution')

    for ax in axs.flat:
        ax.set(xlabel='generation')
        ax.grid(True)

    plt.tight_layout()
    plt.show()