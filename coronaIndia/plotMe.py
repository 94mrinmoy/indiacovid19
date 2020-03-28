import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import Corona.settings as settings
import numpy as np
matplotlib.use('Agg')
#series = pd.read_excel('Book1.xlsx')
#series = pd.read_csv('Book1.csv',delimiter=',')
#print(series)

def plotMe():
    x = [0,1,1,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,5,5,28,30,31,34,39,43,56,62,73,82,102,113,119,142,156,194,244,330,396,499,536,606,694]

    xSpain = [0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,13,15,32,45,84,120,165,222,259,400,500,673,1073,1695,2277,2277,5232,6391,7798,9942,11748,13910,17963,20410,25374,28768,35136,39885,49515,56197]


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
    plt.savefig(settings.PROJECT_ROOT + '/coronaIndia/static/images/graph.png')
    #plt.show()
    print('graph done')

#plotMe()    



def plotMeDiffSpain():
    x = [0,1,1,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,5,5,28,30,31,34,39,43,56,62,73,82,102,113,119,142,156,194,244,330,396,499,536,606,694]

    xSpain = [0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,13,15,32,45,84,120,165,222,259,400,500,673,1073,1695,2277,2277,5232,6391,7798,9942,11748,13910,17963,20410,25374,28768,35136,39885,49515,56197]

    data = [x,
    xSpain]

    color_list = ['b', 'r']
    gap = .8 / len(data)
    for i, row in enumerate(data):
        X = np.arange(len(row))
    plt.bar(X + i * gap, row,
        width = gap,
        color = color_list[i % len(color_list)])

    plt.show()

def plotMeLatest() :
    y = [0,1,1,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,5,5,28,30,31,34,39,43,56,62,73,82,102,113,119,142,156,
    194,244,330,396,499,536,606,694,724]
    x = range(len(y))
    
    # x=['29/01/2020','30/01/2020','31/01/2020','01/02/2020','02/02/2020','03/02/2020','04/02/2020','05/02/2020','06/02/2020',
    # '07/02/2020','08/02/2020','09/02/2020','10/02/2020','11/02/2020','12/02/2020','13/02/2020','14/02/2020','15/02/2020',
    # '16/02/2020','17/02/2020','18/02/2020','01/02/2020','01/02/2020','01/02/2020','01/02/2020','01/02/2020']
    plt.scatter(x, y,color='red')
    plt.title('India Corona Virus Affected count per day')
    plt.xlabel('Day number starting from 29/01/2020 till yesterday')
    plt.ylabel('Corona Affected Count')
    #fig = plt.figure()
    #ax = fig.add_axes([0,0,1,1])
    plt.savefig(settings.PROJECT_ROOT + '/coronaIndia/static/images/graph.png')
    #plt.savefig(settings.PROJECT_ROOT + '\\coronaIndia\\static\\images\\graph.png')
    #plt.close()
    #plt.show()    

#plotMeLatest()    