''' Traffic Violation Penalty Calculator: Process multiple violations 
using vehicle category, offence type, repeat-offence status, and
 predefined fine rules; calculate the final penalty and identify 
 disqualification conditions. '''
offence_type = "speeding"
fine = 0

if offence_type == "speeding":
    fine = 1000
elif offence_type == "no helmet":
    fine = 500

print("Traffic Fine Amount:", fine)