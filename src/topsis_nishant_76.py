import pandas as pd
import numpy as np
import math
import scipy.stats as ss
def topsis_nish(incsv_filename,weights,ff):
    file = open(incsv_filename,'rb')
    ww =weights
    w=ww.split(",")
    w=list(map(int, w))
    f = ff
    f=f.split(",") 
    s2=[]
    df=pd.read_csv(file)
    name=df.iloc[:,0]
    data=df.iloc[:,1:].values.astype('float64')
    rows=data.shape[0]
    cols=data.shape[1]
    for i in range(0,cols):
        sum1=0
        for j in range(0,rows):
            sum1=sum1+(data[j][i]*data[j][i])
        sum1=math.sqrt(sum1)
        s2.append(sum1)
    sum2=0
    for i in range(0,cols):
        sum2=sum2+w[i]
    for i in range(0,cols):
        w[i]=w[i] /sum2
    for i in range(0,cols):
        for j in range(0,rows):
            data[j][i]=(data[j][i]/s2[i])*w[i]
    best=[]
    worst=[]
    for i in range(0,cols):
        max2=-11111
        min2=111110
        for j in range(0,rows):
            if(data[j][i]>max2):
                max2=data[j][i]
            if(data[j][i]<min2):
                min2=data[j][i]
        if(f[i]=='+'):
            best.append(max2)
            worst.append(min2)
        elif(f[i]=='-'):
            best.append(min2)
            worst.append(max2)
    sip=[]
    sin=[]
    for i in range(0,rows):
        sumsip=0
        sumsin=0
        for j in range(0,cols):
            sumsip=sumsip+(data[i][j]-best[j])*(data[i][j]-best[j])
            sumsin=sumsin+(data[i][j]-worst[j])*(data[i][j]-worst[j])
        sip.append(math.sqrt(sumsip))
        sin.append(math.sqrt(sumsin))
    p=[]
    for i in range(0,rows):
        p.append(sin[i]/(sip[i]+sin[i]))
    print("The rankings of the objects  are :{}".format(len(p)-ss.rankdata(p)+1))
    ans=np.max(p)
    for i in range(0,len(p)):
        if p[i] == ans:
            ind=i
    print("Best Performance Object is : ",name[ind])
