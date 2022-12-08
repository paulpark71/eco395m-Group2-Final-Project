import pandas as pd
import os
from .functions.tokenized_without_stopwords import tokenized_without_stopwords
from .functions.count_each_gender import all_count, count_each_place, count_each_gender


"""
    Initial Setting
"""
BASE_DIR = "artifacts"
Data_DIR = "data"

Stopwords_Path = os.path.join(Data_DIR, "stop_words.txt")
Additional_Stopwords_Path = os.path.join(Data_DIR, "additional_stop_words.txt")
Reveiws_CSV_PATH = os.path.join(Data_DIR, "reviews.csv")

Count_CSV_PATH = os.path.join(BASE_DIR, "all_count.csv")
Count_Each_CSV_PATH = os.path.join(BASE_DIR, "store", "count_each.csv")
Count_Each_Gender_CSV_PATH = os.path.join(BASE_DIR, "store", "count_each_gender.csv")

Integrated_CSV_PATH = os.path.join(BASE_DIR, "store", "basic.csv")
Count_integrated_CSV_PATH = os.path.join(BASE_DIR, "store", "count_plus_basic.csv")


"""
    1. Read Reviews from reviews.csv in the data
"""
dataset = pd.read_csv(Reveiws_CSV_PATH)

"""
    2. Get Tokenized Text with excluding NA/blank/stopwords
"""
Tokenized_text = tokenized_without_stopwords(
    dataset, Stopwords_Path, Additional_Stopwords_Path
)
All_wordsFiltered = Tokenized_text[0]
Each_place_words = Tokenized_text[1]
Each_gender_words = Tokenized_text[2]


"""
    3. Word count
"""
all_count_data = all_count(All_wordsFiltered)
count_place_data = count_each_place(Each_place_words)
count_gender_data = count_each_gender(Each_gender_words)


all_count_data = pd.concat([all_count_data, count_gender_data], axis=1)


"""
   4. Ouput each results to csv.files
"""
with open(
    Count_CSV_PATH, mode="w", newline="", encoding="shift-jis", errors="ignore"
) as f:
    all_count_data.to_csv(Count_CSV_PATH, header=True)

with open(
    Count_Each_CSV_PATH, mode="w", newline="", encoding="shift-jis", errors="ignore"
) as f:
    count_place_data.to_csv(Count_Each_CSV_PATH, header=True, index=False)


"""
    5. Intergrated with this result and previous one
"""
integrated_data = pd.read_csv(Integrated_CSV_PATH, index_col="place_id")
count_data = pd.read_csv(Count_Each_CSV_PATH, index_col="place_id")

count_integrated_data = pd.merge(
    integrated_data, count_data, on="place_id", how="inner"
)
print(count_integrated_data)
with open(
    Count_integrated_CSV_PATH,
    mode="w",
    newline="",
    encoding="shift-jis",
    errors="ignore",
) as f:
    count_integrated_data.to_csv(Count_integrated_CSV_PATH, header=True)
