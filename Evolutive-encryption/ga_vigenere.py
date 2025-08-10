from utils import process, visualize
from GA import GeneticAlgorithm

text = process("test-files/mobydick.txt")
population_size = 20
n_generations = 3


ga = GeneticAlgorithm(text, population_size, n_generations)
ga.initialize_population()
fitness_evolution, average_fitness_evolution, key_length_evolution = ga.run()

visualize(n_generations, fitness_evolution, average_fitness_evolution, key_length_evolution)