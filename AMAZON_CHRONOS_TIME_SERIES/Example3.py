## STEP 0: LIBRARIES 
import yfinance as yf
import pandas as pd  
import torch
from chronos import ChronosPipeline
import matplotlib.pyplot as plt  
import numpy as np
import warnings
warnings.filterwarnings("ignore")

## STEP 1: FORECAST PIPELINE
pipeline = ChronosPipeline.from_pretrained(
    #"amazon/chronos-t5-small",
    "amazon/chronos-t5-large",
    device_map="cuda",  # "cpu" o "mps" para Apple Silicon
    torch_dtype=torch.bfloat16,
)

## STEP 2: LOAD DATA
msft = yf.Ticker("MSFT")
#print(msft.info)
hist = msft.history(period="2y").reset_index().rename(columns={'Date':'ds','Open':'y'})
hist['ds'] = hist['ds'].dt.strftime('%Y-%m-%d')
hist['cap']=hist.y.rolling(window=5).mean().fillna(method='bfill')*1.20
hist['floor']=hist.y.rolling(window=5).mean().fillna(method='bfill')*0.80

## STEP 3: PARAMETERS FOR PREDICTION
step_to_predict= 30
samples_to_consider= 50

#print(pipeline.predict.__doc__)

## STEP 4: FORECAST
forecast = pipeline.predict(
    context=torch.tensor(hist["y"]),
    prediction_length=step_to_predict,
    num_samples=samples_to_consider,
)

forecast_index = range(len(hist), len(hist) + step_to_predict)
low, median, high = np.quantile(forecast[0].numpy(), [0.1, 0.5, 0.9], axis=0)

## STEP 5: PLOT
plt.figure(figsize=(8, 4))
plt.plot(hist["y"], color="royalblue", label="historical data (MSFT)")
plt.plot(forecast_index, median, color="tomato", label="median forecast")
plt.fill_between(forecast_index, low, high, color="tomato", alpha=0.3, label="80% prediction interval")
plt.legend()
plt.grid()
plt.show()

