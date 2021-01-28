import numpy as np
from collections import Counter
from math import sqrt


def KNN(k, x_train, y_train, x):
    distances = [sqrt(np.sum((a - x) ** 2)) for a in x_train]
    nearest = np.argsort(distances)
    topk_y = [y_train[i] for i in nearest[:k]]
    votes = Counter(topk_y)
    predict_y = votes.most_common(1)[0][0]

    return predict_y
