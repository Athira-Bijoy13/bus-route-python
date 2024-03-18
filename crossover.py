import random


def crossover_function(parent1,parent2,nodes):
    buses=len(parent1)
    gen1=[]
    # parent1 as array
    for route in parent1:
        for stop in route:
            if stop!=0:
                gen1.append(stop)
        gen1.append(nodes)
        nodes=nodes+1

    # print(gen1)
    nodes=nodes-buses
    gen2=[]
    # parent2 as array
    for route in parent2:
        for stop in route:
            if stop!=0:
                gen2.append(stop)
        gen2.append(nodes)
        nodes=nodes+1

    # print(parent2,gen2)
    nodes=nodes-buses
    size=len(gen1)
    p1=random.randint(0,size-1)
    p2=random.randint(0,size-1)
    start_point=min(p1,p2)
    end_point=max(p1,p2)
    child=[None]*size
    # taking random 2points and copying elements of parent1 (gen1) inchild with the range
    child[start_point:end_point+1]=gen1[start_point:end_point+1]
    # print(child)

    # filling remaining points with stops in parent2 retaining its order
    i=0
    while i<size:
        if child[i]==None:
            if gen1[i]>=nodes:
                child[i]=gen1[i]
            else:
                for element in gen2:
                    if element not in child and element<nodes:
                        child[i]=element
                        break
        i=i+1
    # print(child) 
    bus_route=[]
    route=[0]
    # generating bus routes from thechild array
    for stop in child:
        if stop<nodes:
            route.append(stop)
        else:
            route.append(0)
            bus_route.append(route)
            route=[0]
    # print(bus_route)
    return bus_route      










# p1=[[0, 9, 8, 0], [0, 7, 4, 0], [0, 3, 2, 6, 0], [0, 1, 5, 0]]
# p2= [[0, 9, 8, 0], [0, 7, 5, 0], [0, 6, 4, 0], [0, 1, 3, 2, 0]]
# crossover_function(p1,p2,10)