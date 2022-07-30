import mysql.connector
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import Ridge

class ContentBase:

    def __init__(self, item, subject, item_subject, score):
        self.item = item
        self.subject = subject
        self.item_subject = item_subject
        self.score = score

    def tfidf(self):
        Tfidf = np.zeros((len(self.item), len(self.subject)))
        for x in self.item_subject:
            row = np.where(self.item == int(x[1]))[0][0]
            col = np.where(self.subject == int(x[2]))[0][0]
            Tfidf[row][col] = 1

        transformer = TfidfTransformer(smooth_idf=True, norm='l2')
        Tfidf = transformer.fit_transform(Tfidf).toarray()
        return Tfidf

    def calculate(self, amount):
        tfidf = self.tfidf()
        clf = Ridge(alpha=0.01, fit_intercept=True)
        Xhat = tfidf[self.score[:, 2], :]
        clf.fit(Xhat, self.score[:, 0] * 5)
        w = clf.coef_
        b = clf.intercept_
        np.set_printoptions(precision=2)
        Y = tfidf.dot(w) + b
        result = self.item
        for i in range(len(Y) - 1):
            for j in range(i + 1, len(Y)):
                if Y[i] < Y[j]:
                    a = Y[i]
                    Y[i] = Y[j]
                    Y[j] = a

                    b = result[i]
                    result[i] = result[j]
                    result[j] = b
        return result[0: amount].astype(int).tolist()

