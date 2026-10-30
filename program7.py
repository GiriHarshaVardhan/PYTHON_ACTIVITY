'''Multi-Product Price Fluctuation Analysis: Process historical product prices
 stored in lists, calculate percentage changes, identify maximum fluctuations, 
 and flag products exceeding a supplied threshold.'''
old_prices = [100, 50]
new_prices = [120, 48] 

for i in range(2):
    fluctuation = ((new_prices[i] - old_prices[i]) / old_prices[i]) * 100
    print("Product", i+1, "Changed by:", fluctuation, "%")
    if fluctuation > 15 or fluctuation < -15:
        print("Alert: High price fluctuation!")