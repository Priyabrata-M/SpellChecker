

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 22:41:12 2017

@author: abhijit
"""

import operator




def getSubSet(misspelledWord):
    #Read the file and push each string one by one into the list
    with open("../data/wordlist.txt") as f:
        inputBuffer = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    inputBuffer = [x.strip() for x in inputBuffer] 
    #print inputBuffer
    #print len(inputBuffer)
    
    #print inputBuffer[0]
    trigram=[];   
    mostCloselyRelatedsubSet=[];
    
    dict = {};
         
    for item in range(len(inputBuffer)):  
            inputString = inputBuffer[item];     
            for i in range(len(inputString)-2):   
               if dict.has_key(inputString[i:i+3]):
                  #find the value for that key and append the new value
                  #print "if start"
                  value=[];
                  value= dict.get(inputString[i:i+3]);
                  value.append(inputBuffer[item]);
                  dict[inputString[i:i+3]]=value;
                  #print "end"
               else:
                   #print "else start"
                   value=[];
                   value.append(inputBuffer[item]);
                   dict[inputString[i:i+3]]=value;
                  #print "else end"
    for i in range(len(misspelledWord)-2):  
        trigram.append(misspelledWord[i:i+3]);
        if dict.get(misspelledWord[i:i+3]) is None:
              continue;
        else:
              mostCloselyRelatedsubSet.append(dict.get(misspelledWord[i:i+3]));
 
    return mostCloselyRelatedsubSet;











#Find all the words of the sentence are correct or not 
def sentenceCorrection(incorrect_sentence):
    
    words=[];
    unigram_dict={};
    bigram_dict={};
    flgAllCorrectWords = True;
    incorrectWord="";
    substitutedSentence="";
    sumBaseCount=0;
    finalProbability=1.0;
    verySmallValue=.000001;
    outputDict={};

    for word in incorrect_sentence.split():
          words.append(word);
    print words;
        
    with open("../data/wordlist.txt") as f:
        inputBuffer = f.readlines()
        inputBuffer = [x.strip() for x in inputBuffer]
        
        # you may also want to remove whitespace characters like `\n` at the end of each line
    with open("../data/count_1w100k.txt") as f:
        for line in f:
            items = line.split();
            unigram_dict[items[0]] = items[1]    
    #print unigram_dict.keys();   
    #print inputBuffer
    for word in words:
            returnVal = word in unigram_dict.keys()
            print "**********"
            print word
            print returnVal
            if returnVal:
                flgAllCorrectWords= flgAllCorrectWords & returnVal;
            else:
                incorrectWord=word;
                flgAllCorrectWords= flgAllCorrectWords & returnVal;
    
    if(flgAllCorrectWords):
         outputDict["All words are correct"]=1;
         return outputDict;
    else:
        #Get the candidates for the incorrect word
        print incorrectWord
        closelyRelatedWords=[];
        print getSubSet(incorrectWord);
        closelyRelatedWords=getSubSet(incorrectWord.lower()); #Code has to be updated
        for i in range(len(closelyRelatedWords)):
            for j in range(len(closelyRelatedWords[i])):
                print "Closely related words"
                print closelyRelatedWords[i][j]    
        #Check the probability for sntence level correctness
               
        #Steps:
        #1:Create a dictionary with bigram and count
        with open("../data/count_2w.txt") as f:
            for line in f:
                items = line.split();
                bigram_dict[items[0]+" "+items[1]] = items[2]
        
        
        #Find the sum of all the counts
        for val in bigram_dict.values():
            sumBaseCount=sumBaseCount+ int(val);
                                          
        print sumBaseCount
        #Substitute the closelyRelatedWords in the sentence
        for i in range(len(closelyRelatedWords)):
            for j in range(len(closelyRelatedWords[i])):
           # print closelyRelatedWords[i][j]
               substitutedSentence = incorrect_sentence.replace(incorrectWord,closelyRelatedWords[i][j]);
               #2:Find the individual probability
               substitutedSentence=substitutedSentence.lower();
               print substitutedSentence
               splited_Sentence= substitutedSentence.split();
               #print len(splited_Sentence);
               k=0;
               print "Exec started"
               for k in range(len(splited_Sentence)):
                   print k
                   if k==0:
                       
                       if (bigram_dict.has_key(splited_Sentence[0])):
                           print "For k=0"
                           print "found****"
                           print splited_Sentence[0];
                           print finalProbability
                           finalProbability= float(bigram_dict.get(splited_Sentence[0]))/sumBaseCount;             
                       else:
                           print "Not found****"
                           finalProbability=verySmallValue;
                       
                   else:
                       if (bigram_dict.has_key(splited_Sentence[k-1]+" "+splited_Sentence[k])):
                           print "found"
                           print splited_Sentence[k-1]+" "+splited_Sentence[k];
                           print float(bigram_dict.get(splited_Sentence[k-1]+" "+splited_Sentence[k]))/sumBaseCount;
                           finalProbability= finalProbability * float(bigram_dict.get(splited_Sentence[k-1]+" "+splited_Sentence[k]))/sumBaseCount; 
                       else:
                           print "Not found"
                           print splited_Sentence[k-1]+" "+splited_Sentence[k];
                           finalProbability=finalProbability * verySmallValue;
                           print finalProbability
               if k!=0:
                   print "final value:"
                   print finalProbability;
                   outputDict[substitutedSentence]=finalProbability;
               
                   
              #3:Calculate the final probability
              #4:Suggest the correct senctence
    #print unigram_dict    
    #print bigram_dict     
    print outputDict;
    sorted_x = sorted(outputDict.items(), key=operator.itemgetter(1),reverse=True)       
    print "Suggested words using edit distance:"  
    print '\n\n\n'     
    print sorted_x;
    return sorted_x[0:5];
#sentenceCorrection("I AM WATCHING A MAGH")
#Return the top 3 Sentence 
