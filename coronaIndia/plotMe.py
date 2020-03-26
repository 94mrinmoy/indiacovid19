import pandas as pd
import matplotlib.pyplot as plt
import Corona.settings as settings
import numpy as np
#series = pd.read_excel('Book1.xlsx')
#series = pd.read_csv('Book1.csv',delimiter=',')
#print(series)

def plotMe():
    x = [0,1,1,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,5,5,28,30,31,34,39,43,56,62,73,82,102,113,119,142,156,194,244,330,396,499,536,606]


    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    langs = range(0,len(x))
    #students = [23,17,35,29,12]
    ax.bar(langs,x,width=1.0)
    #ax.set_xticks(x)
    ax.set_xticklabels(langs)
    
    #ax.set_xlabel('from 29/02/20209 to 26/03/2020')
    #ax.set_title('Daily Affected count per day since firt confirmed case.')
    #ax.set_xticks(x)
    #ax.set_xticklabels(labels)
    #ax.legend()

    ax.set_xticks(np.arange(len(x)))
    ax.set_xticklabels(x, rotation = 90)
    #plt.savefig(settings.PROJECT_ROOT + '\\coronaIndia\\static\\images\\graph.png')
    plt.savefig(img.save(settings.PROJECT_ROOT + '/coronaIndia/static/images/graph.png')
    #plt.show()
    print('graph done')

#plotMe()    