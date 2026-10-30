'''Progressive Water Tariff Analysis: Calculate bills for multiple
 households using consumption slabs, fixed fees, and penalties; 
 compare consumption patterns and identify excessive usage. '''
usages = [80, 150]
fixed_fee = 50

for water in usages:
    if water <= 100:
        bill = fixed_fee + (water * 5)
    else:
        bill = fixed_fee + (100 * 5) + ((water - 100) * 10)
        print("Alert: Excessive usage!")
    print("Total Bill: Rs.", bill)