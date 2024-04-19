from flask import Flask,request
import genetic_algorithm
app=Flask(__name__)

@app.route("/")
def home():
   return "HELooo from vercel"

@app.route("/about")
def about():
   return "hello about"

@app.route('/generate-busroute',methods=['POST'])
def combination():

   distance_matrix=request.json['data']
   num_locations=request.json['num_locations']
   no_buses=request.json['no_buses']
   no_of_students=request.json['no_of_students']
   bus_capacity=request.json['bus_capacity']

#    print(distance_matrix,num_locations,no_buses,no_of_students,bus_capacity)
   g=genetic_algorithm.genetic_algorithm(distance_matrix,num_locations,no_buses,no_of_students,bus_capacity)
   print(g)
   result={
      "route":g[0],
      "bus_capacities":g[1],
      "distance_array":g[2],
      "min_distance":g[3],
      "execution_time":g[4]
   }
   return result


if __name__ == '__main__':
   app.run()
  