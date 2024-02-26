import string
import matplotlib.pyplot as plt
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
text=open('read.txt', encoding='utf-8').read()
text=text.lower()
cleanedText=""
for letter in text:##text.translate(str.maketrans('','',string.punctuation))
    if letter not in string.punctuation:
        cleanedText+=letter
wordList=word_tokenize(cleanedText, "english")
finalWords=[]
for word in wordList:
    if word not in stopwords.words("english"):
        finalWords.append(word)
emotionList=[]
with open('emotions.txt','r') as file:
    for line in file:
        clearLine=line.replace('\n',' ').replace("'",'').replace(',','').strip()
        word, emotion=clearLine.split(':')
        if word in finalWords:
            emotionList.append(emotion)
print(emotionList)
w=Counter(emotionList)

def sentimentAnalyze(sentimentText):
    score= SentimentIntensityAnalyzer().polarity_scores(sentimentText)
    print(type(score))
    neg=score['neg']
    pos=score["pos"]
    if neg>pos:
        print("Positive Sentiment")
    elif neg<pos:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")

sentimentAnalyze(cleanedText)
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
