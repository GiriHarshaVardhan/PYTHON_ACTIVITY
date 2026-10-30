'''Smart Hostel Resource Monitoring: Analyse room-wise electricity
 and water consumption, calculate charges, identify threshold violations,
   and compare resource utilization across floors. '''
water_used = [50, 60] 
elec_used = [100, 250]

for i in range(2):
    bill = (water_used[i] * 2) + (elec_used[i] * 5)
    print("Room", i+1, "Bill: Rs.", bill)
    if elec_used[i] > 200:
        print("Warning: High electricity usage in Room", i+1)