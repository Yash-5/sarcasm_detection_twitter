import senti_utils

def getSentiStrength(w, sentidict):
    # sentidict acts as a cache. If word is not there, process that word and add it there
    if w not in sentidict:
        sentidict[w] = runsenti(w)[0]
    return sentidict[w]
        
def getAffect(w, affectdict):
    # Return the affect score if the word is there, else return 0
    if w in affectdict:
        return affectdict[w]
    else:
        for key,value in affectdict.iteritems():
            if key.startswith(w):
                return value
    return 0

def getBigrams(tokens):
    # create bigrams
    bigrams=[]
    c=0
    while c < len(tokens)-1:
        bigrams.append(tokens[c]+tokens[c+1])
        c=c+1
    return bigrams

def getTrigrams(tokens):
    # create trigrams
    trigrams=[]
    c=0
    while c < len(tokens)-2:
        trigrams.append(tokens[c]+tokens[c+1]+tokens[c+2])
        c=c+1
    return trigrams

def contrastingFeatures(words, affectdict, sentidict, bidict, tridict):
    # words is just the tweet given as a list of words
    affectscores = []
    sentiscores = []
    for w in words:
        # Get affect and sentiscores
        affectscores.append(getAffect(w, affectdict))
        sentiscores.append(getSentiStrength(w, sentidict))
    bigrams = getBigrams(words)
    trigrams = getTrigrams(words)
    # Positive and negative counts of bigrams and trigrams
    poscount=0
    possum=0
    negcount=0
    negsum=0
    for bi in bigrams:
        if bi in bidict:
            if bidict[bi]>0:
                possum += bidict[bi]
                poscount = poscount+1
            else:
                negsum += bidict[bi]
                negcount += 1
    for tri in trigrams:
        if tri in tridict:
            if tridict[tri]>0:
                possum += tridict[tri]
                poscount = poscount+1
            else:
                negsum += tridict[tri]
                negcount += 1

    # Return feature 1 according to paprt
    return [(max(affectscores) - min(affectscores)), (max(sentiscores)-min(sentiscores)), poscount, possum, negcount, negsum]