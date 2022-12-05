import pandas as pd
from collections import Counter

'''
    Input: all words
    Output: all counted data
'''
def all_count(All_wordsFiltered):
    all_count_data = pd.DataFrame(Counter(All_wordsFiltered).most_common())
    all_count_data.columns = ['all', 'counts']
    return all_count_data


'''
    Input: words in each places
    Output: counted data in each places

'''
def count_each_place(Each_place_words):
    count_each_place = dict()
    for e in Each_place_words:
        count_each_place[e] = Counter(Each_place_words[e]).most_common()
    each_place_data = pd.DataFrame(list(count_each_place.items()),columns=['place_id','frequent words'])
    return each_place_data


'''
    Input: words in each places
    Output: counted data in each places
'''
def count_each(Each_place_words):
    count_each_place = dict()
    for e in Each_place_words:
        count_each_place[e] = Counter(Each_place_words[e]).most_common()
    each_place_data = pd.DataFrame(list(count_each_place.items()),columns=['place_id','frequent words'])
    return each_place_data

'''
    Input: words in each gender
    Output: countdata in gender
'''

def count_each_gender(Each_gender_words):
    count_each_gender = dict()
    each_gender_data = pd.DataFrame()
    for e in Each_gender_words:
        count_each_gender[e] = Counter(Each_gender_words[e]).most_common()
    each_gender_data_temp = pd.DataFrame(list(count_each_gender.items())).T
