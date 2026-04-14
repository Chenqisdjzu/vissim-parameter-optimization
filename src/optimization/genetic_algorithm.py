import random
import numpy as np

class Individual:
    def __init__(self, chromosome_length):
        self.chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
        self.fitness = 0

    def evaluate(self, fitness_function):
        self.fitness = fitness_function(self.chromosome)

def tournament_selection(population, tournament_size=3):
    selected = random.sample(population, tournament_size)
    selected.sort(key=lambda ind: ind.fitness, reverse=True)
    return selected[0]

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1.chromosome) - 1)
    child1 = Individual(len(parent1.chromosome))
    child2 = Individual(len(parent2.chromosome))
    child1.chromosome = parent1.chromosome[:point] + parent2.chromosome[point:]
    child2.chromosome = parent2.chromosome[:point] + parent1.chromosome[point:]
    return child1, child2

def mutate(individual, mutation_rate):
    for i in range(len(individual.chromosome)):
        if random.random() < mutation_rate:
            individual.chromosome[i] = 1 - individual.chromosome[i]

def genetic_algorithm(population_size, chromosome_length, fitness_function, generations, mutation_rate):
    population = [Individual(chromosome_length) for _ in range(population_size)]
    for gen in range(generations):
        for ind in population:
            ind.evaluate(fitness_function)
        next_generation = []
        while len(next_generation) < population_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            next_generation.append(child1)
            next_generation.append(child2)
        population = next_generation[:population_size]
    return max(population, key=lambda ind: ind.fitness)

# Example fitness function
def sample_fitness_function(chromosome):
    # Example: maximizing the number of 1s in the chromosome
    return sum(chromosome)

# Example usage
if __name__ == '__main__':
    best_individual = genetic_algorithm(population_size=100, chromosome_length=10, fitness_function=sample_fitness_function, generations=50, mutation_rate=0.01)
    print('Best individual:', best_individual.chromosome)
    print('Best fitness:', best_individual.fitness)