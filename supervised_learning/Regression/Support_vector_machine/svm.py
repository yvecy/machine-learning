#importing the libraries


style.use('ggplot')

#importing the dataset
dataset =pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

#splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
classifier = SVC(kernel = 'linear' , random_state = 0)
classifier.fit()




