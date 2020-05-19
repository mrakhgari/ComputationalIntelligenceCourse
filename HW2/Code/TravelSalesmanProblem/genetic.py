import random
from Fittness import Fitness
import operator


class genetic:
    def __init__(self, cities):
        self.cities = cities

    # create a random path.
    def create_path(self):
        return random.sample(self.cities, len(self.cities))

    # initial population in first time.
    def initial_population(self, population_size):
        population = []
        for _ in range(population_size):
            population.append(self.create_path())
        return population

    def next_generation(self, current_population, elite_size, mutation_rate):
        population_raked = self.rank_path(current_population)
        selection_results = self.selection(population_raked, elite_size)
        mating_pool = self.mating_pool(current_population, selection_results)
        children = self.breed_population(mating_pool, elite_size)
        next_population = self.mutate_population(children, mutation_rate)
        return next_population

    def rank_path(self, current_population):
        results = {}
        for index, path in enumerate(current_population):
            results[index] = Fitness(path).getFitness()
        return sorted(results.items(), key=operator.itemgetter(1), reverse=True)

    def selection(self, population_raked, elite_size):
        pass

    def mating_pool(self, current_population, selection_results):
        pass

    def breed_population(self, mating_pool, elite_size):
        pass

    def mutate_population(self, children, mutation_rate):
        return None
