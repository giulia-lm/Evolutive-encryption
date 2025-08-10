import numpy as np
import random
import string
import copy

from vigenere import Vigenere
from utils import matches

class GeneticAlgorithm:
    def __init__(self, text, population_size, n_generations):
        self.population_size = population_size
        self.n_generations = n_generations
        self.population = []
        self.text = text

    def initialize_population(self):
        for i in range(self.population_size):
            rndlen = random.randint(2, len(self.text)//3)

            key = ''.join([random.choice(string.ascii_uppercase) for _ in range(rndlen)])
            keyndividual = Vigenere(self.text, key)
            self.population.append(keyndividual)

    def singlepoint_crossover(self, parent1, parent2):
        minparent = min(len(parent1.key), len(parent2.key))
        point = random.randint(0, minparent )

        key1 = parent1.key[:point] + parent2.key[point:]
        key2 = parent2.key[:point] + parent1.key[point:]

        child1 = Vigenere(self.text, key1)
        child2 = Vigenere(self.text, key2)

        return child1, child2

    def tournament_selection(self, fitness_values):
        tournament = random.sample(range(len(self.population)), k=10)
        tournament_fitness_values = [fitness_values[i] for i in tournament]
        winner_local_index = np.argmin(tournament_fitness_values)

        winner_index = tournament[winner_local_index]
        return winner_index

    def swap_mutation(self, individual):
        mutated = copy.deepcopy(individual)
        index1 = random.randint(0,len(mutated.key) - 1)
        index2 = random.randint(0,len(mutated.key) - 1)

        mutated.key = list(mutated.key)
        mutated.key[index2], mutated.key[index1] = mutated.key[index1], mutated.key[index2]
        mutated.key = ''.join(mutated.key)

        return mutated

    def run(self):
        self.initialize_population()
        n_displacements = len(self.text) // 3
        best_solution_value = float('inf')
        best_solution = None
        fitness_evolution = []
        average_fitness_evolution = []
        key_length_evolution = []

        for i in range(self.n_generations):
            print(f'Current generation: {i}')
            fitness_values = [matches(individual.ciphertext, n_displacements) for individual in self.population]
            current_best_index = np.argmin(fitness_values)
            current_best_fitness = fitness_values[current_best_index]
            current_best_solution = self.population[current_best_index]

            if current_best_fitness < best_solution_value:
                best_solution_value = current_best_fitness
                best_solution = current_best_solution

            new_population = []
            for _ in range(self.population_size // 2):
                parent1 = self.population[self.tournament_selection(fitness_values)]
                parent2 = self.population[self.tournament_selection(fitness_values)]
                child1, child2 = self.singlepoint_crossover(parent1, parent2)
                child1 = self.swap_mutation(child1)
                child2 = self.swap_mutation(child2)
                new_population.extend([child1, child2])

            self.population = new_population

            # compute mean fitness
            average_fitness = np.mean(fitness_values)
            fitness_evolution.append(current_best_fitness)
            average_fitness_evolution.append(average_fitness)
            key_length_evolution.append(np.mean([len(individual.key) for individual in self.population]))

            print('------------------------')
            print("Best key:", best_solution.key)
            print("Cipher text by the key:", best_solution.ciphertext)
            print("Best key fitness:", best_solution_value)
            print("Best key length:", len(best_solution.key))

        return fitness_evolution, average_fitness_evolution, key_length_evolution