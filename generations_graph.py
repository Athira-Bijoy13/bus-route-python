import numpy as np
import genetic_algorithm
import ortools_algorithm
import backtrack_algorithm
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import greedy_algorithm
def create_distance_matrix(num_locations,max_distance):
    distance_matrix=np.random.randint(3,max_distance,size=(num_locations,num_locations))
    np.fill_diagonal(distance_matrix,0)
    distance_matrix=(distance_matrix+distance_matrix.T)/2
    return distance_matrix


input_size=[]
exec_time_genetic=[]
exec_time_greedy=[]
genetic_dist=[]
greedy_dist=[]
exec_time_backtrack=[]
backtrack_dist=[]



num_locations=12
genetic_dist_mean=0
greedy_dist_mean=0
genetic_exec_mean=0
greedy_exec_mean=0
backtrack_dist_mean=0
backtrack_exec_mean=0
distance_matrix=create_distance_matrix(num_locations,30)
no_buses=int(num_locations/3)
no_of_students=np.random.randint(3,10,size=num_locations)
no_of_students[0]=0
total_students=sum(no_of_students)
bus_capacity=int((total_students/no_buses)/4)*4+6    
for i in range(0,25):
    no_of_generations=15*num_locations *i
    genetic_result=genetic_algorithm.genetic_algorithm(distance_matrix,num_locations,no_buses,no_of_students,bus_capacity,no_of_generations)

    exec_time_genetic.append(genetic_result[4])
    genetic_dist.append(genetic_result[3])
    input_size.append(no_of_generations)
    print(i)

plt.figure(figsize=(8, 6))

# Plot execution times for Genetic Algorithm
plt.plot(input_size,genetic_dist,  marker='o', label='Genetic Algorithm')

plt.xlabel('Input size')
plt.ylabel('Minimum Distance')

plt.title('Input Size vs. Minimum Distance')
plt.legend()
plt.grid(True)
plt.show()
       



plt.figure(figsize=(8, 6))

# Plot execution times for Genetic Algorithm
plt.plot(input_size,exec_time_genetic,  marker='o', label='Genetic Algorithm')

plt.xlabel('Input size')
plt.ylabel('Execution Time')

plt.title('Input Size vs. Execution Time')
plt.legend()
plt.grid(True)
plt.show()