#!/bin/python3

import collections
from collections import deque
import copy

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):

    if start_word == end_word:
            wordsout = [start_word]
            return wordsout 
    dict1 = open(dictionary_file,'r')
    wordList = [line[0:5] for line in dict1.readlines()]
    
    wordsout = []                                                 
    wordsout.append(start_word)                                   
    que = deque()                                              
    que.append(wordsout)                                        
    while len(que) > 0:                                          
            theobject = que.popleft()                                  
            for i in wordList:                                  
                    if _adjacent(theobject[len(theobject)-1], i):            
                            if i == end_word:
                                    anotherobject = theobject                
                                    anotherobject.append(i)
                                    return(anotherobject)
                                    break                                       
                            someobject = copy.deepcopy(theobject)            
                            someobject.append(i)                       
                            que.append(someobject)                      
                            wordList.remove(i)                                         
                         
                            
                            
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    


def verify_word_ladder(ladder): #worked with friends on this function
    
    if len(ladder) == 0:
            return False    
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    i = 0
    while i < len(ladder)-1:
            if _adjacent(ladder[i], ladder[i+1]) == True:
                    i+=1   
            else:
                    
                    return False
    
    return True
                


def _adjacent(word1, word2):
    count = 0
    length1 = len(word1)
    length2 = len(word2)

    if word1 == word2:
        return False

    if length1 == length2:
        for x,y in zip(word1, word2):
            if x != y:
                count += 1
    if (count ==1):
        return True

    else:
        return False

