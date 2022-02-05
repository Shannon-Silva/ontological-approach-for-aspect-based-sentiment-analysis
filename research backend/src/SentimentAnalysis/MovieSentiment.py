#Importing libraries
import re
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
#from nltk.tokenize import TweetTokenizer
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, accuracy_score, f1_score
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import confusion_matrix, roc_auc_score, recall_score, precision_score
import pickle

#reading csv file
data = pd.read_csv('moviedata.csv', encoding='mac_roman')

#transform text to lowercase
(data['Review']).astype(str)
data['Review'].apply(lambda x: str(x).lower()) #transform text to lowercase

data['Review'] = data['Review'].apply(lambda x: re.sub('[^a-zA-z0-9\s]', '', str(x)))
data['Review'].head()

print(data.head())

#split the data into training and testing set
train, test = train_test_split(data, test_size=0.2, random_state=1)
X_train = train['Review'].values
X_test = test['Review'].values
y_train = train['Sentiment']
y_test = test['Sentiment']


def tokenize(text):
    tknzr  = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
    return tknzr.tokenize(text)

def stem(doc):
    stemmer = SnowballStemmer('english')
    analyzer = CountVectorizer().build_analyzer()
    return (stemmer.stem(w) for w in analyzer(doc))

en_stopwords = set(stopwords.words("english"))
#Convert a collection of text documents to a matrix of token counts
vectorizer = CountVectorizer(
    analyzer = 'word',
    tokenizer = tokenize,
    lowercase = True,
    ngram_range=(1, 1),
    stop_words = en_stopwords)

#cross validation and grid search to find good hyperparameters for our SVM model.
kfolds = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)

#Construct a Pipeline from the given estimators
np.random.seed(1)

pipeline_svm = make_pipeline(vectorizer,
                            SVC(probability=True, kernel="linear", class_weight="balanced")
                           # SVC(probability=True,C=10, kernel='linear', gamma=0.01,class_weight="balanced")
#SVC(probability=True,gamma='scale', kernel='rbf', C=1)
                             )

# Run the grid search
# grid_svm = GridSearchCV(pipeline_svm,
#                     param_grid = {'svc__C': [0.01, 0.1, 1]},
#                     cv = kfolds,
#                    # scoring='accuracy',
#                     verbose=1,
#                     n_jobs=-1)
#
# grid_svm.fit(X_train, y_train)
# accuracy=grid_svm.score(X_test, y_test)
# print(accuracy)
#
# #check Parameter setting that gave the best results on the hold out data.
# grid_svm.best_params_
#
# #check cross-validated score of the best_estimator
# grid_svm.best_score_
#
#
# with open("Moviesentiment.pickle", "wb") as f:
#    pickle.dump(grid_svm, f)
#
# pickle_in = open("Moviesentiment.pickle", "rb")
# grid_svm = pickle.load(pickle_in)
