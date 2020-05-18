class Fitness:
    def __init__(self, path):
        self.path = path
        self.fitness = 0.0
        self.distance = 0.0

    def getCost(self):
        self.distance = sum(lat.distance(lng) for lat, lng in zip(self.path, self.path[1:]))
        self.distance += self.path[len(self.path) - 1].distance(self.path[0])
        return self.distance

    def getFitness(self):
        self.fitness=1 / float(self.getCost())
        return self.fitness
