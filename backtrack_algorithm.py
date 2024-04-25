import timeit


def calculate_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i+1]]
    return total_distance

def is_feasible(route, demand, capacity):
    return sum(demand[node] for node in route) <= capacity

def backtracking_vrp_util(graph, current_solution, remaining_nodes, demand, capacity, solutions, distance_matrix, min_distance):
    total_distance = sum(calculate_distance(route, distance_matrix) for route in current_solution)
    sorted_solution = tuple(tuple(sorted(route)) for route in current_solution)
    solutions.append((sorted_solution, total_distance))

    if total_distance > min_distance:
        return

    if not remaining_nodes:
        return

    current_node = remaining_nodes[0]
    for i in range(len(current_solution)):
        current_solution[i].append(current_node)
        if is_feasible(current_solution[i], demand, capacity):
            backtracking_vrp_util(graph, current_solution, remaining_nodes[1:], demand, capacity, solutions, distance_matrix, min_distance)
        current_solution[i].pop()

def backtracking_vrp(graph, demand, capacity, distance_matrix,buses):
    num_nodes = len(graph)
    remaining_nodes = list(range(1, num_nodes))  # Exclude the depot

    # Initialize the solutions with the depot as the starting and ending node for each route
    initial_solution = [[0] for _ in range(buses+1)]  # Three routes for three buses
    solutions = []

    min_distance = float('inf')  # Initialize min_distance as positive infinity

    backtracking_vrp_util(graph, initial_solution, remaining_nodes, demand, capacity, solutions, distance_matrix, min_distance)

    # Filter out duplicate solutions
    unique_solutions = set(solutions)

    # Filter solutions with exactly three routes and covering all nodes
    three_routes_solutions = [sol for sol in unique_solutions if len(sol[0]) == buses+1 and set(range(num_nodes)) <= set.union(*map(set, sol[0]))]

    return three_routes_solutions

# Example usage
# graph_example = [
#     [0, 5, 8, 6, 7, 3],
#     [5, 0, 4, 2, 7, 1],
#     [8, 4, 0, 3, 6, 2],
#     [6, 2, 3, 0, 5, 2],
#     [7, 7, 6, 5, 0, 4],
#     [3, 1, 2, 2, 4, 0]
# ]
def calculate_route_distance(vehicle_route,data):
    distance=0
  
    for i in range(1,len(vehicle_route)):
        x=vehicle_route[i-1]
        y=vehicle_route[i]
        distance+=data[x][y]
    return distance
def main():
    graph_example= [[0, 5, 8, 6, 7, 3,2,5,4,3],  
            [5, 0, 4, 2, 7, 1,4,6,8,2],
            [8, 4, 0, 3, 6, 2,3,5,4,6], 
            [6, 2, 3, 0, 5, 2,8,4,3,5], 
            [7, 7, 6, 5, 0, 4,3,3,8,4],  
            [3, 1, 2, 2, 4, 0,6,1,5,3],
            [2,4,3,8,3,6,0,2,6,7],
            [5,6,5,4,3,1,2,0,5,3],
            [4,8,4,3,8,5,6,5,0,2],
            [3,2,6,5,4,3,7,3,2,0]]

    demand_example = [0, 4, 5, 4, 7, 7,6,4,5,5]
    capacity_example = 15
    f=backtrack_algo(graph_example,10,3,demand_example,capacity_example)

def backtrack_algo(graph_example,no_of_nodes, buses,demand_example,capacity_example):

    start = timeit.default_timer()
    vrp_solutions = backtracking_vrp(graph_example, demand_example, capacity_example, graph_example,buses)
    modified_solutions = []

    for solution, distance in vrp_solutions:
        for route in solution:
            last_node=route[-1]
            distance+=graph_example[last_node][0]
        modified_solution = [tuple(list(route) + [0]) for route in solution]
        modified_solutions.append((modified_solution, distance))

    min_distance = float('inf')  # Initialize min_distance as positive infinity

    # Display only the solutions with the minimum distance
    for solution, distance in modified_solutions:
        min_distance = min(min_distance, distance)

    min_distance_solutions = [(solution, distance) for solution, distance in modified_solutions if distance == min_distance]
    stop = timeit.default_timer()
    elapsed_time = stop - start
    elapsed_time_str = "{:.8f}".format(elapsed_time)
    # Display the result
    print("\n\tBACKTRACKING SEARCH ALGORITHM\n")
    for solution, distance in min_distance_solutions:
        capacity_filled = [sum(demand_example[node] for node in route) for route in solution]
        distance_array=[]
        for vehicle_route in solution:
            route_distance = calculate_route_distance(vehicle_route,graph_example)
            distance_array.append(route_distance)

       
        print("Optimal Bus Route:", solution)
        # print("Capacity obtained of each bus : ",capacity_filled)
        # print("Total distance travelled for each bus route:: ", distance_array)
        print("Total distance travelled of all buses ",distance)
        break
    print("Execution Time:", elapsed_time_str, "seconds\n")
    return solution,capacity_filled,min_distance_solutions,distance,elapsed_time_str



if __name__ == "__main__":
    main()
    