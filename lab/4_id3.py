import pandas
from collections import Counter
from sklearn.feature_selection import mutual_info_classif


def id3(data, target, attributes, default_class=None):
    count = Counter(x for x in data[target])

    if len(count) == 1:
        return next(iter(count))

    elif data.empty or not attributes:
        return default_class

    else:
        gain = mutual_info_classif(data[attributes], data[target], discrete_features=True)
        index_of_best_attribute = (list(gain)).index(max(gain))
        best_attribute = attributes[index_of_best_attribute]
        remaining_attributes = [i for i in attributes if i != best_attribute]
        tree = {best_attribute: {}}
        for value, data_subset in data.groupby(best_attribute):
            subtree = id3(data_subset, target, remaining_attributes, default_class)
            tree[best_attribute][value] = subtree
        return tree


data = pandas.read_csv("id3.csv")
attributes = list(data.columns)
attributes.remove("Class")
target = "Class"

for col in data.select_dtypes("object"):
    data[col], _ = data[col].factorize()

# print(data)

res = id3(data, target, attributes)
print("\nTree Structure:")
print(res)


# import pandas as pd
# from pprint import pprint
# from sklearn.feature_selection import mutual_info_classif
# from collections import Counter
#
#
# def id3(df, target_attribute, attribute_names, default_class=None):
#     cnt = Counter(x for x in df[target_attribute])
#     if len(cnt) == 1:
#         return next(iter(cnt))
#
#     elif df.empty or (not attribute_names):
#         return default_class
#
#     else:
#         gainz = mutual_info_classif(df[attribute_names], df[target_attribute], discrete_features=True)
#         index_of_max = gainz.tolist().index(max(gainz))
#         best_attr = attribute_names[index_of_max]
#         tree = {best_attr: {}}
#         remaining_attribute_names = [i for i in attribute_names if i != best_attr]
#
#         for attr_val, data_subset in df.groupby(best_attr):
#             subtree = id3(data_subset, target_attribute, remaining_attribute_names, default_class)
#             tree[best_attr][attr_val] = subtree
#
#         return tree
#
#
# df = pd.read_csv("id3.csv")
#
# attribute_names = df.columns.tolist()
# print("List of attribute name")
#
# attribute_names.remove("Class")
#
# for colname in df.select_dtypes("object"):
#     df[colname], _ = df[colname].factorize()
#
# print(df)
#
# tree = id3(df, "Class", attribute_names)
# print("The tree structure")
# pprint(tree)
