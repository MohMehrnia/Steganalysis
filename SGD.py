import csv
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.classification import accuracy_score
from sklearn.metrics import classification_report
#from dbn import SupervisedDBNClassification
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import SGDClassifier

def loaddata(filename,instanceCol):
    file_reader = csv.reader(open(filename,'r'),delimiter=',')
    x = []
    y = []
    for row in file_reader:
        x.append(row[0:instanceCol])
        y.append(row[-1])
    return np.array(x[1:]).astype((np.float32)), np.array(y[1:]).astype(np.int)

def modeldata(filename):
    scores = []
    print(filename)
    X,Y = loaddata(filename, 99)

    for i in range(3):
        #print('Cross ' + str(i))
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
        # relu, sigmoid
        classifier = SGDClassifier(loss="hinge", penalty="l2")
        classifier.fit(X_train, Y_train)
        Y_pred = classifier.predict(X_test)
        scores.append(accuracy_score(Y_test, Y_pred))
        #print(classification_report(Y_test, Y_pred))

    print('All Accuracy Scores in Cross: ' + str(scores))
    print('Mean Accuracy Scores: ' + str(np.mean(scores)))

if __name__ == '__main__':
    modeldata('D:\\Databases\\PDA\\CSV\\feature(MFCC-70-30-1400b).csv')
    modeldata('D:\\Databases\\PDA\\CSV\\feature(FBank-70-30-1400b).csv')
    modeldata('D:\\Databases\\PDA\\CSV\\feature(LogFBank-70-30-1400b).csv')
    modeldata('D:\\Databases\\PDA\\CSV\\feature(Fractal-70-30-1400b).csv')
