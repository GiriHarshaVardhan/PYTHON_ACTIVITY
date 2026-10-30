''' Environmental Monitoring Data Analyzer: Analyse nested lists of air-quality
 or water-quality readings, calculate averages and extremes, and classify observations
   using supplied threshold values. '''

readings = [[40, 45, 50], [80, 85, 90]]

for i in range(2):
    avg = sum(readings[i]) / 3
    print("Location", i+1, "- Max:", max(readings[i]), "Min:", min(readings[i]))
    if avg > 70:
        print("Danger: Pollution levels are hazardous!")