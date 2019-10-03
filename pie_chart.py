from matplotlib import pyplot as plt 

plt.style.use("fivethirtyeight")

slices = [120,80]

labels = ["Sixty","Fourty"]

plt.pie(slices,labels=labels,wedgeprops={'edgecolor':'black','linewidth': 3})



plt.title("My Pie Chart")
plt.tight_layout()
plt.show()

# Colors
# Blue = "#008fd5"
# Red = "#fc4f30"
# Yellow = "#e5ae37"
# Green = "#6d904f"