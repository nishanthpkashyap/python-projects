from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier as Knn
from sklearn.metrics import accuracy_score, confusion_matrix

data = load_iris()

print('The target names in iris dataset is:')
for i in range(len(data.target_names)):
    print(f'{i+1}) {data.target_names[i]}')

x_train, x_test, y_train, y_test = tts(data.data, data.target, train_size=0.2)

knn = Knn(n_neighbors=5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
print("Actual-Label    Predicted-Label")
for i, j in zip(y_test, y_pred):
    print(f'     {i}               {j}')

print(f'The accuracy is score:\n{accuracy_score(y_test, y_pred)}')
print(f'The confusion matrix is:\n{confusion_matrix(y_test, y_pred)}')
