# def order_crossover(parent1, parent2):
import random

class Bus_route:
    def __init__(self, demand,index):
        self.demand=demand
        self.index=index
def brbax_crossover_with_capacity(parent1, parent2, capacity_limits,stop_capacity):  
    offspring=[]
    visited=[]

    route_strength=[]
    sum=0
    bus_index=0

    for route in parent1:
        sum=0
        for stop in route:
            sum+=stop_capacity[stop]
        if capacity_limits-sum<0:
                    sum=sum-99
        temp=Bus_route(capacity_limits-sum,bus_index)
        bus_index+=1
        route_strength.append(temp)
    for i in range(len(parent1)//2):
         offspring.append(parent1[route_strength[i].index])
    for route in offspring:
        for stop in route:
             if stop!=0:
                  visited.append(stop)
    next_route=[0]
    sum=0
    # print(visited)
    for route in parent2:
        for stop in route:
             if stop not in visited and stop!=0:
                  if sum+stop_capacity[stop]<=capacity_limits:
                       sum=sum+stop_capacity[stop]
                       next_route.append(stop)
                  else:
                       next_route.append(0)
                       copy=next_route.copy()
                       offspring.append(copy)
                       next_route=[0]
                       sum=stop_capacity[stop]
                       next_route.append(stop)
    # print(next_route,visited,sum)
    if sum!=0 :
         next_route.append(0)
         offspring.append(next_route)

    return offspring  
         
   


# def main():
    
    # parent1=[[0, 2, 3, 1, 0], [0, 7,9, 0], [0, 4,5, 0],[0,8,6,0]]
    # parent2=[[0, 4,1,7, 0], [0, 2, 5, 0], [0, 3,8, 0],[0,6,9,0]]
    # stop_capacity=[0, 4, 5, 7, 7, 7,6,4,5,8]
    # data=[[0, 5, 8, 6, 7, 3,2,5,4,3],  
    #     [5, 0, 4, 2, 7, 1,4,6,8,2],
    #     [8, 4, 0, 3, 6, 2,3,5,4,6], 
    #     [6, 2, 3, 0, 5, 2,8,4,3,5], 
    #     [7, 7, 6, 5, 0, 4,3,3,8,4],  
    #     [3, 1, 2, 2, 4, 0,6,1,5,3],
    #     [2,4,3,8,3,6,0,2,6,7],
    #     [5,6,5,4,3,1,2,0,5,3],
    #     [4,8,4,3,8,5,6,5,0,2],
    #     [3,2,6,5,4,3,7,3,2,0]]
    # result=brbax_crossover_with_capacity(parent1,parent2,15,stop_capacity)
    # # print(result)



# if __name__ == "__main__":
#     main()
    