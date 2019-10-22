import pandas
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pandas.read_csv("antivirus_dataset.csv", sep='|')
dfSize = df.shape
dfRows = dfSize[0]
dfColumns = dfSize[1]

df.drop(['Name', 'md5', 'MinorImageVersion', 'MinorSubsystemVersion', 'SectionsMeanRawsize', 'SectionsMeanVirtualsize', 'SectionsMinVirtualsize', 'SizeOfHeapCommit', 'SizeOfOptionalHeader'], axis='columns', inplace=True)

nbNewValues = dfRows*33//100
nbTrainingValues = dfRows - nbNewValues

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#k plus proches voisins
print("######################")
print("k plus proches voisins")
print("######################")
knn = KNeighborsClassifier(n_neighbors=10)
digit_knn = knn.fit(X_train, y_train)
prediction = knn.predict(X_test)
print("Estimation de l'erreur:")
print("- Precision = ", accuracy_score(y_test, prediction))
print("- Recall = ", recall_score(y_test, prediction))
print("- f1 score = ", f1_score(y_test, prediction))

#Regression logique
print("######################")
print("Regression logique")
print("######################")
regression = LogisticRegression()
trainRegression = regression.fit(X_train, y_train)
prediction = regression.predict(X_test)
print("Estimation de l'erreur:")
print("- Precision = ", accuracy_score(y_test, prediction))
print("- Recall = ", recall_score(y_test, prediction))
print("- f1 score = ", f1_score(y_test, prediction))
print("Coefficients: ", trainRegression.coef_, "\n")

#Arbre décisionnel
print("######################")
print("Arbre décisionnel")
print("######################")
tree = DecisionTreeClassifier()
digit_tree = tree.fit(X_train, y_train)
prediction = tree.predict(X_test)
print("Estimation de l'erreur:")
print("- Precision = ", accuracy_score(y_test, prediction))
print("- Recall = ", recall_score(y_test, prediction))
print("- f1 score = ", f1_score(y_test, prediction))
