id = []
label = []

import pandas as pd

df = pd.read_csv('multi_class_data/labels.csv')

def getColumnListValue(labels: str):
    for j in df[labels]:
        if j not in label:
            label.append(j)
    return label

def write2csv(filename: str, col1: asarray, col2: asarray, delimiter=","):
    assert len(col1) > 0
    res = ""
    for i in range(len(col1)):
        res += col1[i] + delimiter + col2 + "\n"
    pd.to_csv(filename + ".csv", res)

c = []