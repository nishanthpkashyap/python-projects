import pandas as pd
from collections import Counter
from sklearn.feature_selection import mutual_info_classif


def id3(data, target, attr, default_class=None):
    count = Counter(x for x in data[target])

    if len(count) == 1:
        return next(iter(count))
    elif data.empty or not attr:
        return default_class
    else:
        gain = mutual_info_classif(data[attr], data[target], discrete_features=True)
        index_of_best_attr = gain.tolist().index(max(gain))
        best_attr = attr[index_of_best_attr]
        remaining_attr = [i for i in attr if i != attr]
        tree = {best_attr: {}}
        for v, sub in data.groupby(best_attr):
            subtree = id3(sub, target, remaining_attr, default_class)
            tree[best_attr][v] = subtree
        return tree


datas = pd.read_csv("id3.csv")
attribute = datas.columns.tolist()
attribute.remove("Class")

for col in datas.select_dtypes("object"):
    datas[col], _ = datas[col].factorize()

print(id3(datas, "Class", attribute))
