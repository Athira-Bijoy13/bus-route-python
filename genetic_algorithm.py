
import random

from crossover import crossover_function
import timeit

class population:
    def __init__(self, route,dist):
        self.route=route
        self.dist=dist

def generate_random_solution(num_nodes, num_vehicles, vehicle_capacity, demands):
    
   
    remaining_capacity = [vehicle_capacity] * num_vehicles
    solution = [[] for _ in range(num_vehicles)]
    unassigned_nodes = list(range(1, num_nodes))  # Exclude the depot
    for i in range(num_vehicles):
        solution[i].append(0)  # Start each route at the depot (node 0)
    cnt=0
    while unassigned_nodes:
        # print(solution)
        current_vehicle = random.randint(0, num_vehicles - 1)
        promising_nodes = [node for node in unassigned_nodes if demands[node] <= remaining_capacity[current_vehicle]]
        if not promising_nodes:
            cnt=cnt+1
            if cnt>10:
                # print("cnt",cnt)
                break
            continue
        cnt=0
        # print("P==",promising_nodes)
        selected_node = random.choice(promising_nodes)
        solution[current_vehicle].append(selected_node)
        remaining_capacity[current_vehicle] -= demands[selected_node]
        unassigned_nodes.remove(selected_node)
    if cnt>10:
        solution=generate_random_solution(num_nodes, num_vehicles, vehicle_capacity, demands)
    else:
        for i in range(num_vehicles):
            solution[i].append(0)  # End each route at the depot (node 0)
    return solution




def calculate_route_distance(vehicle_route,data):
    distance=0
  
    for i in range(1,len(vehicle_route)):
        x=vehicle_route[i-1]
        y=vehicle_route[i]
        distance+=data[x][y]
    return distance

def calculate_route_capacity(vehicle_route,stop_capacity):
    total_capacity=0
    for stop in vehicle_route:
        total_capacity+=stop_capacity[stop]
    return total_capacity

def calculate_fitness(solution,data,stop_capacity,buses,bus_capacity):
    total_distance = 0
    total_capacity_violation = 0
   
    for vehicle_route in solution:
        route_distance = calculate_route_distance(vehicle_route,data)
       
        total_distance += route_distance
        
       
        route_capacity = calculate_route_capacity(vehicle_route,stop_capacity)
        # print(route_capacity)
        if route_capacity > bus_capacity:
           
            total_capacity_violation += (route_capacity - bus_capacity) * 999
    
    # print("total",total_capacity_violation,total_distance)
    fitness = total_distance + total_capacity_violation
    return fitness


def initialize_population(population_size, no_of_nodes,buses,stop_capacity, max_capacity):
    population = []
    # print("HII")
    min_stops=int(no_of_nodes/buses)
  
    a=0
    while a<population_size:
        # Generate random routes for each vehicle
        routes = generate_random_solution(no_of_nodes,buses,max_capacity,stop_capacity)
        flag=0
        for route in routes:
            if len(route)-2<min_stops:
                flag=1
               
                break
       
        if flag==0:
            population.append(routes)
            a=a+1
        # routes=a
        # print(population)

    # print("pp",len(population))
    return population


def roulette_wheel_spin(probabilities):
    # Perform roulette wheel spin to select an index based on probabilities
    rand_num = random.uniform(0, 1)
    cumulative_prob = 0
    for i, prob in enumerate(probabilities):
        cumulative_prob += prob
        if rand_num <= cumulative_prob:
            return i






def roulette_wheel_selection_with_capacity(population, fitness_scores, bus_capacity,stop_capacity):
    selected_parents = []
    total_fitness = sum(fitness_scores)
    # Normalize fitness scores to probabilities
    probabilities = [score / total_fitness for score in fitness_scores]

    while len(selected_parents) < len(population):
        # Select individuals probabilistically based on their probabilities
        selected_index = roulette_wheel_spin(probabilities)
        selected_individual = population[selected_index]
        feasibility=True

        for route in selected_individual:
            sum_of_bus=0
            for i in route:
                sum_of_bus=sum_of_bus+stop_capacity[i]
            if sum_of_bus>bus_capacity:
                feasibility=False
        # Check capacity feasibility before selecting
        # print(feasibility,selected_index,selected_individual)
        if feasibility:
            selected_parents.append(selected_individual)

    return selected_parents

def roulette_wheel_selection1(population, fitness_scores):
    selected_parents = []
    for _ in range(2):  # Select 2 parents for crossover
        rand = random.random()  # Generate a random number between 0 and 1
        cumulative_prob = 0
        for idx, fitness in enumerate(fitness_scores):
            cumulative_prob += fitness
            if rand <= cumulative_prob:
                selected_parents.append(population[idx])  # Select the individual
                break
    return selected_parents

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
    # data= [
    # [0, 20, 15, 30, 25, 10, 35, 40, 45, 50],
    # [20, 0, 25, 35, 15, 30, 20, 40, 35, 45],
    # [15, 25, 0, 30, 20, 10, 35, 25, 40, 30],
    # [30, 35, 30, 0, 10, 40, 15, 20, 25, 30],
    # [25, 15, 20, 10, 0, 25, 30, 35, 40, 45],
    # [10, 30, 10, 40, 25, 0, 35, 20, 15, 30],
    # [35, 20, 35, 15, 30, 35, 0, 25, 30, 20],
    # [40, 40, 25, 20, 35, 20, 25, 0, 15, 10],
    # [45, 35, 40, 25, 40, 15, 30, 15, 0, 25],
    # [50, 45, 30, 30, 45, 30, 20, 10, 25, 0]
# ]
    buses=4
    no_of_nodes=10
    stop_capacity=[0, 4, 5, 4, 7, 7,6,4,5,5]
                # 0, 1, 2, 3, 4, 5,6, 7 8,9
    bus_capacity=15
    res=genetic_algorithm(data,no_of_nodes,buses,stop_capacity,bus_capacity)
 
    # initial_sol=generate_random_solution(no_of_nodes,buses,10,stop_capacity)
    # print(initial_sol)
def genetic_algorithm(data,no_of_nodes, buses,stop_capacity,bus_capacity):
    start = timeit.default_timer()
    initial_population=initialize_population(10, no_of_nodes,buses,stop_capacity, bus_capacity)
    # initial_population=[[[0, 2, 3, 1, 0], [0, 7, 9, 0], [0, 4, 0], [0, 8, 6, 0]]]
    # depth=len(initial_population)
    # print(initial_population)
    min_score=1e9
    for a in range(1,1000):
       
        fitness_scores=[]
        bus_route_array=[]
        for initial_sol in initial_population:
            fitness=calculate_fitness(initial_sol,data,stop_capacity,buses,bus_capacity)
            fitness_scores.append(fitness)
            # print(fitness,initial_sol)
            bus_route=population(initial_sol,fitness)
            bus_route_array.append(bus_route)
            if fitness<min_score:
                min_score=fitness
                best_route=initial_sol
     
        selected_parents=bus_route_array
        # bus_route_array=[]
      
        new_gen=[]
        # print(len(selected_parents),len(initial_population),len(new_gen))
     
        set_of_parents=[]
       
        
        while len(new_gen)<len(initial_population):
            # parent_index=random.sample(range(0,len(selected_parents)-1),2)
            # # print(parent_index)


            # performing 4 way tournament selection process for parent selection
            #for parent1
            fitness_min=1e9
            selected_indices_parent1=random.sample(range(0,len(selected_parents)-1),4)
            
            for index in selected_indices_parent1:
                
                if selected_parents[index].dist<fitness_min:            #selecting parent with best fitness value(min)  
                    fitness_min=selected_parents[index].dist
                    parent1=selected_parents[index]


          

            selected_parents.remove(parent1)
           
            #for parent2
            selected_indices_parent2=random.sample(range(0,len(selected_parents)-1),4)
            fitness_min=1e9
            
            for index in selected_indices_parent2:
                if selected_parents[index].dist<fitness_min:                #selecting parent with best fitness value(min)
                    fitness_min=selected_parents[index].dist
                    parent2=selected_parents[index]
            selected_parents.append(parent1)
            
            parents=[parent1,parent2]
           
            if parents not in set_of_parents:
                set_of_parents.append(parents)
                parent1=parent1.route
                parent2=parent2.route
                # result=brbax_crossover_with_capacity(parent1,parent2,bus_capacity,stop_capacity)
                result=crossover_function(parent1,parent2,no_of_nodes)
                # print(result,"crossover")
                new_gen.append(result)
            # print(set_of_parents)
       
        new_generation=[]
        for data1 in new_gen:
            cut_point=random.sample(range(0,no_of_nodes-1),2)
            cut_point.sort()
            array=[]
            
            for bus in data1:
                for stop in bus:
                    if stop!=0:
                        array.append(stop)
            # print(array,cut_point)
            sub_array=array[cut_point[0]:cut_point[1]]
           
            random.shuffle(sub_array)
            i=cut_point[0]
            j=0
            
            while i<cut_point[1] and j<len(sub_array):
                array[i]=sub_array[j]
                j=j+1
                i=i+1
           
            ind=0
            new_routes=[]
          
            for x in range(0,len(data1)):
                new_bus_route=[0]
                y=0
                while y<len(data1[x])-2:
                    new_bus_route.append(array[ind])
                    ind=ind+1
                    y=y+1
                new_bus_route.append(0)
                new_routes.append(new_bus_route)
             
           
            new_generation.append(new_routes)
            
        initial_population=new_generation
        selected_parents=[]
   
    
    dist_array=[]
    capacity_array=[]
    for route in best_route:
        dist=calculate_route_distance(route,data)
        capacity=calculate_route_capacity(route,stop_capacity)
        dist_array.append(dist)
        capacity_array.append(capacity)

    stop = timeit.default_timer()
    elapsed_time = stop - start
    elapsed_time_str = "{:.8f}".format(elapsed_time)
    print("\n\tGENETIC ALGORITHM\n")
    print("INPUT DATA ::")
    print("Number of stops:: ",no_of_nodes)
    print("Number of bus::",buses)
    print("Maximum capacity of each bus::",bus_capacity)
    print("Distance Matrix ::")
    for row in data:
        print(row)
    
    print("Number of students at each stop::", stop_capacity)
    print("")
    print("OUTPUT ")

    print("\n\tGENETIC ALGORITHM\n")
    print("Optimal bus route::",best_route)
    print("Capacity obtained for each bus::",capacity_array)
    print("Total distance travelled for each bus route::",dist_array)
    print("Total distance travelled of all buses::",min_score)
    print("Execution Time:", elapsed_time_str, "seconds\n")
    
    return best_route,capacity_array,dist_array,min_score,elapsed_time_str


if __name__ == "__main__":
    main()
    