import re
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.stem import SnowballStemmer
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pickle
# reading csv file
data = pd.read_csv('moviedata.csv', encoding='mac_roman')
# transform text to lowercase
(data['Review']).astype(str)
data['Review'].apply(lambda x: str(x).lower())  # transform text to lowercase
data['Review'] = data['Review'].apply(lambda x: re.sub('[^a-zA-z0-9\s]', '', str(x)))
data['Review'].head()
# split the data into training and testing set
train, test = train_test_split(data, test_size=0.2, random_state=1)
X_train = train['Review'].values
X_test = test['Review'].values
y_train = train['Sentiment']
y_test = test['Sentiment']
def tokenize(text):
    tknzr = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
    return tknzr.tokenize(text)
def stem(doc):
    stemmer = SnowballStemmer('english')
    analyzer = CountVectorizer().build_analyzer()
    return (stemmer.stem(w) for w in analyzer(doc))



pickle_in = open("Moviesentiment.pickle", "rb")
grid_svm = pickle.load(pickle_in)

predictions = grid_svm.predict(X_test)
best_accuracy=grid_svm.best_score_
print(best_accuracy)

from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))