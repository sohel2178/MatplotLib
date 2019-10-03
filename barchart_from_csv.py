from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter

plt.style.use('fivethirtyeight')

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    row = next(csv_reader)
    language_counter = Counter()
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(";"))

languages =[]
popularity =[]

for x in language_counter.most_common(15):
    languages.append(x[0])  
    popularity.append(x[1])  

languages.reverse()
popularity.reverse()

plt.barh(languages,popularity)

# plt.xlabel("Languages")
plt.xlabel("No of People use")
plt.title("Most Popular Laguages")

# plt.legend()

plt.tight_layout()
plt.show()