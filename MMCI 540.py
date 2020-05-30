import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#pip freeze > requirements.txt

df = pd.read_csv('venv/mmci_sample.csv')

df['total#'].hist(bins = 20)
plt.title('total #')
plt.show()

df.rate.hist(bins = 20)
plt.title('rate')
plt.show()

df.cost.hist(bins = 20)
plt.title('cost')
plt.show()