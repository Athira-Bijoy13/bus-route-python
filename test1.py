import random
from deap import base, creator, tools, algorithms

# Define the optimization problem
creator.create("FitnessMin", base.Fitness, weights=(1.0,))  # Minimize the fitness value
creator.create("Individual", list, fitness=creator.FitnessMin)

# Define the problem-specific functions
def objective(individual):
    x, y = individual
    return x**2 + y**2,

def constraint(individual):
    x, y = individual
    return 2 * x + y - 5,  # Constraint: 2x + y <= 5

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -5, 5)  # Decision variables within the range [-5, 5]
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=2)  # Two decision variables
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", objective)
toolbox.decorate("evaluate", tools.DeltaPenalty(constraint, delta=0))  # Apply penalty for violating constraints

toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Genetic Algorithm parameters
population_size = 50
num_generations = 100

# Create an initial population
population = toolbox.population(n=population_size)

# Evaluate the entire population
fitnesses = list(map(toolbox.evaluate, population))
for ind, fit in zip(population, fitnesses):
    ind.fitness.values = fit

# Run the genetic algorithm
algorithms.eaMuPlusLambda(population, toolbox, mu=population_size, lambda_=2*population_size,
                          cxpb=0.7, mutpb=0.2, ngen=num_generations, stats=None, halloffame=None, verbose=True)

# Print the best individual found
best_individual = tools.selBest(population, k=1)[0]
print("Best Individual:", best_individual)
print("Objective Value:", best_individual.fitness.values[0])
