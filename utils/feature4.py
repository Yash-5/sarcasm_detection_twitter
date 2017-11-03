import nltk

def familiarityLanguage(words,back_data):
    num_hashtags =0 
    total_words =0 
    dict1 = { }
    dict2 = {'CC' : 0 ,	'CD' : 0 ,'DT' : 0 ,'EX' : 0 ,'FW' : 0 ,'IN' : 0 ,'JJ' : 0 ,'JJR' : 0 ,'JJS' : 0 , 'LS' : 0 ,\
    'MD' : 0 ,'NN' : 0 ,'NNS' : 0 ,	'NNP' : 0 , 'NNPS' : 0 ,'PDT' : 0 ,'POS' : 0 ,	'PRP' : 0 , 'PRP$' : 0 ,'RB' : 0 ,\
    'RBR' : 0 , 'RBS' : 0 , 'RP' : 0 ,'SYM' : 0 ,'TO' : 0 , 'UH' : 0 ,'VB' : 0 ,'VBD' : 0 ,	 'VBG' : 0 ,'VBN' : 0 ,'VBP' : 0 ,\       'VBZ' : 0 , 'WDT' : 0 , 'WP' : 0 , 'WP$' : 0 ,'WRB' : 0 }
    features = []
    num_not = 0
    distinct_words=0
    for i in back_data:
        total_words = total_words + len(i)
        for j in i:
            if(j[0]=='#'):
                num_hashtags += 1
            if j not in dict1:
                dict1[j] = 1
                distinct_words += 1
            dict2[nltk.pos_tag(nltk.word_tokenize(j))[0][1]] = dict2[nltk.pos_tag(nltk.word_tokenize(j))[0][1]] + 1
    for i in dict2.keys():
        dict2[i] = dict2[i] / total_words
        features.append(dict2[i])
    ratio = distinct_words / total_words
    features.append(total_words)
    features.append(distinct_words)
    features.append(ratio)
    features.append(num_not)
    features.append(num_hashtags)
    return features