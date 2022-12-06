import pandas as pd
from collections import Counter


def all_count(All_wordsFiltered):
    """
    Input: all words
    Output: all counted data
    """
    all_count_data = pd.DataFrame(Counter(All_wordsFiltered).most_common())
    all_count_data.columns = ["all", "counts"]
    return all_count_data


def count_each_place(Each_place_words):
    """
    Input: words in each places
    Output: counted data in each places
    """
    count_each_place = dict()
    for e in Each_place_words:
        count_each_place[e] = Counter(Each_place_words[e]).most_common()
    each_place_data = pd.DataFrame(
        list(count_each_place.items()), columns=["place_id", "frequent words"]
    )
    return each_place_data


def count_each(Each_place_words):
    """
    Input: words in each places
    Output: counted data in each places
    """
    count_each_place = dict()
    for e in Each_place_words:
        count_each_place[e] = Counter(Each_place_words[e]).most_common()
    each_place_data = pd.DataFrame(
        list(count_each_place.items()), columns=["place_id", "frequent words"]
    )
    return each_place_data


def count_each_gender(Each_gender_words):
    """
    Input: words in each gender
    Output: countdata in gender
    """
    count_each_gender = dict()
    each_gender_data = pd.DataFrame()
    for e in Each_gender_words:
        count_each_gender[e] = Counter(Each_gender_words[e]).most_common()
    each_gender_data_temp = pd.DataFrame(list(count_each_gender.items())).T

    for i in range(len(each_gender_data_temp.T)):
        temp1 = []
        temp2 = []
        cname = each_gender_data_temp[i][0]
        cname2 = ""
        for e in each_gender_data_temp[i][1]:
            temp1.append(e[0])
            temp2.append(e[1])
        temp1S = pd.Series(temp1.copy(), name=cname)
        temp2S = pd.Series(temp2.copy(), name=cname2)
        each_gender_data = pd.concat([each_gender_data, temp1S, temp2S], axis=1)
    return each_gender_data
