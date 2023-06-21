from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier as KNN

data = load_iris()
print("Targets in Iris data:")
for i in range(len(data.target_names)):
    print(f'{i+1}){data.target_names[i]}')

x_train, x_test, y_train, y_test = tts(data.data, data.target, train_size=0.2)

knn = KNN(n_neighbors=5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
print(f'The accuracy score is:\n{accuracy_score(y_pred, y_test)}')


print("Actual-Label Predicted-Label")
for i, j in zip(y_test, y_pred):
    print(f'     {i}            {j}')
