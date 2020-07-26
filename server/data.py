import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random
import math
import time
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error
import datetime
import operator
from flask import Flask, jsonify

import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)

plt.style.use('fivethirtyeight')
#%matplotlib inline

confirmedCases = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
#confirmedCases.head()
deathsReported = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
#deathsReported.head()
recoveredCases = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
#recoveredCases.head()
latestData = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/07-24-2020.csv')
#latestData.head()

cols = confirmedCases.keys()

confirmed = confirmedCases.loc[:, cols[4]:cols[-1]]
deaths = deathsReported.loc[:, cols[4]:cols[-1]]
recoveries = recoveredCases.loc[:, cols[4]:cols[-1]]

dates = confirmed.keys()

worldCases = []
totalDeaths = []
mortalityRate = []
recoveryRate = []
totalRecovered = []
totalActive = []

usaC=[]
brazilC=[]
indiaC=[]
russiaC=[]
southafricaC=[]
peruC=[]
mexicoC=[]
chileC=[]
spainC=[]
ukC=[]

usaD=[]
brazilD=[]
indiaD=[]
russiaD=[]
southafricaD=[]
peruD=[]
mexicoD=[]
chileD=[]
spainD=[]
ukD=[]

usaR=[]
brazilR=[]
indiaR=[]
russiaR=[]
southafricaR=[]
peruR=[]
mexicoR=[]
chileR=[]
spainR=[]
ukR=[]

for i in dates:
    confirmedSum = confirmed[i].sum()
    deathSum = deaths[i].sum()
    recoveredSum = recoveries[i].sum()

    worldCases.append(confirmedSum)
    totalDeaths.append(deathSum)
    totalRecovered.append(recoveredSum)
    totalActive.append(confirmedSum-deathSum)

    mortalityRate.append(deathSum/confirmedSum)
    recoveryRate.append(recoveredSum/confirmedSum)

    usaC.append(confirmedCases['Country']=='USA'[i].sum())
    brazilC.append(confirmedCases['Country']=='Brazil'[i].sum())
    indiaC.append(confirmedCases['Country']=='India'[i].sum())
    russiaC.append(confirmedCases['Country']=='Russia'[i].sum())
    southafricaC.append(confirmedCases['Country']=='South Africa'[i].sum())
    peruC.append(confirmedCases['Country']=='Peru'[i].sum())
    mexicoC.append(confirmedCases['Country']=='Mexico'[i].sum())
    chileC.append(confirmedCases['Country']=='Chile'[i].sum())
    spainC.append(confirmedCases['Country']=='Spain'[i].sum())
    ukC.append(confirmedCases['Country']=='UK'[i].sum())
    
    usaD.append(confirmedCases['Country']=='USA'[i].sum())
    brazilD.append(confirmedCases['Country']=='Brazil'[i].sum())
    indiaD.append(confirmedCases['Country']=='India'[i].sum())
    russiaD.append(confirmedCases['Country']=='Russia'[i].sum())
    southafricaD.append(confirmedCases['Country']=='South Africa'[i].sum())
    peruD.append(confirmedCases['Country']=='Peru'[i].sum())
    mexicoD.append(confirmedCases['Country']=='Mexico'[i].sum())
    chileD.append(confirmedCases['Country']=='Chile'[i].sum())
    spainD.append(confirmedCases['Country']=='Spain'[i].sum())
    ukD.append(confirmedCases['Country']=='UK'[i].sum())

    usaR.append(confirmedCases['Country']=='USA'[i].sum())
    brazilR.append(confirmedCases['Country']=='Brazil'[i].sum())
    indiaR.append(confirmedCases['Country']=='India'[i].sum())
    russiaR.append(confirmedCases['Country']=='Russia'[i].sum())
    southafricaR.append(confirmedCases['Country']=='South Africa'[i].sum())
    peruR.append(confirmedCases['Country']=='Peru'[i].sum())
    mexicoR.append(confirmedCases['Country']=='Mexico'[i].sum())
    chileR.append(confirmedCases['Country']=='Chile'[i].sum())
    spainR.append(confirmedCases['Country']=='Spain'[i].sum())
    ukR.append(confirmedCases['Country']=='UK'[i].sum())

    def dailyIncrease(data):
        d=[]
        for i in range(len(data)):
            if i==0:
                d.append(data[0])
            else:
                d.append(data[i]-data[i-1])
        return d

worldDailyIncrease = dailyIncrease(worldCases)
usaDailyIncrease = dailyIncrease(worldCases)
brazilDailyIncrease = dailyIncrease(worldCases)
indiaDailyIncrease = dailyIncrease(worldCases)
russiaDailyIncrease = dailyIncrease(worldCases)
southafricaDailyIncrease = dailyIncrease(worldCases)
peruDailyIncrease = dailyIncrease(worldCases)
mexicoDailyIncrease = dailyIncrease(worldCases)
chileDailyIncrease = dailyIncrease(worldCases)
spainDailyIncrease = dailyIncrease(worldCases)
ukDailyIncrease = dailyIncrease(worldCases)

worldDailyDeath = dailyIncrease(totalDeaths)
usaDailyDeath = dailyIncrease(totalDeaths)
brazilDailyDeath = dailyIncrease(totalDeaths)
indiaDailyDeath = dailyIncrease(totalDeaths)
russiaDailyDeath = dailyIncrease(totalDeaths)
southafricaDailyDeath = dailyIncrease(totalDeaths)
peruDailyDeath = dailyIncrease(totalDeaths)
mexicoDailyDeath = dailyIncrease(totalDeaths)
chileDailyDeath = dailyIncrease(totalDeaths)
spainDailyDeath = dailyIncrease(totalDeaths)
ukDailyDeath = dailyIncrease(totalDeaths)

worldDailyRecovery = dailyIncrease(totalRecovered)
usaDailyRecovery = dailyIncrease(totalRecovered)
brazilDailyRecovery = dailyIncrease(totalRecovered)
indiaDailyRecovery = dailyIncrease(totalRecovered)
russiaDailyRecovery = dailyIncrease(totalRecovered)
southafricaDailyRecovery = dailyIncrease(totalRecovered)
peruDailyRecovery = dailyIncrease(totalRecovered)
mexicoDailyRecovery = dailyIncrease(totalRecovered)
chileDailyRecovery = dailyIncrease(totalRecovered)
spainDailyRecovery = dailyIncrease(totalRecovered)
ukDailyRecovery = dailyIncrease(totalRecovered)

uniqueCountries = list(latestData['Country'].unique())
countryConfirmedCases = []
countryDeathCases=[]
countryActiveCases=[]
countryRecoveryCases=[]
countryMortalityRate=[]

noCases = []

for i in uniqueCountries:
    cases = latestData[latestData['Country']==i]['Confirmed'].sum()
    if cases>0:
        countryConfirmedCases.append(cases)
    else:
        noCases.append(i)

for i in noCases:
    uniqueCountries.remove(i)

#----------------------------------------------------------------------------------------

# uniqueCountries = [k for k, v in sorted(zip(uniqueCountries, countryConfirmedCases), key=operator.itemgetter(1), reverse=True)]

# for i in range(len(uniqueCountries)):
#     countryConfirmedCases[i]=latestData[latestData['Country']==uniqueCountries[i]]['Confirmed'].sum()
#     countryDeathCases.append=latestData[latestData['Country']==uniqueCountries[i]]['Deaths'].sum()
#     countryRecoveryCases.append=latestData[latestData['Country']==uniqueCountries[i]]['Recovered'].sum()
#     countryActiveCases.append(countryConfirmedCases[i] - countryDeathCases[i] - countryRecoveryCases[i])
#     countryMortalityRate.append(countryDeathCases[i]/countryConfirmedCases[i])

# countryDf = pd.DataFrame({'Country Name': uniqueCountries, 'Number of Confirmed Cases': countryConfirmedCases, 'Number of Deaths': countryDeathCases, 'Number of Recoveries': countryRecoveryCases, 'Number of Active Cases': countryActiveCases, 'Mortality Rate': countryMortalityRate})
# countryDf.style.background_gradient(cmap='Reds')

#-----------------------------------------------------------------------------------------


#show 10 countries with the most confirmed cases, rest are grouped into other category
# visualUniqueCountries=[]
# visualConfirmedCases=[]
# others = np.sum(countryConfirmedCases[:10])

# for i in range(len(countryConfirmedCases[:10])):
#     visualUniqueCountries.append(uniqueCountries[i])
#     visualConfirmedCases.append(countryConfirmedCases[i])

# visualUniqueCountries.append('Others')
# visualConfirmedCases.append(others)

# def plotBarGraphs(x, y, title):
#     plt.figure(figsize=(16, 9))
#     plt.barh(x,y)
#     plt.title(title, size=20)
#     plt.xticks(size=20)
#     plt.yticks(size=20)
#     plt.show()

# plotBarGraphs(visualUniqueCountries, visualConfirmedCases, 'Number of COVID-19 Cases in Top 10 Countries')


daysFromJan22 = np.array([i for i in range(len(dates))]).reshape(-1,1)
worldCases=np.array(worldCases).reshape(-1,1)
totalDeaths=np.array(totalDeaths).reshape(-1,1)
totalRecovered=np.array(totalRecovered).reshape(-1,1)

daysInFuture = 20
futureForecast=np.array([i for i in range(len(dates)+daysInFuture)]).reshape(-1,1)
adjustedDates = futureForecast[:-20]

start='1/22/2020'
startDate= datetime.datetime.strptime(start, '%m/%d/%Y')

futureForecastDates = []

for i in range(len(futureForecast)):
    futureForecastDates.append((startDate + datetime.timedelta(days=i)).strftime('%m/%d/%Y'))


xtrainconf, xtestconf, ytrainconf, ytestconf = train_test_split(daysFromJan22, worldCases, test_size = 0.25, shuffle= False)

#transforming data for polynomial regression
poly = PolynomialFeatures(degree=3)
polyxtrainconf=poly.fit_transform(xtrainconf)
polyxtestconf=poly.fit_transform(xtestconf)
polyfutureforecast = poly.fit_transform(futureForecast)

#polynomial regression
linearModel = LinearRegression(normalize=True, fit_intercept=False)
linearModel.fit(polyxtrainconf, ytrainconf)
testLinearPred=linearModel.predict(polyfutureforecast)
# print('MAE:', mean_absolute_error(testLinearPred, ytestconf))
# print('MAE:', mean_squared_error(testLinearPred, ytestconf))

# plt.plot(ytestconf)
# plt.plot(testLinearPred)
# plt.legend(['Test Data', 'Polynomial Regression Predictions'])
# #here should print a graph

# svmConf = SVR(shrinking=True, kernel='poly', gamma=0.01, epsilon=1, degree=5, C=0.1)
# svmConf.fit(xtrainconf, ytrainconf)
# svmpred = svmConf.predict(futureForecast)

# svmTestPred = svmConf.predict(xtestconf)
# plt.plot(ytestconf)
# plt.plot(svmTestPred)
# plt.legend(['Test Data', 'SVM Predictions'])
# print('MAE:', mean_absolute_error(svmTestPred, ytestconf))
# print('MAE:', mean_squared_error(svmTestPred, ytestconf))
# #here should print a graph

adjustedDates=adjustedDates.reshape(1, -1)[0]

# plt.figure(figsize=(16,9))
# plt.plot(adjustedDates, worldCases)
# plt.title('Number of COVID-19 Cases Over Time', size=30)
# plt.xlabel('Days Since 1/22/2020', size=30)
# plt.ylabel('Number of Cases', size=30)
# plt.xticks(size=20)
# plt.yticks(size=20)
# plt.show()

# plt.figure(figsize=(16,9))
# plt.plot(adjustedDates, totalDeaths)
# plt.title('Number of COVID-19 Deaths Over Time', size=30)
# plt.xlabel('Days Since 1/22/2020', size=30)
# plt.ylabel('Number of Cases', size=30)
# plt.xticks(size=20)
# plt.yticks(size=20)
# plt.show()

def plotPredictions(x,y,pred,algo,color):
    #fig = Figure()
    plt.figure(figsize=(16,9))
    plt.plot(x,y)
    plt.plot(futureForecast, pred, linestyle='dashed', color=color)
    plt.title('Number of COVID-19 Cases Over Time', size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('Number of Cases', size=30)
    plt.legend(['Confirmed Cases', algo], prop={'size': 20})
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.savefig('plot.png')
    #return fig

plotPredictions(adjustedDates, worldCases, testLinearPred, 'Predicted', 'red')
#plotPredictions(adjustedDates, worldCases, linearPred, 'SVM Predictions', 'purple')

# testLinearPred = testLinearPred.reshape(1, -1)[0]
# polydf = pd.DataFrame({'Date': futureForecastDates[-20:], 'Predicted number of Confirmed Cases Worldwide': np.round(testLinearPred, decimals=0, out=None)})


@app.route('/plot.png')
def plot_png():
    fig = plt.figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run()
