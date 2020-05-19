class Fitness:
    def __init__(self, path):
        self.path = path
        self.fitness = 0.0
        self.distance = 0.0

    def getCost(self):
        self.distance = 0.0
        for i in range(0, len(self.path)):
            fromCity = self.path[i]
            toCity = None
            if i + 1 < len(self.path):
                toCity = self.path[i + 1]
            else:
                toCity = self.path[0]
            self.distance += fromCity.distance(toCity)
        return self.distance

    def getFitness(self):
        self.fitness = 1 / float(self.getCost())
        return self.fitness
