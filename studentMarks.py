import pandas as pd
import plotly.figure_factory as pff
import plotly.graph_objects as pgo
import random
import statistics

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()
finalList = []
populationmean = statistics.mean(data)
populationstd = statistics.stdev(data)
print(populationmean,"Population Mean")
print(populationstd,"Population Standard Deviation")

def datapoints():
    sampledata = []
    for i in range(0,100):
        datapos = random.randint(0,len(data)-1)
        val = data[datapos]
        sampledata.append(val)
    mean = statistics.mean(sampledata)
    finalList.append(mean)

for i in range(0,1000):
    datapoints()

samplemean = statistics.mean(finalList)
samplestd = statistics.stdev(finalList)
print(samplemean,"Sample Mean")
print(samplestd,"Sample Standard Deviation")

#Finding 1st 2nd & 3rd std
fstartingStd = samplemean - samplestd
fendingStd = samplemean + samplestd
sstartingStd = samplemean - (2*samplestd)
sendingStd = samplemean + (2*samplestd)
tendingStd = samplemean - (3*samplestd)
tendingStd = samplemean + (3*samplestd)

data1df = pd.read_csv("data1.csv")
data1 = data1df["Math_score"].tolist()
data1_mean = statistics.mean(data1)

graph = pff.create_distplot([finalList],["finalList"],show_hist=False)
graph.add_trace(pgo.Scatter(x=[data1_mean,data1_mean],y=[0,0.17],mode="lines",name="Mean of data1"))
graph.add_trace(pgo.Scatter(x=[fendingStd,fendingStd],y=[0,0.17],mode="lines",name="1st Standard Deviation"))
graph.add_trace(pgo.Scatter(x=[sendingStd,sendingStd],y=[0,0.17],mode="lines",name="2nd Standard Deviation"))
graph.add_trace(pgo.Scatter(x=[tendingStd,tendingStd],y=[0,0.17],mode="lines",name="3rd Standard Deviation"))
#graph.show()

zvalue = (data1_mean - samplemean)/samplestd
print(zvalue)

