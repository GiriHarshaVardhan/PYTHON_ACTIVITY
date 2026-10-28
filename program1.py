'''Fuel Consumption and Route Comparison: Calculate fuel 
requirements and journey costs for several vehicles using distance,
 mileage, fuel prices, and reserve requirements; identify the
 lowestcost feasible option. '''
distance = 500 
mileage = 15    
fuel_price = 100 

total_cost = (distance / mileage) * fuel_price
print(f"Total Journey Cost: {total_cost:.2f}")