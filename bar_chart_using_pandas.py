from matplotlib import pyplot as plt
import numpy as np
from collections import Counter
import pandas as pd

plt.style.use('fivethirtyeight')


df = pd.read_csv('data.csv')

languages_counter = Counter()
for lang in df['LanguagesWorkedWith']:
    languages_counter.update(lang.split(";"))

languages =[]
popularity =[]

for x in languages_counter.most_common(15):
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