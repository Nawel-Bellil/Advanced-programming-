
def calculate_taxi_rides():
    people = int(input("How many people need a ride? "))
    
    capacity = int(input("How many people fit in one taxi? "))

    full_taxis = people // capacity

    if people % capacity != 0:
        total_taxis = full_taxis + 1
    else:
        total_taxis = full_taxis

    print(f"Number of taxis needed: {total_taxis}")

calculate_taxi_rides()
