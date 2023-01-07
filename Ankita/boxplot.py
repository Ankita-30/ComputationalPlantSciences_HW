import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np



    
#Open the file and read each line into an array
with open("outputt_b") as code:
    DLA = []
    for line in code:
        x=line.rstrip('\n')
        y=float(x)
        DLA.append(y)

with open("output") as code:
    DLA8 = []
    for line in code:
        x=line.rstrip('\n')
        y=float(x)
        DLA8.append(y)

with open("output_i") as code:
    DLA1 = []
    for line in code:
        x=line.rstrip('\n')
        y=float(x)
        DLA1.append(y)



#Save plot as png
mpl.use('agg')

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot([DLA8, DLA])

# Save the figure
fig.savefig('fig1.png', bbox_inches='tight') 






