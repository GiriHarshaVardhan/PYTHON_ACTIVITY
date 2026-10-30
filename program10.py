''' Smart Public Transport Fare Reconciliation: Calculate passenger
 fares across multiple routes and passenger categories, reconcile 
 collected revenue with expected revenue, and identify discrepancies. '''
passengers = [50, 30] 
fares = [20, 10]
collected_revenue = 1200 
expected_revenue = 0

for i in range(2):
    expected_revenue = expected_revenue + (passengers[i] * fares[i])

print("Expected Rs.", expected_revenue, "| Collected Rs.", collected_revenue)
if expected_revenue != collected_revenue:
    print("Discrepancy found! Amount missing: Rs.", expected_revenue - collected_revenue)