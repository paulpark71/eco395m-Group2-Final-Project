import os
import pandas as pd
from .functions.sentiment_analysis import sentiment_analysis
from .functions.review_gender import review_gender


BASE_DIR = 'artifacts'
Data_DIR = 'data'
Reveiws_CSV_PATH = os.path.join(Data_DIR, 'reviews.csv')
Count_integrated_CSV_PATH = os.path.join(BASE_DIR,'store', 'count_plus_basic.csv')
Sentimental_data_CSV_PATH = os.path.join(BASE_DIR,'store', 'sentimental_data.csv')
Summary_sentimental_PATH = os.path.join(BASE_DIR, 'senti_plus_count_basic.csv')
Reviewr_PATH = os.path.join(BASE_DIR, 'reviewer_r.csv')

dataset = pd.read_csv(Reveiws_CSV_PATH)
dd = sentiment_analysis(dataset)
df = review_gender(dataset)

mean = dd.groupby(['place_id']).mean()
mean.rename(columns = {'neg':'negative_mean','neu':'neutral_mean','pos':'positive_mean','compound':'compound_mean',},inplace=True)
std = dd.groupby(['place_id']).std()
std.rename(columns = {'neg':'negative_std','neu':'neutral_std','pos':'positive_std','compound':'compound_std',},inplace=True)
total = pd.merge(mean,std,how='inner', on='place_id')

os.makedirs(os.path.join(BASE_DIR,'store'), exist_ok=True)
dd.to_csv(Sentimental_data_CSV_PATH,header=True)
df.to_csv(Reviewr_PATH,header=True)
count_integrated_data = pd.read_csv(Count_integrated_CSV_PATH , index_col = 'place_id')
summary=pd.merge(count_integrated_data,total,how='inner', on='place_id')
summary.to_csv(Summary_sentimental_PATH,header=True)