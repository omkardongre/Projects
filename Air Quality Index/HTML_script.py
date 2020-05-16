import os
import time
import requests #download the whole html
import sys
def retrival_html():
    path=os.getcwd()
    for year in range(2013,2019):

        for month in range(1,13):
            if month<10:
                url="https://en.tutiempo.net/climate/0{}-{}/ws-432950.html".format(month,year)
            else:
                 url="https://en.tutiempo.net/climate/{}-{}/ws-432950.html".format(month,year)
            
            texts=requests.get(url) # get the whole html
            # html text contain some unknown characters so need to convert into some standard format
            text_utf=texts.text.encode('utf=8') 
            if not os.path.exists('{}/Html_Data/{}'.format(path,year)):
                os.makedirs('{}/Html_Data/{}'.format(path,year))
                
            # with -> ensuring that a resource is properly released after use      
            with open('{}/Html_Data/{}/{}'.format(path,year,month),"wb") as output:
                output.write(text_utf)
            sys.stdout.flush()                

if __name__=="__main__":
    start_time=time.time()
    retrival_html()
    stop_time=time.time()
    print("Time Taken {}".format(stop_time-start_time))
    
     
