from src.SentimentAnalysis.HotelSentiment import *
from src.SentimentAnalysis import *


def analysis(select, com):
    cat_sen = []
    com_sen = []

    posi = []
    neut = []
    nega = []

    sel_arr = select[1]

    if select[0] is "Movie":
        pickle_in = open("Moviesentiment.pickle", "rb")
        grid_svm = pickle.load(pickle_in)
        line_tokens = sel_arr
        for line in line_tokens:
            # predict the probability that the object belongs to the given classes.
            predict_probability = grid_svm.predict_proba([line])
            arr1 = []
            for probability in predict_probability:
                pos = "{:.10f}".format(probability[0])
                neg = "{:.10f}".format(probability[1])
                neu = "{:.10f}".format(probability[2])
                arr1.append(pos)
                arr1.append(neg)
                arr1.append(neu)
                nega.append(pos)
                neut.append(neg)
                posi.append(neu)
            cat_sen.append(arr1)

        comment_probability = grid_svm.predict_proba(com)
        for probability in comment_probability:
            neg = "{:.10f}".format(probability[0])
            neu = "{:.10f}".format(probability[1])
            pos = "{:.10f}".format(probability[2])
            com_sen.append(neg)
            com_sen.append(neu)
            com_sen.append(pos)

        return nega, neut, posi, com_sen

    elif select[0] is "Hotel":
        pickle_in = open('Hotelsentiment.pickle', "rb")
        grid_svm = pickle.load(pickle_in)
        line_tokens = sel_arr
        for line in line_tokens:
            # predict the probability that the object belongs to the given classes.
            predict_probability = grid_svm.predict_proba([line])
            arr1 = []
            for probability in predict_probability:
                pos = "{:.10f}".format(probability[0])
                neg = "{:.10f}".format(probability[1])
                neu = "{:.10f}".format(probability[2])
                arr1.append(pos)
                arr1.append(neg)
                arr1.append(neu)
                nega.append(pos)
                neut.append(neg)
                posi.append(neu)
            cat_sen.append(arr1)

        comment_probability = grid_svm.predict_proba(com)
        for probability in comment_probability:
            neg = "{:.10f}".format(probability[0])
            neu = "{:.10f}".format(probability[1])
            pos = "{:.10f}".format(probability[2])
            com_sen.append(neg)
            com_sen.append(neu)
            com_sen.append(pos)
        return nega,neut,posi,com_sen

    else:
        print("c")

