from src.SentimentAnalysis.SentimentMain import *

pickle_in = open("Hotelsentiment.pickle", "rb")
grid_svm = pickle.load(pickle_in)

predictions = grid_svm.predict(X_test)
best_accuracy=grid_svm.best_score_
print(best_accuracy)

from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))
