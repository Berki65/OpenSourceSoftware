"""
Assignment from Berkay Bentetik - 24170078
Python Lab 8 - Breast Cancer Classification with Cross-validation
"""

from sklearn import (datasets, tree, model_selection)
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import time

if __name__ == '__main__':
    # Load a dataset
    wdbc = datasets.load_breast_cancer()

    # Initialize the model
    model = RandomForestClassifier(max_depth=11, random_state=2, n_estimators=100)

    # Start timing
    start_time = time.time()

    # Perform cross-validation
    cv_results = model_selection.cross_validate(model, wdbc.data, wdbc.target, cv=5, return_train_score=True)

    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Evaluate the model
    acc_train = np.mean(cv_results['train_score'])
    acc_test = np.mean(cv_results['test_score'])
    print(f'* Accuracy @ training data: {acc_train:.3f}')
    print(f'* Accuracy @ test data: {acc_test:.3f}')
    print(f'* Your score: {max(10 + 100 * (acc_test - 0.9), 0):.0f}')
    print(f'* Elapsed time: {elapsed_time:.2f} seconds')
