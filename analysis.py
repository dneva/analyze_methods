import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

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

l=(speed*pressure)/radiation
print(l)
#print(data)
#print(data.dtypes)
#print(wind_direction)

fig,ax= plt.subplots(figsize=(25,15))
ax.grid(True)
ax.scatter(x=temperature,y=l, c='black')
plt.show()

###############
start_date = pd.to_datetime('9/01/2016', utc= True)
end_date = pd.to_datetime('9/30/2016', utc= True)
september=data.loc[(data['Data'] > start_date) & (data['Data'] < end_date)] #выборка за сентябрь

sep_unix_time = september.loc[:,'UNIXTime'].values #секунды с 1 января 1970 года
sep_date = september.loc[:,'Data'].values #дата в формате yyyy-mm-dd
sep_time = september.loc[:,'Time'].values #локальное время (секунды с начала дня)
sep_radiation = september.loc[:,'Radiation'].values #Вт/м2
sep_temperature = september.loc[:,'Temperature'].values #градусы Фаренгейта
sep_pressure = september.loc[:,'Pressure'].values #атмосферное давление в дюймах ртутного столба
sep_humidity = september.loc[:,'Humidity'].values #влажность в процентах
sep_wind_direction = september.loc[:,'WindDirection(Degrees)'].values #направление ветра в градусах
sep_speed = september.loc[:,'Speed'].values #мили в час
sep_time_sunrise=september.loc[:,'TimeSunRise'].values #гавайское время (секунды с начала дня)
sep_time_sunset=september.loc[:,'TimeSunSet'].values #гавайское время (секунды с начала дня)
sep_l=(sep_speed*sep_pressure)/sep_radiation

fig,ax= plt.subplots(figsize=(25,15))
ax.grid(True)
ax.scatter(x=sep_temperature,y=sep_l, c='green')
plt.show()
##########################
##########################
start_date = pd.to_datetime('10/01/2016', utc= True)
end_date = pd.to_datetime('10/31/2016', utc= True)
october=data.loc[(data['Data'] > start_date) & (data['Data'] < end_date)] #выборка за октябрь

oct_unix_time = october.loc[:,'UNIXTime'].values #секунды с 1 января 1970 года
oct_date = october.loc[:,'Data'].values #дата в формате yyyy-mm-dd
oct_time = october.loc[:,'Time'].values #локальное время (секунды с начала дня)
oct_radiation = october.loc[:,'Radiation'].values #Вт/м2
oct_temperature = october.loc[:,'Temperature'].values #градусы Фаренгейта
oct_pressure = october.loc[:,'Pressure'].values #атмосферное давление в дюймах ртутного столба
oct_humidity = october.loc[:,'Humidity'].values #влажность в процентах
oct_wind_direction = october.loc[:,'WindDirection(Degrees)'].values #направление ветра в градусах
oct_speed = october.loc[:,'Speed'].values #мили в час
oct_time_sunrise=october.loc[:,'TimeSunRise'].values #гавайское время (секунды с начала дня)
oct_time_sunset=october.loc[:,'TimeSunSet'].values #гавайское время (секунды с начала дня)
oct_l=(oct_speed*oct_pressure)/oct_radiation

fig,ax= plt.subplots(figsize=(25,15))
ax.grid(True)
ax.scatter(x=oct_temperature,y=oct_l, c='red')
plt.show()
##########################
##########################
start_date = pd.to_datetime('11/01/2016', utc= True)
end_date = pd.to_datetime('11/30/2016', utc= True)
november=data.loc[(data['Data'] > start_date) & (data['Data'] < end_date)] #выборка за ноябрь

nov_unix_time = november.loc[:,'UNIXTime'].values #секунды с 1 января 1970 года
nov_date = november.loc[:,'Data'].values #дата в формате yyyy-mm-dd
nov_time = november.loc[:,'Time'].values #локальное время (секунды с начала дня)
nov_radiation = november.loc[:,'Radiation'].values #Вт/м2
nov_temperature = november.loc[:,'Temperature'].values #градусы Фаренгейта
nov_pressure = november.loc[:,'Pressure'].values #атмосферное давление в дюймах ртутного столба
nov_humidity = november.loc[:,'Humidity'].values #влажность в процентах
nov_wind_direction = november.loc[:,'WindDirection(Degrees)'].values #направление ветра в градусах
nov_speed = november.loc[:,'Speed'].values #мили в час
nov_time_sunrise=november.loc[:,'TimeSunRise'].values #гавайское время (секунды с начала дня)
nov_time_sunset=november.loc[:,'TimeSunSet'].values #гавайское время (секунды с начала дня)
nov_l=(nov_speed*nov_pressure)/nov_radiation

fig,ax= plt.subplots(figsize=(25,15))
ax.grid(True)
ax.scatter(x=oct_temperature,y=oct_l, c='grey')
plt.show()
##########################
##########################
start_date = pd.to_datetime('9/01/2016', utc= True)
end_date = pd.to_datetime('9/30/2016', utc= True)
december=data.loc[(data['Data'] > start_date) & (data['Data'] < end_date)] #выборка за декабрь

nov_unix_time = november.loc[:,'UNIXTime'].values #секунды с 1 января 1970 года
nov_date = november.loc[:,'Data'].values #дата в формате yyyy-mm-dd
nov_time = november.loc[:,'Time'].values #локальное время (секунды с начала дня)
nov_radiation = november.loc[:,'Radiation'].values #Вт/м2
nov_temperature = november.loc[:,'Temperature'].values #градусы Фаренгейта
nov_pressure = november.loc[:,'Pressure'].values #атмосферное давление в дюймах ртутного столба
nov_humidity = november.loc[:,'Humidity'].values #влажность в процентах
nov_wind_direction = november.loc[:,'WindDirection(Degrees)'].values #направление ветра в градусах
nov_speed = november.loc[:,'Speed'].values #мили в час
nov_time_sunrise=november.loc[:,'TimeSunRise'].values #гавайское время (секунды с начала дня)
nov_time_sunset=november.loc[:,'TimeSunSet'].values #гавайское время (секунды с начала дня)
nov_l=(nov_speed*nov_pressure)/nov_radiation

#x = np.arange(3)
#print(*data.head())
#plt.bar(*data.head(),radiation)
#plt.show()