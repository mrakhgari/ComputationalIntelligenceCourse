import random


class genetic:
    def __init__(self, cities):
        self.cities = cities

    # create a random path.
    def create_path(self):
        return random.sample(self.cities, len(self.cities))

    # initial population in first time.
    def initial_population(self, population_size):
        population = []
        for i in range(population_size):
            population.append(self.create_path())
        return population

