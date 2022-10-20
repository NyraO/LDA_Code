import os

pkl_files = []
# directory of where the .pkl files are located since the data is being extracted from there
for file in os.listdir("C://Users//Kois//Downloads//with_verb"):
    if file.endswith(".pkl"):
        pkl_files.append(file.replace('.pkl',""))

csv = [['k','alpha','beta','coherence']]
for row in pkl_files:
    cols = row.split("_")
    csv.append([cols[1][1:], cols[2][1:], cols[3][1:], cols[4][1:]])

summary = {}
# take the maximum coherence found at that k after different alpha and beta combination model training
for k,alpha,beta,coherence in csv[1:]:
    summary[k] = max(summary.get(k,0), float(coherence))

# convert dictoinary to list of [(key, value),...] pairs
to_plot = sorted(summary.items(),key=lambda k:int(k[0]))


import matplotlib.pyplot as plt

# extract the x and y values separately for plotting
x = [item[0] for item in to_plot]
y = [item[1] for item in to_plot]

plt.plot(x, y)

plt.ylabel("coherence")
plt.xlabel("k-topics")

plt.show()
