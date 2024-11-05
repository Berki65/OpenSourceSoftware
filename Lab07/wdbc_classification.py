"""
Assignment from Berkay Bentetik - 24170078
Python Lab 07 - Breast Cancer Classification
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import (datasets, svm, metrics)
from matplotlib.lines import Line2D # For the custom legend
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay


def load_wdbc_data(filename):
    class WDBCData:
        data          = [] # Shape: (569, 30)
        target        = [] # Shape: (569, )
        target_names  = ['malignant', 'benign']
        feature_names = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness', 'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension',
                         'radius error', 'texture error', 'perimeter error', 'area error', 'smoothness error', 'compactness error', 'concavity error', 'concave points error', 'symmetry error', 'fractal dimension error',
                         'worst radius', 'worst texture', 'worst perimeter', 'worst area', 'worst smoothness', 'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry', 'worst fractal dimension']
    wdbc = WDBCData()
    with open(filename) as f:
        for line in f.readlines():
            items = line.split(',')
            diagnosis = 0 if items[1] == 'M' else 1
            wdbc.target.append(diagnosis)

            features = list(map(float, items[2:]))
            wdbc.data.append(features)
        wdbc.data = np.array(wdbc.data)
        wdbc.target = np.array(wdbc.target)
    return wdbc

if __name__ == '__main__':
    # Load a dataset
    wdbc = load_wdbc_data('data/wdbc.data')

    # Train a model SVM
    modelS = svm.SVC()
    modelS.fit(wdbc.data, wdbc.target)

    # Train a model Random Forest
    modelF = RandomForestClassifier(n_estimators=100, random_state=42)
    modelF.fit(wdbc.data, wdbc.target)

    # Test the model SVM
    predictS = modelS.predict(wdbc.data)
    accuracyS = metrics.balanced_accuracy_score(wdbc.target, predictS)

    # Test the model Random Forest
    predictF = modelF.predict(wdbc.data)
    accuracyF = metrics.balanced_accuracy_score(wdbc.target, predictF)

    # Confusion Matrix SVM
    cm = metrics.confusion_matrix(wdbc.target, predictS)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=wdbc.target_names)
    disp.plot()
    plt.title('Confusion Matrix')
    plt.show()

    # Confusion Matrix Random Forest
    cm = metrics.confusion_matrix(wdbc.target, predictF)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=wdbc.target_names)
    disp.plot(cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.show()

    # Visualize testing results SVM
    cmap = np.array([(1, 0, 0), (0, 1, 0)])
    clabel = [Line2D([0], [0], marker='o', lw=0, label=wdbc.target_names[i], color=cmap[i]) for i in range(len(cmap))]
    for (x, y) in [(0, 1)]: # Not mandatory, but try [(i, i+1) for i in range(0, 30, 2)]
        plt.figure()
        plt.title(f'My Classifier (Accuracy: {accuracyS:.3f})')
        plt.scatter(wdbc.data[:,x], wdbc.data[:,y], c=cmap[wdbc.target], edgecolors=cmap[predictS])
        plt.xlabel(wdbc.feature_names[x])
        plt.ylabel(wdbc.feature_names[y])
        plt.legend(handles=clabel, framealpha=0.5)
    plt.show()

    # Visualize testing results Random Forest
    cmap = np.array([(1, 0, 0), (0, 1, 0)])
    clabel = [Line2D([0], [0], marker='o', lw=0, label=wdbc.target_names[i], color=cmap[i]) for i in range(len(cmap))]
    for (x, y) in [(0, 1)]: # Not mandatory, but try [(i, i+1) for i in range(0, 30, 2)]
        plt.figure()
        plt.title(f'My Classifier (Accuracy: {accuracyF:.3f})')
        plt.scatter(wdbc.data[:,x], wdbc.data[:,y], c=cmap[wdbc.target], edgecolors=cmap[predictF])
        plt.xlabel(wdbc.feature_names[x])
        plt.ylabel(wdbc.feature_names[y])
        plt.legend(handles=clabel, framealpha=0.5)
    plt.show()