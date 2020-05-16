import pandas as pd 
import matplotlib.pyplot as plt


def avg_data(Year):
    
    temp_i=0
    average=[]
    #data is on hourly basis so calculate average of each day 24
    for rows in pd.read_csv('Data/AQI/aqi{}.csv'.format(Year),chunksize=24):
        add_val=0
        avg=0.0
        data=[]
        
        # only PM2.5 column is stored in data
        for index,row in rows.iterrows():
            data.append(row['PM2.5'])

        #calculating average per day i.e 24 rows 
        for value in data:
            if type(value) is float or type(value) is int:
                add_val+=value

            elif type(value) is str:
                if value not  in ['NoData','PwrFail','---','InVld']:
                    add_val+=float(value)
                    
        avg=add_val/24 
        average.append(avg)
        temp_i+=1
    
    return average 


if __name__=="__main__":

   #storing records     
    lst_2013=avg_data(2013)
    lst_2014=avg_data(2014)
    lst_2015=avg_data(2015)
    lst_2016=avg_data(2016)
    lst_2017=avg_data(2017)
    lst_2018=avg_data(2018)
    
    plt.plot(range(0,365),lst_2013,label="2013 data")
    plt.plot(range(0,364),lst_2014,label="2014 data")

    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()
