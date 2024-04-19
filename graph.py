
import matplotlib.pyplot as plt	

input_size=[13,14,17,18,19]
genetic_dist=[178.5,195.5,257.0,301.5,315.0]
greedy_dist=[195.5,208.5,262.0,304.5,318.5]
backtrack_dist=[178.5,195.5,252.0,295.5,312.5]
genetic_time=[0.4703,0.6686,0.5766,0.9328,1.4764]
greedy_time=[0.0006,0.0009,0.0011,0.0031,0.0034]
backtrack_time=[1.2356,1.8352,2.0384,2.5766,3.0284]


plt.figure(figsize=(8, 6))

# Plot execution times for Genetic Algorithm
plt.plot(input_size,genetic_dist,  marker='o', label='Genetic Algorithm')

# Plot execution times for Greedy Algorithm
plt.plot(input_size,greedy_dist,  marker='o', label='Greedy Algorithm')
plt.plot(input_size,backtrack_dist,  marker='o', label='BackTracking Algorithm')


plt.xlabel('Input size')
plt.ylabel('Minimum Distance')

plt.title('Input Size vs. Minimum Distance')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 5))

# Plot execution times for Genetic Algorithm
plt.plot(input_size,genetic_time,  marker='o', label='Genetic Algorithm')

# Plot execution times for Greedy Algorithm
plt.plot(input_size,greedy_time,  marker='o', label='Greedy Algorithm')
plt.plot(input_size,backtrack_time,  marker='o', label='BackTracking Algorithm')


plt.xlabel('Input size')
plt.ylabel('Execution Time')

plt.title('Input Size vs. Execution Time')
plt.legend()
plt.grid(True)
plt.show()