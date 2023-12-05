import math

# Latitude and longitude data for 10 cities (example data)
cities = {
    "New York": (40.7128, -74.0060),
    "Los Angeles": (34.0522, -118.2437),
    "Chicago": (41.8781, -87.6298),
    "Houston": (29.7604, -95.3698),
    "Phoenix": (33.4484, -112.0740),
    "Philadelphia": (39.9526, -75.1652),
    "San Antonio": (29.4241, -98.4936),
    "San Diego": (32.7157, -117.1611),
    "Dallas": (32.7767, -96.7970),
    "San Jose": (37.3382, -121.8863)
}

# Function to calculate distance between two geographical coordinates using Haversine formula
def haversine(coord1, coord2):
    R = 6371  # Radius of the Earth in kilometers
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

# Create a distance matrix using the Haversine formula
num_cities = len(cities)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]

for i, (city1, coord1) in enumerate(cities.items()):
    for j, (city2, coord2) in enumerate(cities.items()):
        if i != j:
            distance = haversine(coord1, coord2)
            distance_matrix[i][j] = distance

# Display the distance matrix
for row in distance_matrix:
    print(row)