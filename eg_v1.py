import xlrd
import nltk
import re
import enchant
import pickle

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

#for i in range(0,12978):
#	print(score[i][1],score[i][3])

print(len(score))

wc = []
sc = []
nc = []
vc = []
advc = []
adjc = []
lwc = []
cc = []
pc = []
ld = []
qc = []
spell = []
kw = []

kwID1 = ["education","communicating","technology","society","positive","negative","effects","communication","conversation","texting","teaching"]
kwID2 = [ "library","censor","books","media specialist","book banning","censorship","self-censorship","students","education","suppressing","free speech","freedom","internet porn","inappropriate content","maturity"]
kwID3 = ["bicycles","bike","physical fitness","means of transportation","soil","organic","reactions","weight cutting","combat sports","muscle movement","Health","economic benefits"]
kwID4 = ["Winter Hibiscus","concludes","author","summary","story","Saeng","example","instance","reasons"]
kwID5 = ["author","feelings","feels","tells","writer","story","example","instance","reasons","summary"]
kwID6 = ["iconic skyscrapers","architecture","construction","buildings","interior design","obstacles","sustainable buildings","environment","waste","problems"]
kwID7 = ["patience","waited","thinking and acting","service learning","love","family","confidence","frugality","health","adaptations","self-improvement","temperance","chastity","anxiety","compassion","happy"]
kwID8 = ["laughter","cure","therapy","depression","muscles","zygomaticus","cheekbones","humor","playfulness","exercise","stress management","health","angry","protein","comedy","sense","emotions","irony","sarcasm","happy","symptoms"]

def wordCount(text):
	tokens = nltk.word_tokenize(text)
	return (len(tokens))

def sentCount(text):
	tokens = nltk.sent_tokenize(text)
	return (len(tokens))

def nounCount(text):
	cnt_nn=0
	tokens = nltk.word_tokenize(text)
	postags = nltk.pos_tag(tokens)
	for j in range(len(postags)):
		if postags[j][1] == "NN" or postags[j][1] == "NNS" or postags[j][1] == "NNP" or postags[j][1] == "NNPS":
			cnt_nn+=1
	return (cnt_nn)

def verbCount(text):
	cnt_vrb=0
	tokens = nltk.word_tokenize(text)
	postags = nltk.pos_tag(tokens)
	for j in range(len(postags)):
		if postags[j][1] == "VB" or postags[j][1] == "VBD" or postags[j][1] == "VBG" or postags[j][1] == "VBN" or postags[j][1] == "VBP" or postags[j][1] == "VBZ":
			cnt_vrb+=1
	return (cnt_vrb)

def adjectiveCount(text):
	cnt_adjctv=0
	tokens = nltk.word_tokenize(text)
	postags = nltk.pos_tag(tokens)
	for j in range(len(postags)):
		if postags[j][1] == "JJ" or postags[j][1] == "JJR" or postags[j][1] == "JJS":
			cnt_adjctv+=1
	return (cnt_adjctv)

def adverbCount(text):
	cnt_advrb=0
	tokens = nltk.word_tokenize(text)
	postags = nltk.pos_tag(tokens)
	for j in range(len(postags)):
		if postags[j][1] == "RB" or postags[j][1] == "RBR" or postags[j][1] == "RBS":
			cnt_advrb+=1
	return (cnt_advrb)

def longWordCount(text):
	cnt_g5=0
	tokens = nltk.word_tokenize(text)
	for words in tokens:
		if len(words)>5:
			cnt_g5+=1
	return (cnt_g5)

def commaCount(text):
	cnt_comma=0
	tokens = nltk.word_tokenize(text)
	for comma in tokens:
		if comma==",":
			cnt_comma+=1
	return (cnt_comma)

def punctCount(text):
	cnt_pnct=0
	tokens = nltk.word_tokenize(text)
	Punct = re.compile('.*[^A-Za-z0-9/-].*')
	filtered = [words for words in tokens if Punct.match(words)]
	cnt_pnct+=len(filtered)
	return (cnt_pnct)

def lexDivCount(text):
	tokens = nltk.word_tokenize(text)
	return (float(len(set(tokens))/len(tokens)))

def quoteCount(text):
	cnt_qt=0
	tokens = nltk.word_tokenize(text)
	for quote in tokens:
		if "'" in quote:
			cnt_qt+=1
	return (cnt_qt)

def spellErrCount(text):
	cnt_spl=0
	tokens = nltk.word_tokenize(text)
	Dict = enchant.Dict("en_US")
	for spelling in tokens:
		if not Dict.check(spelling):
			cnt_spl+=1
	return (cnt_spl)

def keyWordsCount(text):
	cnt_kw=0
	tokens = nltk.word_tokenize(score[i][2])
	if score[i][1]==1:
		for keyWords in tokens:
			if keyWords in kwID1:
				cnt_kw+=1
		return (cnt_kw)
	elif score[i][1]==2:
		for keyWords in tokens:
			if keyWords in kwID2:
				cnt_kw+=1
		return (cnt_kw)
	elif score[i][1]==3:
		for keyWords in tokens:
			if keyWords in kwID3:
				cnt_kw+=1
		return (cnt_kw)
	elif score[i][1]==4:
		for keyWords in tokens:
			if keyWords in kwID4:
				cnt_kw+=1
		return (cnt_kw)
	elif score[i][1]==5:
		for keyWords in tokens:
			if keyWords in kwID5:
				cnt_kw+=1
		return (cnt_kw)
	elif score[i][1]==6:
		for keyWords in tokens:
			if keyWords in kwID6:
				cnt_kw+=1
		return (cnt_kw)
	elif score[i][1]==7:
		for keyWords in tokens:
			if keyWords in kwID7:
				cnt_kw+=1
		return (cnt_kw)
	elif score[i][1]==8:
		for keyWords in tokens:
			if keyWords in kwID8:
				cnt_kw+=1
		return (cnt_kw)




for i in range(0,12978):
	print(i)
	wc.append(wordCount(score[i][2]))
	sc.append(sentCount(score[i][2]))
	nc.append(nounCount(score[i][2]))
	vc.append(verbCount(score[i][2]))
	adjc.append(adjectiveCount(score[i][2]))
	advc.append(adverbCount(score[i][2]))
	lwc.append(longWordCount(score[i][2]))
	cc.append(commaCount(score[i][2]))
	pc.append(punctCount(score[i][2]))
	ld.append(lexDivCount(score[i][2]))
	qc.append(quoteCount(score[i][2]))
	spell.append(spellErrCount(score[i][2]))
	kw.append(keyWordsCount(score[i][2]))
	
print(len(wc),len(sc),len(nc),len(vc),len(adjc),len(advc),len(lwc),len(cc),len(pc),len(ld),len(qc),len(spell),len(kw))
print(wc,sc,nc,vc,adjc,advc,lwc,cc,pc,ld,qc,spell,kw)

features = {}
features['word']=wc
features['sent']=sc
features['noun']=nc
features['verb']=vc
features['adjective']=adjc
features['adverb']=advc
features['longword']=lwc
features['coma']=cc
features['punct']=pc
features['lexdiv']=ld
features['quotes']=qc
features['spellerr']=spell
features['keyword']=kw

with open('13features.p','wb') as f:
	pickle.dump( features, f )
