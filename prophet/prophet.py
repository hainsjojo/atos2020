import pandas as pd
import os
from fbprophet import Prophet
from matplotlib import pyplot as plt
dfData=pd.read_csv('dataset.csv')
df=pd.read_csv('dataset.csv')
future = df.tail(1000)
future = future.drop('y', axis=1)
#drop last 1000 value from the actuals
df.drop(df.tail(1000).index,inplace=True)
m = Prophet(weekly_seasonality=False)
m.add_seasonality(name='hourly', period=1000, fourier_order=3)
m.fit(df) # Fit the model
forecast = m.predict(future)
#Plot the Forecast
m.plot(forecast)
plt.title("CrowdSurf 1000 Prediction")
plt.show() # To save the fig use plt.savefig(‘pred.png’)
dfForecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

yActual = dfData.tail(1000)['y'].values.tolist()

yPredicted = forecast['yhat'].values.tolist()
plt.plot(dfForecast.ds,yActual,dfForecast.ds,yPredicted)
plt.title("Forecasted Value vs Actuals")
plt.show() # To save the fig use plt.savefig(‘comp.png’)
forecast[['ds','yhat']].to_csv('predicted_raw.csv',sep=',',index=False)
os.system("cat predicted_raw.csv | cut -f1 -d'.' > predict.csv")
os.system('cp -r predict.csv /var/www/html')
os.system('rm predicted_raw.csv')
