import xlrd
import nltk
import re
import enchant
import pickle
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

features = pickle.load(open('13features.p','rb'))

wc=features['word']
sc=features['sent']
nc=features['noun']
vc=features['verb']
adjc=features['adjective']
advc=features['adverb']
lwc=features['longword']
cc=features['coma']
pc=features['punct']
ld=features['lexdiv']
qc=features['quotes']
spell=features['spellerr']
kw=features['keyword']

#print(len(wc),len(sc),len(nc),len(vc),len(adjc),len(advc),len(lwc),len(cc),len(pc),len(ld),len(qc),len(spell),len(kw))
#print(wc,sc,nc,vc,adjc,advc,lwc,cc,pc,ld,qc,spell,kw)

book = xlrd.open_workbook("/home/harsh/training_set.xls")

first_sheet = book.sheet_by_index(0)

cell = first_sheet.cell(0,0)

score = []
for i in range(1,12979):
	score.append(first_sheet.row_values(i))

for i in range(1,9):
	k = 0
	for j in range(0,12978):
		if score[j][1] == i:
			if score[j][3] >= k:
				k = score[j][3]
	for j in range(0,12978):
		if score[j][1] == i:
			score[j][3] = score[j][3] / (k)

x=np.zeros((12978,13))

for i in range(12978):
	x[i][0]=wc[i]
	x[i][1]=sc[i]
	x[i][2]=nc[i]
	x[i][3]=vc[i]
	x[i][4]=adjc[i]
	x[i][5]=advc[i]
	x[i][6]=lwc[i]
	x[i][7]=cc[i]
	x[i][8]=pc[i]
	x[i][9]=ld[i]
	x[i][10]=qc[i]
	x[i][11]=spell[i]
	x[i][12]=spell[i]

x = np.asarray(x)

y = []
for i in range(0,12978):
	y.append(score[i][3])

y = np.asarray(y)
print(x.shape,y.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(y_train.shape)
print(x_train.shape)
print(y_test.shape)
print(x_test.shape)

regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)
mse = (np.mean((regr.predict(x_test) - y_test) ** 2))
acc = 100-mse*100
print("Accuracy:::::: %.7f" % acc)
print(y_test[0:10])
print(regr.predict(x_test)[0:10])
print("Co-efficient:::::::: \n",regr.coef_)
print(len(regr.coef_))
#from sklearn.metrics import confusion_matrix
#print(confusion_matrix(y_test,regr.predict(x_test)))