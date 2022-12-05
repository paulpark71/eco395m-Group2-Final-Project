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


