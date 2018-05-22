import matplotlib.pyplot as plt

from matplotlib.ticker import MultipleLocator
import csv
re = {}
with open("/Users/jsa/Desktop/reveal.js-master/images/iphone.csv", "r") as f:
    data = csv.reader(f)
    re = {}
    for i,j in enumerate(data):
        re[i] = int(j[1])

print(re)

fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(1, 1, 1)




ax.plot([int(i) for i in re.keys()],[int(i) for i in re.values()],linewidth=4)
ax.xaxis.set_major_locator(MultipleLocator(12))
ticks = ["","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018"]
#ax.set_xticks(range(8))
ax.set_xticklabels(ticks,fontsize=15)
ax.text(2,75,"A",fontsize=65,fontweight="heavy")
ax.set_xlabel("Year")
ax.set_ylabel("Frequency")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig("iphone.png")
