import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import random
import statistics as st

df=pd.read_csv("pro111.csv")
data = df["reading_time"].tolist()

def RandomSet(counter):
    dataSet=[]
    for i in range(0, counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)

    mean=st.mean(dataSet)
    return mean

def ShowFig(meanList):
    df = meanList
    mean = st.mean(df)
    fig=ff.create_distplot([df], ["result"], show_hist=False)
    fig.show()


meanList=[]
for i in range(0,100):
    setOfMeans = RandomSet(30)
    meanList.append(setOfMeans)

ShowFig(meanList)
mean=st.mean(meanList)
sd=st.stdev(meanList)


sd1start, sd1end = mean-sd, mean+sd
sd2start, sd2end = mean-(2*sd), mean+(2*sd)
sd3start, sd3end = mean-(3*sd), mean+(3*sd)

fig=ff.create_distplot([meanList], ["Result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[sd1start,sd1start],y=[0,0.17],mode="lines",name="SD1"))
fig.add_trace(go.Scatter(x=[sd1end,sd1end],y=[0,0.17],mode="lines",name="SD1"))
fig.add_trace(go.Scatter(x=[sd2start,sd2start],y=[0,0.17],mode="lines",name="SD2"))
fig.add_trace(go.Scatter(x=[sd2end,sd2end],y=[0,0.17],mode="lines",name="SD2"))
fig.add_trace(go.Scatter(x=[sd3start,sd3start],y=[0,0.17],mode="lines",name="SD3"))
fig.add_trace(go.Scatter(x=[sd3end,sd3end],y=[0,0.17],mode="lines",name="SD3"))

fig.show()


