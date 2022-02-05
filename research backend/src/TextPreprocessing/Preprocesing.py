# coding: utf-8

from src.TextPreprocessing.Lowercase import to_lower
from src.TextPreprocessing.WordTokenize import word_tokenize
from src.TextPreprocessing.RemoveStopwords import remove_stopwords
from src.TextPreprocessing.RemoveNumbers import remove_numbers
from src.TextPreprocessing.RemovePunctuation import remove_punct
from src.TextPreprocessing.RemoveTags import remove_Tags
from src.TextPreprocessing.Spaces import textFix


def pre_process(text):
    text = to_lower(text)
    text = textFix(text)
    text = remove_numbers(text)
    text = remove_punct(text)
    text = remove_Tags(text)
    text = remove_stopwords(text)
    text = word_tokenize(text)
    return (text)


