import numpy as np
import genetic_algorithm
import ortools_algorithm
import backtrack_algorithm
import matplotlib.pyplot as plt
import math
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

for i in range(8,22):
    num_locations=i
    genetic_dist_mean=0
    greedy_dist_mean=0
    genetic_exec_mean=0
    greedy_exec_mean=0
    backtrack_dist_mean=0
    backtrack_exec_mean=0
    bus_capacity=20
    for j in range(1,6) :
        distance_matrix=create_distance_matrix(num_locations,30)
       
        no_of_students=np.random.randint(3,10,size=num_locations)
        no_of_students[0]=0
        total_students=sum(no_of_students)
        no_buses=math.ceil(total_students/bus_capacity)
         
        no_of_generations=150*num_locations                       
        # print(len(distance_matrix),no_buses,no_of_students,total_students,bus_capacity)
        # print("INPUT DATA ::")
        # print("Number of stops:: ",num_locations)
        # print("Number of bus::",no_buses)
        # print("Maximum capacity of each bus::",bus_capacity)
        # print("Distance Matrix ::")
        # for row in distance_matrix:
        #     print(row)
        
        # print("Number of students at each stop::", no_of_students)
        # print("")
        # print("OUTPUT ")
        genetic_result=genetic_algorithm.genetic_algorithm(distance_matrix,num_locations,no_buses,no_of_students,bus_capacity,no_of_generations)
        # ortools_algorithm.ortool_algo(distance_matrix,num_locations, no_buses,no_of_students,bus_capacity)
        greedy_result=greedy_algorithm.greedy_algo(distance_matrix,num_locations,no_buses,no_of_students,bus_capacity)
        backtrack_result=backtrack_algorithm.backtrack_algo(distance_matrix,num_locations,no_buses,no_of_students,bus_capacity)
        # print(genetic_result[3],genetic_result[4])
        genetic_exec_mean+=float(genetic_result[4])
        genetic_dist_mean+=float(genetic_result[3])
        greedy_exec_mean+=float(greedy_result[4])
        greedy_dist_mean+=float(greedy_result[3])
        backtrack_dist_mean+=float(backtrack_result[3])
        backtrack_exec_mean+=float(backtrack_result[4])
    
    input_size.append(num_locations)
    # greedy_exec=sum(greedy_exec_mean)/5
    # greedy_dist=sum(greedy_dist_mean)/5
    # genetic_exec=sum(genetic_exec_mean)/5
    # genetic_dist=sum(genetic_dist_mean)/5
    exec_time_genetic.append(float((genetic_exec_mean)/5))
    genetic_dist.append(float((genetic_dist_mean)/5))
    exec_time_greedy.append(float((greedy_exec_mean)/5))
    greedy_dist.append(float((greedy_dist_mean)/5))
    exec_time_backtrack.append(float(backtrack_exec_mean/5))
    backtrack_dist.append(float(backtrack_dist_mean/5))






    print("")
print(input_size,exec_time_genetic,exec_time_greedy)

print(genetic_dist,greedy_dist)

# for i in range(1,6):
#     print(input_size[i],exec_time_genetic[i],genetic_dist[i],exec_time_greedy[i],greedy_dist[i])
plt.figure(figsize=(8, 6))

# Plot execution times for Genetic Algorithm
plt.plot(input_size,genetic_dist,  marker='o', label='Genetic Algorithm')

# Plot execution times for Greedy Algorithm
plt.plot(input_size,greedy_dist,  marker='o', label='Greedy Algorithm')

plt.plot(input_size,backtrack_dist,  marker='o', label='Backtracking Algorithm')


plt.xlabel('Input size')
plt.ylabel('Minimum Distance')

plt.title('Input Size vs. Minimum Distance')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))

# Plot execution times for Genetic Algorithm
plt.plot(input_size,exec_time_genetic,  marker='o', label='Genetic Algorithm')

# Plot execution times for Greedy Algorithm
plt.plot(input_size,exec_time_greedy,  marker='o', label='Greedy Algorithm')

plt.plot(input_size,exec_time_backtrack,  marker='o', label='Backtracking Algorithm')
plt.xlabel('Input size')
plt.ylabel('Execution Time')

plt.title('Input Size vs. Execution Time')
plt.legend()
plt.grid(True)
plt.show()
    
# t_statistic, p_value = ttest_ind(genetic_dist, greedy_dist)

# # Print results
# print("T-statistic:", t_statistic)
# print("P-value:", p_value)
