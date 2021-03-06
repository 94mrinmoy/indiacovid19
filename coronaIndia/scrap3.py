import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import pandas as pd
from datetime import date

today = date.today()

states=[] 
allStates=[]
currentCount=[] 
curedCount=[] 
deathCount=[]
population=[]

def coronaData () :
    
    url= "http://www.mohfw.gov.in/"
    page= requests.get(url)
    #print(page.status_code)
    soup= BeautifulSoup(page.content,'html.parser')
    a= list(soup.children)
    startPoint = 0
    endPoint = 0
    for i,e in enumerate(soup.find_all('tr')):#, class_= "table-responsive")):
        #print(e.get_text())
        try:
            if e.get_text().split('\n')[2] == 'Andhra Pradesh' :
                startPoint = i
            elif e.get_text().split('\n')[2] == 'West Bengal' :
                endPoint = i    
                break
        except:
            pass     

    for i,e in enumerate(soup.find_all('tr')):#, class_= "table-responsive")):
        #print(startPoint)
        #print(e.get_text())
        #states.append(e.get_text().split('\n')[2])
        #print(e.get_text().split('\n')[4] + ':')
        #print(e.get_text().split('\n')[5])
        if i>=startPoint and i<=endPoint:#len(soup.find_all('tr'))-2:
            print(e.get_text())
            states.append(e.get_text().split('\n')[2])
            if e.get_text().split('\n')[3] != '':
                # cc = int(e.get_text().split('\n')[3]) + int(e.get_text().split('\n')[4])
                cc = int(e.get_text().split('\n')[3]) 
            else:
                #print(e.get_text())
                print('error1')
                #cc = int(e.get_text().split('\n')[4]) + int(e.get_text().split('\n')[5])
            if e.get_text().split('\n')[4] !='':    
                cuc = int(e.get_text().split('\n')[4])
            else:
                #cuc = int(e.get_text().split('\n')[6])
                print('error2')
            dc=int(e.get_text().split('\n')[5].replace('#',''))
        else:
            cc=0   
            cuc=0 
            dc=0
        currentCount.append(cc)#e.get_text().split('\n')[3])
        curedCount.append(cuc)
        deathCount.append(dc)
    #icount = soup.find_all('span', class_= "icount")[1].get_text()        
    #dcount = soup.find_all('span', class_= "icount")[3].get_text().replace('#','')
    icount = soup.find_all('strong')[5].get_text()        
    dcount = soup.find_all('strong')[7].get_text().replace('#','')
    allTotal = int(icount) + int(dcount)  
    print(allTotal,icount)
    return states,currentCount,curedCount,icount,dcount,deathCount,allTotal,startPoint,endPoint


def getPopulation():
    datas = []
    url= "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_population"
    page= requests.get(url)
    #print(page.status_code)
    soup= BeautifulSoup(page.content,'html.parser')
    a= list(soup.children)
    for e in soup.find_all('tr'):#, class_= "table"):
        datas.append(e.get_text().split('\n'))
    return datas#,population

#data = getPopulation()

# for i,a in enumerate(data):
#     if i >4 and i<41:
#         allStates.append(a[3])
#         if i!=14:
#             population.append(a[5].split('(')[0])
#         else:
#             population.append(a[5].split('(')[0].split('[')[0])
# print(allStates)
# print(population)


allStates = ['Uttar Pradesh', 'Maharashtra', 'Bihar', 'West Bengal', 'Madhya Pradesh', 'Tamil Nadu', 'Rajasthan', 'Karnataka', 
'Gujarat', 'Andhra Pradesh', 'Odisha', 'Telengana', 'Kerala', 'Jharkhand', 'Assam', 'Punjab', 'Chhattisgarh', 'Haryana', 
'Uttarakhand', 'Himachal Pradesh', 'Tripura', 'Meghalaya', 'Manipur', 'Nagaland', 'Goa', 'Arunachal Pradesh', 'Mizoram', 
'Sikkim', 'Delhi', 'Jammu and Kashmir', 'Puducherry', 'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu', 
'Andaman and Nicobar Islands', 'Ladakh', 'Lakshadweep']
population = ['199,812,341', '112,374,333', '104,099,452', '91,276,115', '72,626,809', '72,147,030', '68,548,437', '61,095,297', 
'60,439,692', '49,577,103', '41,974,218', '35,003,674', '33,406,061', '32,988,134', '31,205,576', '27,743,338', '25,545,198', 
'25,351,462', '10,086,292', '6,864,602', '3,673,917', '2,966,889', '2,570,390', '1,978,502', '1,458,545', '1,383,727', 
'1,097,206', '610,577', '16,787,941', '12,267,032', '1,247,953', '1,055,450', '585,764', '380,581', '274,000', '64,473']

#print(len(coronaData()))
states,currentCount,curedCount,icount,dcount,deathCount,allTotal,startPoint,endPoint = coronaData()
#print(len(states))
#print(currentCount[1:-1])

#states = states[1:-1]
currentCount = currentCount[startPoint:endPoint+1]
curedCount = curedCount[startPoint:endPoint+1]
deathCount = deathCount[startPoint:endPoint+1]
#print(len(states))
#print(len(currentCount))

populationDict = {}

def main():
    for i,a in enumerate(allStates) :
        populationDict.update({a:population[i]})

    #print(populationDict['West Bengal'])
    total=0
    cTotal = 0
    pop = []
    for i,s in enumerate(states):
        #print(states)
        print(s + ' : ' + str(currentCount[i]) +' / ' +populationDict[s] + ', Cured : ' + str(curedCount[i]))
        pop.append(int(populationDict[s].replace(',','')))
        total = total + int(currentCount[i])
        cTotal = cTotal + int(curedCount[i])

    print('total : ' + str(total))

    df = pd.DataFrame({'States':states,'Corona Affected Count':currentCount,'Cured Count':curedCount,'Total Population':pop,'Death Count':deathCount}) 

    notAffectedStates = list(set(allStates) - set(states))
    popu = []
    for s in notAffectedStates:
        popu.append(int(populationDict[s].replace(',','') ))
    df2 = pd.DataFrame({'States':notAffectedStates,'Corona Affected Count':[0]*len(notAffectedStates),'Cured Count':[0]*len(notAffectedStates),'Total Population':popu,'Death Count':[0]*len(notAffectedStates)})
    #print(df2)
    df = df.append(df2,  ignore_index=True)    

    df.to_csv('Corona_' + str(today) + '.csv', index=False, encoding='utf-8')
    return df,total,cTotal,icount,dcount,allTotal


def getPlotlyData(htmlPath):
    datas = []
    #url= getPlotlyData#"plotly.html"
    #page= #requests.get(url)
    #print(page.status_code)
    soup= BeautifulSoup(open(htmlPath),'html.parser')
    #a= list(soup.children)
    for e in soup.find_all('body'):#, class_= "table"):
        print('here')
        datas.append(e)
    return datas[0]#,population

def getPlotlyDataNew(htmlPath,htmlPath2,htmlPath3):
    htmlFile = open(htmlPath)
    data = htmlFile.readlines()
    htmlFile.close()
    htmlFile = open(htmlPath,'w')
    s=''
    for d in data[3:-2]:
        s=s+d
    htmlFile.write(s)
    htmlFile.close()

    htmlFile = open(htmlPath2)
    data = htmlFile.readlines()
    htmlFile.close()
    htmlFile = open(htmlPath3,'w')
    sn=''
    for d in data:
        if d.strip() =='<!-- add plotly -->':
            sn=sn+s
        sn=sn+d
    htmlFile.write(sn)
    htmlFile.close()

    print()



