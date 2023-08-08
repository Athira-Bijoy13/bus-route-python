from flask import Flask, request
from itertools import combinations
import random
import algorithm 
import numpy as np
app = Flask(__name__)

@app.route('/',methods=['GET'])
def helloworld():
   return "hello"


@app.route('/comb',methods=['POST'])
def combination():
   
   matrix=request.json['data']
   busSize=request.json['size']
   size=len(matrix)
   array=[i for i in range(1,size)]
   arraysize=int(len(array)/busSize)
   combs = combinations(array, arraysize)
    
   
   groups = []
   for comb in combs:
        l=len(array)-len(comb)
        next_comb=combinations(tuple(set(array) - set(comb)),l)
        for x in next_comb:
         groups.append([comb,x])
    
   # for grp in groups:
   #      print(grp)
   min_cost=99999
   for grp in groups:
      stop_array=[]
      total_sum=0
      best_route=[]
      for i in range(len(grp)):
         stop_array.append((0,)+grp[i])
         matrix_size=len(stop_array[i])
         distmatrix=[]
         for j in range(matrix_size):
            array=[0]*matrix_size
            for k in range(matrix_size):
               array[k]=matrix[stop_array[i][j]][stop_array[i][k]]
            distmatrix.append(array)
         # print(np.matrix(distmatrix))
         solver = algorithm.TSPSolver(distmatrix)
         solver.solve()

         best_tour = solver.get_best_tour()
         best_cost = solver.get_best_cost()
         total_sum=total_sum+best_cost
         best_route.append(best_tour)
   #   print(total_sum)
      if total_sum<min_cost:
         min_cost=total_sum
         min_cost_route=best_route
         route_path=stop_array

      #   print(stop_array)
   final_route=[]
   for x in range(len(min_cost_route)):
      arr=[0]*len(min_cost_route[x])
      for y in range(len(min_cost_route[x])):
         arr[y]=route_path[x][min_cost_route[x][y]]
      final_route.append(arr)


   print(min_cost,final_route)
   result={
      "cost":min_cost,
      "route":final_route
   }

   
   return result



if __name__ == '__main__':
   app.run()

   