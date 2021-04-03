import matplotlib.pyplot as plt
import pandas as pd
import datetime

data=pd.read_csv('SolarPrediction.csv')
data.Data=pd.to_datetime(data.Data, utc= True)

data.Time = (pd.to_datetime(data.Time, format='%H:%M:%S')- datetime.datetime(1900, 1, 1)).dt.total_seconds()
data.TimeSunRise = (pd.to_datetime(data.TimeSunRise, format='%H:%M:%S')- datetime.datetime(1900, 1, 1)).dt.total_seconds()
data.TimeSunSet = (pd.to_datetime(data.TimeSunSet, format='%H:%M:%S') - datetime.datetime(1900, 1, 1)).dt.total_seconds()

unix_time = data.loc[:,'UNIXTime'].values #секунды с 1 января 1970 года
date = data.loc[:,'Data'].values #дата в формате yyyy-mm-dd
time = data.loc[:,'Time'].values #локальное время (секунды с начала дня)
radiation = data.loc[:,'Radiation'].values #Вт/м2
temperature = data.loc[:,'Temperature'].values #градусы Фаренгейта
pressure = data.loc[:,'Pressure'].values #атмосферное давление в дюймах ртутного столба
humidity = data.loc[:,'Humidity'].values #влажность в процентах
wind_direction = data.loc[:,'WindDirection(Degrees)'].values #направление ветра в градусах
speed = data.loc[:,'Speed'].values #мили в час
time_sunrise=data.loc[:,'TimeSunRise'].values #гавайское время (секунды с начала дня)
time_sunset=data.loc[:,'TimeSunSet'].values #гавайское время (секунды с начала дня)
data['λ']=(speed*pressure)/radiation
l= data.loc[:, 'λ'].values

start_date = pd.to_datetime('9/01/2016', utc=True)
end_date = pd.to_datetime('9/30/2016', utc=True)
september = data.loc[(data['Data'] >= start_date) & (data['Data'] <= end_date)]  # выборка за сентябрь

start_date = pd.to_datetime('10/01/2016', utc=True)
end_date = pd.to_datetime('10/31/2016', utc=True)
october = data.loc[(data['Data'] >= start_date) & (data['Data'] <= end_date)]  # выборка за октябрь

start_date = pd.to_datetime('11/01/2016', utc=True)
end_date = pd.to_datetime('11/30/2016', utc=True)
november = data.loc[(data['Data'] >= start_date) & (data['Data'] <= end_date)]  # выборка за ноябрь

start_date = pd.to_datetime('12/01/2016', utc=True)
end_date = pd.to_datetime('12/30/2016', utc=True)
december = data.loc[(data['Data'] >= start_date) & (data['Data'] <= end_date)]  # выборка за декабрь


if __name__ == '__main__':

    fig,ax= plt.subplots()
    ax.grid(True)
    #ax.scatter(x=temperature,y=λ, c='black')
    ax.plot(unix_time, l, c='black')
    figManager = plt.get_current_fig_manager()
    figManager.window.state('zoomed')
    plt.show()

    ###############
    sep_unix_time = september.loc[:,'UNIXTime'].values #секунды с 1 января 1970 года
    sep_l= september.loc[:,'λ'].values

    fig,ax= plt.subplots()
    ax.grid(True)
    #ax.scatter(x=sep_temperature,y=sep_λ, c='green')
    ax.plot(sep_unix_time, sep_l, c='green')
    figManager = plt.get_current_fig_manager()
    figManager.window.state('zoomed')
    plt.show()
    ##########################

    ##########################
    oct_unix_time = october.loc[:, 'UNIXTime'].values  # секунды с 1 января 1970 года
    oct_l=october.loc[:,'λ'].values

    fig,ax= plt.subplots()
    ax.grid(True)
    #ax.scatter(x=oct_temperature,y=oct_l, c='red')
    ax.plot(oct_unix_time,oct_l,c='red')
    figManager = plt.get_current_fig_manager()
    figManager.window.state('zoomed')
    plt.show()
    ##########################

    ##########################
    nov_unix_time = november.loc[:,'UNIXTime'].values #секунды с 1 января 1970 года
    nov_l=november.loc[:,'λ'].values

    fig,ax= plt.subplots()
    ax.grid(True)
    #ax.scatter(x=nov_temperature,y=nov_l, c='grey')
    ax.plot(nov_unix_time,nov_l,c='grey')
    figManager = plt.get_current_fig_manager()
    figManager.window.state('zoomed')
    plt.show()
    ##########################

    ##########################
    dec_unix_time = december.loc[:,'UNIXTime'].values #секунды с 1 января 1970 года
    dec_l=december.loc[:,'λ'].values

    fig,ax= plt.subplots()
    ax.grid(True)
    #ax.scatter(x=dec_temperature,y=dec_l, c='blue')
    ax.plot(dec_unix_time,dec_l,c='blue')
    figManager = plt.get_current_fig_manager()
    figManager.window.state('zoomed')
    plt.show()


    '''
    графики внутри дня (288 точек)
    '''

