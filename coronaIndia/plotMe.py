import pandas as pd
import matplotlib.pyplot as plt
#series = pd.read_excel('Book1.xlsx')
series = pd.read_csv('covid.csv',delimiter=',')
print(series)


#x = [value1, value2, value3,....]
#plt.hist(series.transpose()['1970-01-01'], bins = 10)
#plt.show()