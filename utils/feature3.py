import numpy as np
import math

def affectSentiment(words, affectdict, sentidict):
    arr_affect = []
    arr_senti = []
    for i in range(9):
        arr_affect.append(0)
    for i in range(11):
        arr_senti.append(0) 
    sum1=0
    sum2=0

    for i in words:
        if i in affectdict:
            arr_affect[int(affectdict[i])] = arr_affect[int(affectdict[i])] + 1
            sum1 = sum1 + 1 
        if i in sentidict:
            arr_senti[int(sentidict[i]) + 5] = arr_senti[int(sentidict[i]) + 5] + 1
            sum2 = sum2 + 1
    for i in range(9):
        try:
            arr_affect[i] = (arr_affect[i]*1.0)/sum1
        except:
            arr_affect[i] = 0

    for i in range(11):
        try:
            arr_senti[i] = (arr_senti[i]*1.0)/sum2
        except:
            arr_senti[i]=0

    feature = []
    feature.append(np.mean(arr_affect))
    feature.append(np.median(arr_affect))
    feature.append(min(arr_affect))
    feature.append(max(arr_affect))
    feature.append(np.std(arr_affect))
    feature.append(np.mean(arr_senti))
    feature.append(np.median(arr_senti))
    feature.append(min(arr_senti))
    feature.append(max(arr_senti))
    feature.append(np.std(arr_senti))
    feature.append(sum1)
    feature.append(sum2)
    #print feature
    return feature