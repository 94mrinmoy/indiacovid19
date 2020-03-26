from PIL import Image, ImageDraw,ImageFont
import Corona.settings as settings

def getImage(dictAffectedData,dictCuredData,total,cTotal,dcount,allTotal):
 
    # img = Image.open("Corona\coronaIndia\static\images\india3.png")#('RGB', (100, 30), color = (0, 26, 102))
    #print(static)
    #img = Image.open(r"coronaIndia\static\images\india5.png")#('RGB', (100, 30), color = (0, 26, 102))
    img = Image.open(settings.STATIC_ROOT + "/images/india5.png")
    d = ImageDraw.Draw(img)
    fnt = ImageFont.load_default()
    fnt1 = ImageFont.load_default()
    #fnt = ImageFont.truetype('arial.ttf', 15)
    #fnt1 = ImageFont.truetype('arial.ttf', 18)
    print('here')
    #Ladakh
    d.text((300,72), str(dictAffectedData['Ladakh']),font=fnt, fill=(0, 26, 102))
    d.text((305,92), str(dictCuredData['Ladakh']),font=fnt, fill=(0, 26, 102)) 

    #Jammu and Kashmir
    d.text((254,110), str(dictAffectedData['Jammu and Kashmir']),font=fnt, fill=(0, 26, 102))
    d.text((255,127), str(dictCuredData['Jammu and Kashmir']),font=fnt, fill=(0, 26, 102)) 

    #Punjab
    d.text((260,203), str(dictAffectedData['Punjab']),font=fnt, fill=(0, 26, 102))
    d.text((260,220), str(dictCuredData['Punjab']),font=fnt, fill=(0, 26, 102)) 

    #Himachal Pradesh
    d.text((320,203), str(dictAffectedData['Himachal Pradesh']),font=fnt, fill=(0, 26, 102))
    d.text((320,220), str(dictCuredData['Himachal Pradesh']),font=fnt, fill=(0, 26, 102))     

    #Uttarakhand
    d.text((380,270), str(dictAffectedData['Uttarakhand']),font=fnt, fill=(0, 26, 102))
    d.text((380,287), str(dictCuredData['Uttarakhand']),font=fnt, fill=(0, 26, 102)) 

    #Haryana
    d.text((290,283), str(dictAffectedData['Haryana']),font=fnt, fill=(0, 26, 102))
    d.text((290,300), str(dictCuredData['Haryana']),font=fnt, fill=(0, 26, 102)) 

    #Rajasthan
    d.text((190,337), str(dictAffectedData['Rajasthan']),font=fnt, fill=(0, 26, 102))
    d.text((190,354), str(dictCuredData['Rajasthan']),font=fnt, fill=(0, 26, 102)) 

    #Uttar Pradesh
    d.text((415,387), str(dictAffectedData['Uttar Pradesh']),font=fnt, fill=(0, 26, 102))
    d.text((415,404), str(dictCuredData['Uttar Pradesh']),font=fnt, fill=(0, 26, 102)) 

    #Bihar
    d.text((580,425), str(dictAffectedData['Bihar']),font=fnt, fill=(0, 26, 102))
    d.text((580,442), str(dictCuredData['Bihar']),font=fnt, fill=(0, 26, 102)) 

    #Sikkim
    d.text((670,342), str(dictAffectedData['Sikkim']),font=fnt, fill=(0, 26, 102))
    d.text((670,359), str(dictCuredData['Sikkim']),font=fnt, fill=(0, 26, 102)) 

    #Arunachal Pradesh
    d.text((800,336), str(dictAffectedData['Arunachal Pradesh']),font=fnt, fill=(0, 26, 102))
    d.text((800,353), str(dictCuredData['Arunachal Pradesh']),font=fnt, fill=(0, 26, 102)) 

    #Assam
    d.text((800,390), str(dictAffectedData['Assam']),font=fnt, fill=(0, 26, 102))
    d.text((800,407), str(dictCuredData['Assam']),font=fnt, fill=(0, 26, 102)) 

    #Mizoram
    d.text((860,390), str(dictAffectedData['Mizoram']),font=fnt, fill=(0, 26, 102))
    d.text((860,407), str(dictCuredData['Mizoram']),font=fnt, fill=(0, 26, 102)) 

    #Manipur
    d.text((830,438), str(dictAffectedData['Manipur']),font=fnt, fill=(0, 26, 102))
    d.text((830,455), str(dictCuredData['Manipur']),font=fnt, fill=(0, 26, 102)) 

    #Meghalaya
    d.text((730,445), str(dictAffectedData['Meghalaya']),font=fnt, fill=(0, 26, 102))
    d.text((730,462), str(dictCuredData['Meghalaya']),font=fnt, fill=(0, 26, 102)) 

    #Tripura
    d.text((720,483), str(dictAffectedData['Tripura']),font=fnt, fill=(0, 26, 102))
    d.text((720,500), str(dictCuredData['Tripura']),font=fnt, fill=(0, 26, 102)) 

    #Nagaland
    d.text((795,486), str(dictAffectedData['Nagaland']),font=fnt, fill=(0, 26, 102))
    d.text((795,503), str(dictCuredData['Nagaland']),font=fnt, fill=(0, 26, 102)) 

    #West Bengal
    d.text((640,496), str(dictAffectedData['West Bengal']),font=fnt, fill=(0, 26, 102))
    d.text((640,513), str(dictCuredData['West Bengal']),font=fnt, fill=(0, 26, 102)) 

    #Jharkhand
    d.text((550,510), str(dictAffectedData['Jharkhand']),font=fnt, fill=(0, 26, 102))
    d.text((550,527), str(dictCuredData['Jharkhand']),font=fnt, fill=(0, 26, 102)) 

    #Madhya Pradesh
    d.text((390,470), str(dictAffectedData['Madhya Pradesh']),font=fnt, fill=(0, 26, 102))
    d.text((390,487), str(dictCuredData['Madhya Pradesh']),font=fnt, fill=(0, 26, 102)) 

    #Gujarat
    d.text((110,525), str(dictAffectedData['Gujarat']),font=fnt, fill=(0, 26, 102))
    d.text((110,542), str(dictCuredData['Gujarat']),font=fnt, fill=(0, 26, 102)) 

    #Chhattisgarh
    d.text((445,580), str(dictAffectedData['Chhattisgarh']),font=fnt, fill=(0, 26, 102))
    d.text((445,597), str(dictCuredData['Chhattisgarh']),font=fnt, fill=(0, 26, 102))    

    #Odisha
    d.text((515,616), str(dictAffectedData['Odisha']),font=fnt, fill=(0, 26, 102))
    d.text((515,633), str(dictCuredData['Odisha']),font=fnt, fill=(0, 26, 102))  

    #Maharashtra
    d.text((215,656), str(dictAffectedData['Maharashtra']),font=fnt, fill=(0, 26, 102))
    d.text((215,673), str(dictCuredData['Maharashtra']),font=fnt, fill=(0, 26, 102)) 

    #Telengana
    d.text((355,758), str(dictAffectedData['Telengana']),font=fnt, fill=(0, 26, 102))
    d.text((355,775), str(dictCuredData['Telengana']),font=fnt, fill=(0, 26, 102)) 

    #Goa
    d.text((145,769), str(dictAffectedData['Goa']),font=fnt, fill=(0, 26, 102))
    d.text((145,786), str(dictCuredData['Goa']),font=fnt, fill=(0, 26, 102))

    #Tamil Nadu
    d.text((320,962), str(dictAffectedData['Tamil Nadu']),font=fnt, fill=(0, 26, 102))
    d.text((320,979), str(dictCuredData['Tamil Nadu']),font=fnt, fill=(0, 26, 102))

    #Kerala
    d.text((220,932), str(dictAffectedData['Kerala']),font=fnt, fill=(0, 26, 102))
    d.text((220,949), str(dictCuredData['Kerala']),font=fnt, fill=(0, 26, 102))

    #Karnataka
    d.text((245,854), str(dictAffectedData['Karnataka']),font=fnt, fill=(0, 26, 102))
    d.text((245,871), str(dictCuredData['Karnataka']),font=fnt, fill=(0, 26, 102))

    #Total
    d.text((600,83) , "Total Affected Count            : " + str(allTotal + cTotal ),font=fnt1, fill=(0, 26, 102))
    d.text((600,100), "Total Active Affected Count : " + str(total),font=fnt1, fill=(0, 26, 102))
    d.text((600,117), "Total Cured Count               : " + str(cTotal),font=fnt1, fill=(0, 26, 102))
    d.text((600,134), "Total Death Count               : " + str(dcount),font=fnt1, fill=(0, 26, 102))

    #img.save(r'coronaIndia\static\images\india4.png')
    #print(settings.PROJECT_ROOT + '/coronaIndia/static/images/india4.png')
    #img.save(settings.PROJECT_ROOT + '\\coronaIndia\\static\\images\\india4.png')
    img.save(settings.PROJECT_ROOT + '/coronaIndia/static/images/india4.png')
    print(settings.PROJECT_ROOT + '/coronaIndia/static/images/india4.png')
    #img.save('coronaIndia\static\images\india.jp2', 'JPEG2000', quality_mode='dB', quality_layers=[41])