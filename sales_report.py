"""Generate sales report showing total melons each salesperson sold."""

# create empty dictionary: saler: number of sold melons
saler_melons = {}
# open file
f = open('sales-report.txt')

# read all lines from file
for line in f:
    # remove all trailing whitespaces
    line = line.rstrip()
    # crate list of strings from line seperated with |
    entries = line.split('|')

    salesperson = entries[0]
    melons = int(entries[2])
    
    # saler_melons[salesperson] = melons if salerperson wasn't added to saler_melons, 
    # saler_melons[salesperson] = saler_melons[salesperson] + melons otherwise
    saler_melons[salesperson] = saler_melons.get(salesperson, 0) + melons

for key, val in saler_melons.items():
    print(f'{key} sold {val} melons')