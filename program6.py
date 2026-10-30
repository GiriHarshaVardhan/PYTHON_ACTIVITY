'''Bus Passenger Occupancy Simulation: Process boarding and 
alighting counts across multiple stops, calculate passenger counts
 at each stop, and flag any capacity violations. '''
boarding = [10, 5, 8]
alighting = [0, 3, 5]
passengers = 0
capacity = 15

for i in range(3):
    passengers = passengers + boarding[i] - alighting[i]
    print("Stop", i+1, "Passengers:", passengers)
    if passengers > capacity:
        print("Alert: Bus overloaded!")