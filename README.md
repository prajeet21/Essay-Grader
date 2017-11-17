# Essay-Grader
It takes the essay as an input and gives the score between 0-1. 
Extracting Features :  featureExtraction.py file extracts features like wordCount, nounCount, adjectiveCount, keywords, etc. 
Total 13 features will be extracted and stored in file 13features.p by pickling the data.  Testing, Training, 
Predicting :  testTrainPredict.py file reads the features from 13feature.p file and applies linear regression from sklearn library.
