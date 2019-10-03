from matplotlib import pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')
# print(plt.style.available)





ages_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496,42000,46752,49320,53200,56000,
        65316,64928,67317,68748,73752]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

x_indexes = np.arange(len(ages_x))

bar_width = 0.25


plt.bar(x_indexes-bar_width,py_dev_y,width=bar_width, label="Python") # Shifting bar Left
plt.bar(x_indexes,dev_y, color ='#444444',width=bar_width, label="All Devs")
plt.bar(x_indexes+bar_width,js_dev_y,width=bar_width,label="JavaScript")# Shifting bar Right

plt.xticks(x_indexes,ages_x)

plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Age")



plt.legend()

plt.tight_layout()
plt.show()
