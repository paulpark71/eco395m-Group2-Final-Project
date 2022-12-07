import pandas as pd
import gender_guesser.detector as gender

ge = gender.Detector()


def review_gender(dataset):
    """
    Input: dataset
    Output: dataset(included gender guessed from author title)
    """
    temp = []
    for i, e in enumerate(dataset["author_title"]):
        temp.append(ge.get_gender(e.split()[0]))
    dd = pd.Series(temp, name="gender")
    dataset = pd.concat([dataset, dd], axis=1)
    return dataset
