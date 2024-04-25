import random
import timeit
import math

def main():
     data=[[0, 5, 8, 6, 7, 3,2,5,4,3],  
        [5, 0, 4, 2, 7, 1,4,6,8,2],
        [8, 4, 0, 3, 6, 2,3,5,4,6], 
        [6, 2, 3, 0, 5, 2,8,4,3,5], 
        [7, 7, 6, 5, 0, 4,3,3,8,4],  
        [3, 1, 2, 2, 4, 0,6,1,5,3],
        [2,4,3,8,3,6,0,2,6,7],
        [5,6,5,4,3,1,2,0,5,3],
        [4,8,4,3,8,5,6,5,0,2],
        [3,2,6,5,4,3,7,3,2,0]]
     buses=4
     no_of_nodes=10
     bus_capacity=15
     stop_capacity=[0, 4, 5, 4, 7, 7,6,4,5,5]
     greedy_algo(data,no_of_nodes,buses,stop_capacity,bus_capacity)
                  # 0, 1, 2, 3, 4, 5
def greedy_algo(data,no_of_nodes,buses,stop_capacity,bus_capacity):
     start = timeit.default_timer()
     solution = [[] for _ in range(buses)]
     remaining_capacity = [bus_capacity] * buses
     unassigned_nodes = list(range(1, no_of_nodes))  # Exclude the depot
     distance_sol=[0 for _ in range(buses)]

     for i in range(buses):
        solution[i].append(0) 
     while unassigned_nodes:
         for i in range(buses):                                                 
             nodes=[node for node in unassigned_nodes if stop_capacity[node]<=remaining_capacity[i]]              #no of nodes* no of buses N*B `
             if len(nodes)>0:
               distance_array=[{'dist':data[solution[i][-1]][node],'index':node} for node in nodes] 
               next_node=min(distance_array, key=lambda x:x['dist'])['index']
               distance_sol[i]+=data[solution[i][-1]][next_node]
               solution[i].append(next_node)
               unassigned_nodes.remove(next_node)
               remaining_capacity[i]-=stop_capacity[next_node]
               
     bus_capacities=[bus_capacity-remaining_capacity[i] for i in range(buses)]
     total_dist=0
     for i in range(buses):
         distance_sol[i]+=data[solution[i][-1]][0]
         solution[i].append(0)
         remaining_capacity[i]-=stop_capacity[0]
         total_dist+=distance_sol[i]
  
     print(solution,bus_capacities,distance_sol,total_dist)


            





    
     stop = timeit.default_timer()
     elapsed_time = stop - start
     elapsed_time_str = "{:.8f}".format(elapsed_time)
     print("\n\tGREEDY ALGORITHM\n")
     print("Optimal bus route::",solution)
     print("Capacity obtained for each bus::",bus_capacities)
     print("Total distance travelled for each bus route::",distance_array)
     print("Total distance travelled of all buses::",total_dist)
     print("Execution Time:", elapsed_time_str, "seconds\n")

     return solution,bus_capacities,distance_array,total_dist,elapsed_time_str
         

if __name__ == "__main__":
    main()