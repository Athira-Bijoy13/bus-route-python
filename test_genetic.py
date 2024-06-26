

import random

def calculate_fitness(solution):
    total_distance = 0
    total_capacity_violation = 0
    # Iterate over each vehicle's route in the solution
    for vehicle_route in solution:
        route_distance = calculate_route_distance(vehicle_route)
        total_distance += route_distance
        
        # Check and penalize if capacity constraint is violated
        route_capacity = calculate_route_capacity(vehicle_route)
        if route_capacity > MAX_CAPACITY:
            # Penalize by adding a high value
            total_capacity_violation += (route_capacity - MAX_CAPACITY) * PENALTY_FACTOR
    
    # Combine both factors (distance and capacity violation) to get fitness
    fitness = total_distance + total_capacity_violation
    return fitness



def main():
#      data = [
#         # fmt: off
#       [0, 548, 776, 696, 582, 274, 502, 194, 308, 194, 536, 502, 388, 354, 468, 776, 662],
#       [548, 0, 684, 308, 194, 502, 730, 354, 696, 742, 1084, 594, 480, 674, 1016, 868, 1210],
#       [776, 684, 0, 992, 878, 502, 274, 810, 468, 742, 400, 1278, 1164, 1130, 788, 1552, 754],
#       [696, 308, 992, 0, 114, 650, 878, 502, 844, 890, 1232, 514, 628, 822, 1164, 560, 1358],
#       [582, 194, 878, 114, 0, 536, 764, 388, 730, 776, 1118, 400, 514, 708, 1050, 674, 1244],
#       [274, 502, 502, 650, 536, 0, 228, 308, 194, 240, 582, 776, 662, 628, 514, 1050, 708],
#       [502, 730, 274, 878, 764, 228, 0, 536, 194, 468, 354, 1004, 890, 856, 514, 1278, 480],
#       [194, 354, 810, 502, 388, 308, 536, 0, 342, 388, 730, 468, 354, 320, 662, 742, 856],
#       [308, 696, 468, 844, 730, 194, 194, 342, 0, 274, 388, 810, 696, 662, 320, 1084, 514],
#       [194, 742, 742, 890, 776, 240, 468, 388, 274, 0, 342, 536, 422, 388, 274, 810, 468],
#       [536, 1084, 400, 1232, 1118, 582, 354, 730, 388, 342, 0, 878, 764, 730, 388, 1152, 354],
#       [502, 594, 1278, 514, 400, 776, 1004, 468, 810, 536, 878, 0, 114, 308, 650, 274, 844],
#       [388, 480, 1164, 628, 514, 662, 890, 354, 696, 422, 764, 114, 0, 194, 536, 388, 730],
#       [354, 674, 1130, 822, 708, 628, 856, 320, 662, 388, 730, 308, 194, 0, 342, 422, 536],
#       [468, 1016, 788, 1164, 1050, 514, 514, 662, 320, 274, 388, 650, 536, 342, 0, 764, 194],
#       [776, 868, 1552, 560, 674, 1050, 1278, 742, 1084, 810, 1152, 274, 388, 422, 764, 0, 798],
#       [662, 1210, 754, 1358, 1244, 708, 480, 856, 514, 468, 354, 844, 730, 536, 194, 798, 0],
#         # fmt: on
#     ]
     
     data=[[0, 5, 8, 6, 7, 3],  
    [5, 0, 4, 2, 7, 1],
    [8, 4, 0, 3, 6, 2], 
    [6, 2, 3, 0, 5, 2], 
    [7, 7, 6, 5, 0, 4],  
    [3, 1, 2, 2, 4, 0]]
     buses=3
     stop_capacity=[0, 4, 2, 4, 8, 8]
                  # 0, 1, 2, 3, 4, 5
    
     visited=[0]
     capacity=0
     x=0
     total_capacity=[]
     initial_sol=[]
     vect=[0]
     total_dist=[]
     dist=0
     while len(visited)<len(data):
          
          min_value=999
          for y in range(0,len(data)):
               if y not in visited and data[x][y]<min_value:
                    min_value=data[x][y]
                    index=y
          
          if capacity+stop_capacity[index]<=10:
                dist=dist+data[x][index]
                x=index
                
                capacity=capacity+stop_capacity[index]
                visited.append(index)
                vect.append(index)
          else:
              vect.append(0)
              initial_sol.append(vect)
              vect.clear
              vect=[0]
              dist=dist+data[x][0]
              total_dist.append(dist)
              dist=0
              total_capacity.append(capacity)
              capacity=0
              x=0
        #   print(vect,visited,capacity,min_value)
     total_capacity.append(capacity)
     dist=dist+data[x][0]
     total_dist.append(dist)
     vect.append(0)
     initial_sol.append(vect)
     sum=0
     for d in total_dist:
          sum=sum+d
     print("initital bus route::",initial_sol)
     print("capacity for each bus::",total_capacity)
     print("total distance travelled for each bus route::",total_dist)
     print("total distance travelled of all buses::",sum)
  
         

                    
                    


if __name__ == "__main__":
    main()