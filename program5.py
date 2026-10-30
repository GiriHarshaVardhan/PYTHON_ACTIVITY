''' Weekly Electricity Consumption Matrix: Process appliance-wise 
electricity readings across seven days, calculate daily and appliance
 totals, and identify consumption exceeding specified limits. '''

usage_matrix = [[10, 20, 15], [30, 40, 35]] 
limit = 70

for i in range(2):
    total_usage = sum(usage_matrix[i])
    print("Appliance", i+1, "Total:", total_usage)
    if total_usage > limit:
        print("Warning: Usage limit exceeded!")