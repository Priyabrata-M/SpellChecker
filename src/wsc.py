# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 00:00:07 2017

@author: madhavi
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def generate_trigram(item):
    list3=[]
    temp2=""
    for i in range(0,len(item)-2):
        temp2=item[i]+item[i+1]+item[i+2]
        list3.append(temp2)
    
    return list3

def editDistDP(str1, str2):
    m=len(str1)
    n=len(str2)
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
 
    # Fill d[][] in bottom up manner
    for i in range(m+1):
        for j in range(n+1):
 
            # If first string is empty, only option is to
            # isnert all characters of second string
            if i == 0:
                dp[i][j] = j    # Min. operations = j
 
            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i
 
            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
 
            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace
 
    return dp[m][n];

def jaccard_similarity(x,y):
    intersection_cardinality=len(set.intersection(*[set(x),set(y)]))
    union_cardinality=len(set.union(*[set(x),set(y)]))
    return intersection_cardinality/float(union_cardinality)

    
def create_inv_index(file_name):
    f=open(file_name,"r")
    data=f.read()
    list1=data.split("\n") 
    word={}
    for item in list1:
        temp=item.split("\t")
        word[temp[0]]=temp[1]
#    print word
    
    
    list2=word.keys()
    list4=[]
    list5=[]
    for item in list2:
        
        if len(item)>=3:
           list4=generate_trigram(item)
           # print list4
        list5.append(list4)
           
   #print list5

       
           
    index={}
    for j in range(0,len(list2)):
        if len(list2[j])>=3:
            index[list2[j]]=list5[j]
   
   
#    print index
    
    inv_index={}
    for i in index:        
        for j in index[i]:
            if j in (inv_index.keys()):
                temp=inv_index[j]
                temp.append(i)
                inv_index[j]=temp
            else:
                inv_index[j]=[i]
                
    
    return inv_index
    
   
    
def return_candidate_correct_words(inv_index, typo):
    trigrams=generate_trigram(typo)
    candidate=[]
    for item in trigrams:
        try:
            words=inv_index[item]
            candidate=candidate+words
        except:
            pass
#    print candidate
    return candidate
    



def correct_words(typo):
    import pickle  
    inv_index=pickle.load(open("../data/inv_index.p","r"))

    print "abhijit"
    candidates=return_candidate_correct_words(inv_index, typo)
#    print candidates
    print len(candidates)
    
    candidate_dict={}
    for item in candidates:
        temp=editDistDP(typo,item)
        candidate_dict[item]=temp
                      
#    print candidate_dict
    
    import operator
    best_words_list = sorted(candidate_dict.items(), key=operator.itemgetter(1), reverse=False)
    
    k=5
    best_words=best_words_list[0:k]
        
    print best_words
    return best_words



if __name__ == "__main__":
    import pickle    
#    inv_index= create_inv_index("../data/unigram.txt")
#    import pickle
#    pickle.dump(inv_index, open("../data/inv_index.p",'w'))
    inv_index=pickle.load(open("../data/inv_index.p","r"))
#    print correct_words("APLE")

                
        
#        

