from django.shortcuts import render
import coronaIndia.scrap3 as s3
import coronaIndia.getImage as gi
import coronaIndia.plotMe as pm
import Corona.settings as settings
# Create your views here.
from django.http import HttpResponse
import pandas as pd
from IPython.display import HTML


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    df,total,cTotal,icount,dcount,allTotal = s3.main()
    #print(df[1][1])
    #dfhtml = HTML(df.to_html(index=False))
    dfStates = list((df['States']))
    dfAffected = list(df['Corona Affected Count'])
    dfCured = list(df['Cured Count'])
    dfPop = list(df['Total Population'])
    data = []
    for i in range(len(dfStates)):
        data.append([dfStates[i],dfAffected[i],dfCured[i],dfPop[i]])
    #print (df)
    #htmlPath = pm.plotMeInt()
    #plotlyDiv = s3.getPlotlyData(htmlPath)
    #s3.getPlotlyDataNew(htmlPath,settings.PROJECT_ROOT + '/coronaIndia/templates/indexdup2.html',settings.PROJECT_ROOT + '/coronaIndia/templates/index.html')
    context = {
        'df':data,
        'total':total,
        'cTotal':cTotal,
        'dict':{'1':'Ladakh'}
        # 'plotlyDiv' : plotlyDiv
    }
    #print(plotlyDiv)
    #return render(request, 'index.html', context)
    return render(request, 'example.html', context)
    #return render (dfhtml.data)

def index2(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    df,total,cTotal,icount,dcount,allTotal = s3.main()
    #print(df[1][1])
    #dfhtml = HTML(df.to_html(index=False))
    df = df.sort_values(by=['Corona Affected Count'],ascending=False)
    dfStates = list((df['States']))
    dfAffected = list(df['Corona Affected Count'])
    dfCured = list(df['Cured Count'])
    dfDeath = list(df['Death Count'])
    dfPop = list(df['Total Population'])
    data = []
    dictAffectedData = {}
    dictCuredData = {}
    dictDeathData={}
    for i,s in enumerate(dfStates):
        dictAffectedData.update({s:dfAffected[i]})
        dictCuredData.update({s:dfCured[i]})
        dictDeathData.update({s:dfDeath[i]})
    #print(dictAffectedData)        
    for i in range(len(dfStates)):
        data.append([dfStates[i],dfAffected[i],dfCured[i],dfPop[i],dfDeath[i]])
    #print (df)
    pm.plotMeLatest()
    # htmlPath = pm.plotMeInt()
    # s3.getPlotlyDataNew(htmlPath,settings.PROJECT_ROOT + '/coronaIndia/templates/indexdup.html',settings.PROJECT_ROOT + '/coronaIndia/templates/indexMain.html')
    context = {
        'df':data,
        'total':allTotal+cTotal,
        'cTotal':cTotal,
        'dcount':dcount,
        'dictAffectedData':dictAffectedData,
        'dictCuredData':dictCuredData,
        'dictDeathData':dictDeathData
    }
    prvCountFile = open('aTotal.txt')
    prvCount = prvCountFile.read()
    prvCountFile.close()
    if True:#(total>int(prvCount)):
        #print('here')
        gi.getImage(dictAffectedData,dictCuredData,icount,cTotal,dcount,allTotal)
        pm.plotMeLatest()
        prvCountFile = open('aTotal.txt','w+')
        prvCountFile.write(str(total))
        prvCountFile.close()
    return render(request, 'indexMain.html', context)
    # return render(request, 'indexdup.html', context)
    #return render (dfhtml.data)