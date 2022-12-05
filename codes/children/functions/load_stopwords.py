import re


def load_stopwords(Stopwords_Path, Additional_Stopwords_Path):
    '''
    Input: Stoprwords_path and Additional_Stopwords_path
    Ouput: Stopwords(data)
    '''
    '''1. Stopwords file'''
    with open(Stopwords_Path, 'r',encoding='utf8') as file:
        liststopword=file.readlines()
    for i,e in enumerate(liststopword):
        if '\n' in e:
            liststopword[i]=e.replace('\n','')
        liststopword[i]=liststopword[i].lower()
        liststopword[i]=re.sub('[^A-Za-z\s]', '', liststopword[i])
        liststopword[i] = re.sub('\s+', ' ', liststopword[i])
    stopwords = liststopword

    '''2. Additional Stopwords file'''
    with open(Additional_Stopwords_Path, 'r',encoding='utf8') as file:
        additional_words=file.readlines()
    for i,e in enumerate(additional_words):
        if '\n' in e:
            additional_words[i]=e.replace('\n','')
        additional_words[i]=additional_words[i].lower()
        additional_words[i]=re.sub('^[a-zA-Z0-9!-!@#$^_:,.]$', '', additional_words[i])
        additional_words[i] = re.sub('\s+', ' ', additional_words[i]) 
    stopwords.extend(additional_words)
    
    return stopwords
