from .load_stopwords import load_stopwords
from .clean_words_function import clean_words_function

import nltk
nltk.download(['punkt'])
from nltk.tokenize import word_tokenize

import gender_guesser.detector as gender
ge=gender.Detector()

All_wordsFiltered = []
wordsFiltered = []
wordsFiltered_each=dict()
words_dict = dict()
gender=dict({'male':[],
            'mostly_male':[],
            'female':[],
            'mostly_female':[],
            'andy':[],
            'unknown':[]
            })

key =""


    
def tokenized_without_stopwords(dataset,Stopwords_Path, Additional_Stopwords_Path ):
    '''
        Input: dataset, dictionary of stopwords path, that of additional stopwords path
        Ouput: dataset on tokenized without stopwords
    '''
    for i,e in enumerate(dataset['review_text']):
        if e=="":
            dataset['review_text'][i]= ""
    dataset =dataset.dropna(subset = ['review_text']).reset_index(drop=True)
    stopwords = load_stopwords(Stopwords_Path,Additional_Stopwords_Path)

    for i,e in enumerate(dataset['review_text']):
        wordsFiltered = []
        words = word_tokenize(e)
        clean_words = clean_words_function(words) 

        for w in clean_words:
            if w not in stopwords:
                wordsFiltered.append(w) 
        wordsFiltered = list(filter(None,wordsFiltered))
        if i==0:
            All_wordsFiltered = []
        else:
            All_wordsFiltered.extend(wordsFiltered.copy())

        if i == 0 or key is not dataset['place_id'][i]:
            wordsFiltered_each[dataset['place_id'][i]]=[]
            wordsFiltered_each[dataset['place_id'][i]].extend(wordsFiltered.copy())
            key=dataset['place_id'][i]
        else:
            wordsFiltered_each[dataset['place_id'][i]].extend(wordsFiltered.copy())
        each_gender = ge.get_gender(dataset['author_title'][i].split()[0])
        gender[each_gender].extend(wordsFiltered.copy())


        print(f"\r\033[K#{i+1}/"+str(len(dataset['review_text'])), end="")

    return [All_wordsFiltered,wordsFiltered_each,gender]
