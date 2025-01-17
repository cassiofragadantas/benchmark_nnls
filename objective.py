from benchopt import BaseObjective
import numpy as np


class Objective(BaseObjective):
    name = "Non Negative Least Squares"

    parameters = {
        'fit_intercept': [False],
    }

    def __init__(self, fit_intercept=False):
        self.fit_intercept = fit_intercept

    def set_data(self, X, y):
        self.X, self.y = X, y

    def get_one_solution(self):
        n_features = self.X.shape[1]
        if self.fit_intercept:
            n_features += 1
        return np.zeros(n_features)

    def compute(self, beta):
        if (beta >= 0).all():
            diff = self.y - self.X.dot(beta)
            return .5 * diff.dot(diff)
        else:
            return np.inf

    def to_dict(self):
        return dict(X=self.X, y=self.y, fit_intercept=self.fit_intercept)
