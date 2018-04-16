# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:46:15 2018

@author: sam
"""

import jieba

stopWordsPath = "chineseStopWords.txt"
textPath = "chineseText.txt"

def buildStopwords(path):
    text = ""
    with open(path,"r",encoding="utf-8") as file:
        for line in file.readlines():
            text += line
    text = text.split(",")
    return text
    
def extractText(path):
    text = ""
    with open(path, "r",encoding="utf-8") as file:
        for line in file.readlines():
            text += line
    return(text)

def preprocessText(text,stopwords):
    sentences = text.split("。")
    cutSentences = []
    
    for sentence in sentences:
        sentence = jieba.cut(sentence,cut_all=False)
        cutSentences.append(list(sentence))
        
    #print(cutSentences)
    
    sentences = []
    for sentence in cutSentences:
        cleanedSentence = []
        for word in sentence:
            if word not in stopwords:
                cleanedSentence.append(word)
        if(len(cleanedSentence) > 0):
            sentences.append(cleanedSentence)   
    
    return sentences

        

#text = extractText(textPath)
#stopwords = buildStopwords(stopWordsPath)

text = preprocessText(extractText(textPath),buildStopwords(stopWordsPath))

def summarize(text,strictness):
    freqTable = dict()
    
    for sentence in text:
        for word in sentence:
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1
            
    sentenceValues = []
    
    for sentence in text:
        sentenceValue = 0
        for word in sentence:
            if word in freqTable:
                sentenceValue += freqTable[word]
        sentenceValue = sentenceValue / len(sentence)
        sentenceValues.append(sentenceValue)
        
        
    averageValue = 0
    
    for value in sentenceValues:
        print(value)
        averageValue += value
    averageValue = averageValue / len(sentenceValues)
    
    
    summary = ""
    sentenceNum = 0 
    for sentence in text:
        sentenceText = ""
        if(sentenceValues[sentenceNum] > (strictness * averageValue)):
            for word in sentence:
                sentenceText += word
        summary = summary + sentenceText + ". "

    return summary

print(summarize(text,1.2))
        
        
        
        
        
        
        
        
        
    
            
