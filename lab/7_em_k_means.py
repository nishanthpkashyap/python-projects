from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split as tts
from sklearn.mixture import GaussianMixture
from sklearn import datasets

data = datasets.load_iris()

x_train, x_test, y_train, y_test = tts(data.data, data.target)

kmeans = KMeans(n_clusters=3)
kmeans.fit(x_train, y_train)
kmeans.score(x_train, y_train)
print(f'Kmeans:\n{accuracy_score(kmeans.predict(x_train), y_train)}')

gm = GaussianMixture(n_components=3)
gm.fit(x_train, y_train)
gm.score(x_train, y_train)
print(f'GaussianMixture:\n{accuracy_score(gm.predict(x_train), y_train)}')

