
class TSPSolver:
    def __init__(self, distances):
        self.distances = distances
        self.n = len(distances)
        self.best_tour = None
        self.best_cost = float('inf')
    
    def solve(self):
        self.best_tour = None
        self.best_cost = float('inf')
        initial_tour = list(range(self.n))
        self.branch_and_cut(initial_tour)
    
    def branch_and_cut(self, tour):
        if len(tour) == self.n:
            cost = self.calculate_tour_cost(tour)
            if cost < self.best_cost:
                self.best_tour = tour
                self.best_cost = cost
        else:
            for candidate_tour in self.generate_candidate_tours(tour):
                if self.calculate_lower_bound(candidate_tour) < self.best_cost:
                    self.branch_and_cut(candidate_tour)
    
    def generate_candidate_tours(self, tour):
        remaining_cities = set(range(self.n)) - set(tour)
        for city in remaining_cities:
            for i in range(len(tour) + 1):
                new_tour = tour[:i] + [city] + tour[i:]
                yield new_tour
    
    def calculate_tour_cost(self, tour):
        cost = 0
        for i in range(self.n):
            cost += self.distances[tour[i]][tour[(i + 1) % self.n]]
        return cost
    
    def calculate_lower_bound(self, tour):
        cost = self.calculate_tour_cost(tour)
        remaining_cities = set(range(self.n)) - set(tour)
        for city in remaining_cities:
            min_distance = min(self.distances[city][other_city] for other_city in remaining_cities)
            cost += min_distance
        return cost
    
    def get_best_tour(self):
        return self.best_tour
    
    def get_best_cost(self):
        return self.best_cost
