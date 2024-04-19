
import numpy as np

class TSPSolver:
    def __init__(self, distances):
        self.distances = distances
        self.n = len(distances)
        self.best_tour = None
        self.best_cost = float('inf')
        self.visited = [False] * self.n
    
    def solve(self):
        self.best_tour = None
        self.best_cost = float('inf')
        self.visited = [False] * self.n
        initial_tour = [0]
        self.visited[0] = True
        self.branch_and_bound(initial_tour, 0, 0)
    
    def branch_and_bound(self, tour, cost, level):
        if level == self.n - 1:
            last_city = tour[-1]
            cost += self.distances[last_city][0]
            if cost < self.best_cost:
                self.best_tour = tour
                self.best_cost = cost
        else:
            for city in range(1, self.n):
                if not self.visited[city]:
                    new_cost = cost + self.distances[tour[-1]][city]
                    if new_cost < self.best_cost:
                        self.visited[city] = True
                        self.branch_and_bound(tour + [city], new_cost, level + 1)
                        self.visited[city] = False
    
    def get_best_tour(self):
        return self.best_tour
    
    def get_best_cost(self):
        return self.best_cost