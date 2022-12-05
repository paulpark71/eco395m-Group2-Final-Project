import pandas as pd
import nltk
import numpy as np
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
vader_analyzer = SentimentIntensityAnalyzer()

def sentiment_analysis(dataset):
    sentences=[]
    result = []
    for i,e in enumerate(dataset['review_text']):
        try:
            sentences.append([dataset['place_id'][i],e])
        except:
            pass
    for i,s in enumerate(sentences):
        try:
            score = vader_analyzer.polarity_scores(s[1])
            score['place_id'] = sentences[i][0]
            result.append(score)
        except:
            score = dict({'neg': np.nan, 'neu': np.nan, 'pos': np.nan, 'compound': np.nan})
            score['place_id'] = sentences[i][0]
            result.append(score)