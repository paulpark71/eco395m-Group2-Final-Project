import re

def clean_words_function(word):
    '''
    Input: tokenized words
    Output: clean words
    '''
    wordslist =[]
    wordslist = word
    for i,e in enumerate(wordslist):
        wordslist[i]=wordslist[i].lower()
        wordslist[i]=re.sub('^[a-zA-Z0-9!-’-!-!@#$^_:,.]$','', wordslist[i])
        wordslist[i]=re.sub('\s+', ' ', wordslist[i])
    return wordslist
