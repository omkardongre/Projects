import sys
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import csv
from Plot_AQI import avg_data


def met_data(month,year):
    file_html=open('Data/Html_Data/{}/{}'.format(year,month),'rb')
    # contain whole html
    plain_text=file_html.read()
    
    # lxml parser
    soup=BeautifulSoup(plain_text,"lxml")
    
    #storing  data  present inside  <td>'Day'</td>  i.e 'Day'
    tempD = [] 
    
    for table in soup.findAll('table',{'class':'medias mensuales numspan'}):
        for tr in table:
            for td in tr:
                tempD.append(td.get_text())
                
  
    #total columns are 15, as every element is present in the list 1D list so divide by 15 to get row count 
    Rows=int(len(tempD)/15)
    
    finalD = []
    
    for row in range(Rows):
   
        newtemp=[]
        for i in range(15):
            newtemp.append(tempD[0])
            tempD.pop(0)
                
        finalD.append(newtemp)

        
    #first row and last row has just labels, unwanted so remove that
    finalD.pop(Rows-1)
    finalD.pop(0)
  
    #length update
    Rows=Rows-2
    
    # in the dataset many columns have missing data , so removing that column number
    for i in range(Rows): 
        finalD[i].pop(14)
        finalD[i].pop(13)
        finalD[i].pop(12)
        finalD[i].pop(11)
        finalD[i].pop(10)
        finalD[i].pop(6)
        finalD[i].pop(4)
        finalD[i].pop(0)

    return finalD




        
        
        
if __name__=="__main__":
    
    path=os.getcwd()
    cpath=os.path.join(path,"Data/Real-Data")
    if not os.path.exists(cpath):
        os.makedirs(cpath)
 
    for year in range(2013,2017):
        final_data=[]
        with open(cpath+'/real_'+ str(year)+'.csv' , 'w') as csvfile:
            #styling looks like excel
            wr=csv.writer(csvfile,dialect='excel')
            wr.writerow(['T','TM','Tm','H','VV','V','VM','PM 2.5'])
            
        for month in range(1,13):
            temp=met_data(month,year)
            final_data=final_data+temp
        
        # getting target feature
        pm=avg_data(year)
      

        # combining  target feature and indenpendent feature together
        for i in range(len(pm)):
            final_data[i].append(pm[i])
      
        with open(cpath+'/real_'+str(year)+'.csv','a') as csvfile:
            wr=csv.writer(csvfile,dialect='excel')
            for row in final_data:
                flag=0
                for ele in row:
                    if flag>2:
                        break
                    elif ele=='' or ele=='-':
                        flag+=1
              
                #if row  has more than 2 blanks space that means the row is empty 
                if flag<2:
                    wr.writerow(row)
                
                
    total_data=[]
    for year in range(2013,2017):
        df=pd.read_csv(cpath+'/real_'+str(year)+'.csv','rb')
        total_data=total_data+df.values.tolist()
        
    
    with open(cpath+'/Real_Combine.csv','w') as  csvfile:
         wr=csv.writer(csvfile,dialect='excel')
         wr.writerow(['T','TM','Tm','H','VV','V','VM','PM 2.5'])
         wr.writerows(total_data)

        
    
  
        
        
    
