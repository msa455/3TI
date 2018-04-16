# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 10:09:46 2018

@author: sam
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

stopWords = set(stopwords.words("english"))

textPath = "newsToSummarize.txt"

def extractText(path):
    text = ""
    with open(textPath, "r") as file:
        for line in file.readlines():
            text += line
    return(text)


def createSummary(text,strictness):
    words = word_tokenize(text)


    freqTable = dict()
    for word in words:
        word = word.lower()
        if word not in stopWords:
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1
      
    sentences = sent_tokenize(text)

    sentenceValues = [] 

    for sentence in sentences:
        sentenceValue = 0
        sentence = sentence.split(" ")
        for word in sentence:
            if word in freqTable:
                sentenceValue += freqTable[word]
        sentenceValue = sentenceValue / len(sentence)
        
        sentenceValues.append(sentenceValue)

    sumValues = 0
    for value in sentenceValues:
        sumValues += value
    averageValue = sumValues / len(sentenceValues)
    
    thresholdValue = averageValue * strictness
    
    summary = " "
    sentenceNum = 0
    
    
    for sentence in sentences:
        if(sentenceValues[sentenceNum] > thresholdValue):
            summary += sentence
        sentenceNum += 1

    return(summary)
    
print(createSummary(extractText(textPath),1.5))

            
            
    
    