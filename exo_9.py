# used a dictionqary to pair city and population
city_populations = {}

print("Enter city names one by one. Type 'stop' to finish:")

while True:
    city_name = input("City name: ").strip()
    
    if city_name.lower() == "stop":
        break
    
    population = len(city_name) * 1_000_000  # 1 million per letter
    
    city_populations[city_name] = population

sorted_cities = sorted(city_populations.items(), key=lambda item: item[1], reverse=True)

print("\nCities and their populations:")
for city, population in sorted_cities:
    print(f"{city}: {population:,}")
