# coding: utf-8
import nltk
from nltk import word_tokenize

from src.TextPreprocessing.Lowercase import to_lower



def selector(x, text):
    final =[]
    room_category = []
    hotelService_category = []
    food_category = []
    price_category = []
    others_category = []
    dom = x[0]
    for i in range(len(x[1])):
        if i == 0:
            for j in range(len(x[1][i])):
                word = x[1][i][j]
                word = str(word).casefold()
                txt = to_lower(text)
                sentences = nltk.sent_tokenize(txt)
                a = [sentence for sentence in sentences if word in sentence]
                s1 = ' '.join(str(e) for e in a)
                room_category.append(s1)
            s3 = " ".join(str(e) for e in room_category)
            final.append(s3)

        elif i == 1:
            for j in range(len(x[1][i])):
                word = x[1][i][j]
                word = str(word).casefold()
                txt = to_lower(text)
                sentences = nltk.sent_tokenize(txt)
                a = [sentence for sentence in sentences if word in sentence]
                s1 = ' '.join(str(e) for e in a)
                hotelService_category.append(s1)
            s2 = " ".join(str(e) for e in hotelService_category)
            final.append(s2)

        elif i == 2:
            for j in range(len(x[1][i])):
                word = x[1][i][j]
                word = str(word).casefold()
                txt = to_lower(text)
                sentences = nltk.sent_tokenize(txt)
                a = [sentence for sentence in sentences if word in sentence]
                s1 = ' '.join(str(e) for e in a)
                food_category.append(s1)
            s4 = " ".join(str(e) for e in food_category)
            final.append(s4)

        elif i == 3:
            for j in range(len(x[1][i])):
                word = x[1][i][j]
                word = str(word).casefold()
                txt = to_lower(text)
                sentences = nltk.sent_tokenize(txt)
                a = [sentence for sentence in sentences if word in sentence]
                s1 = ' '.join(str(e) for e in a)
                price_category.append(s1)
            s5 = " ".join(str(e) for e in price_category)
            final.append(s5)

        elif i == 4:
            for j in range(len(x[1][i])):
                word = x[1][i][j]
                word = str(word).casefold()
                txt = to_lower(text)
                sentences = nltk.sent_tokenize(txt)
                a = [sentence for sentence in sentences if word in sentence]
                s1 = ' '.join(str(e) for e in a)
                others_category.append(s1)
            s6 = " ".join(str(e) for e in others_category)
            final.append(s6)

        elif i == 5:
            for j in range(len(x[1][i])):
                word = x[1][i][j]
                word = str(word).casefold()
                txt = to_lower(text)
                sentences = nltk.sent_tokenize(txt)
                a = [sentence for sentence in sentences if word in sentence]
                s1 = ' '.join(str(e) for e in a)
                others_category.append(s1)
            s7 = " ".join(str(e) for e in others_category)
            final.append(s7)

    if dom == 'Hotel':
        hh_cat = ["Room", "Hotel Service", "Food", "Price", "Others"]
        for i in range(len(final)):
            if len(final[i]) == 0:
                hh_cat[i] = ''

        final1 = [i for i in final if i]
        hh_cat1 = [j for j in hh_cat if j]

        return (dom, final1, hh_cat1)

    elif dom == 'Movie':
        mm_cat =["Acting and Production", "Genre", "Duration", "Plot", "Others"]
        for i in range(len(final)):
            if len(final[i]) == 0:
                mm_cat[i] = ''

        final1 = [i for i in final if i]
        mm_cat1 = [j for j in mm_cat if j]
        return (dom, final1, mm_cat1)

