from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split as tts
from sklearn.mixture import GaussianMixture
from sklearn.datasets import load_iris

data = load_iris()

x_train, x_test, y_train, y_test = tts(data.data, data.target)

kmeans = KMeans(n_clusters=3)
kmeans.fit(x_train, y_train)
y_pred = kmeans.predict(x_test)
print(f'Kmeans accuracy score:\n{accuracy_score(y_test, y_pred)}')
print(f'Kmeans Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}')

gm = GaussianMixture(n_components=3)
gm.fit(x_train, y_train)
y_pred = gm.predict(x_test)
print(f'Kmeans accuracy score:\n{accuracy_score(y_test, y_pred)}')
print(f'Kmeans Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}')
