def count_words(words, stopwords):

    """
    Input: words
    Output word_counts

    * Counts the words that are not included in stopwords.
    returns a dictionary with words as keys and values.
    """

    word_counts = dict()
    for e in words:
        if e not in word_counts:
            if e not in stopwords:
                word_counts.setdefault(e, 1)
        else:
            if e not in stopwords:
                word_counts[e] = word_counts[e] + 1
    return word_counts
