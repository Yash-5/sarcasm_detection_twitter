import nltk

def structuralVariations(words , affectdict , sentidict):
    feature = []
    tags = nltk.pos_tag(words)

    try:
        feature.append( tags[0][1] )
    except:
        feature.append('')
    
    try:
        feature.append( tags[1][1] )
    except:
        feature.append('')
    
    try:
        feature.append( tags[2][1] )
    except:
        feature.append('')
    
    try:
        feature.append( tags[len(words)-3][1] )
    except:
           feature.append('')
    
    try:
        feature.append( tags[len(words)-2][1] )
    except:
        feature.append('')
    
    try:
        feature.append( tags[len(words)-1][1] )
    except:
        feature.append('')

    flag=0
    for i in range (len(words)):
        if( words[i] in affectdict):
            feature.append(i+1)
            flag=1
            break
    if(flag==0):
        feature.append(0)
    
    flag=0
    for i in range (len(words)):
        if( words[i] in sentidict):
            feature.append(i+1)
            flag=1
            break
    if(flag==0):
        feature.append(0)


    hashtags_part1 =0 
    hashtags_part2=0
    hashtags_part3 =0

    for i in range(len(words)):
        if(words[i][0]=='#'):
            if(i< len(words)//3):
                hashtags_part1=hashtags_part1+1
            elif(i<( len(words)*2)//3): 
                hashtags_part2=hashtags_part2+1
            else:
                hashtags_part3=hashtags_part3+1 


    feature.append(hashtags_part1)
    feature.append(hashtags_part1)
    feature.append(hashtags_part1)
    return feature