class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        wordtosimilar={}
        if len(sentence1) != len(sentence2):
            return False
                
        for word1,word2 in similarPairs:
            if word1 not in wordtosimilar:
                wordtosimilar[word1] = set()
            if word2 not in wordtosimilar:
                wordtosimilar[word2] = set()
            
            wordtosimilar[word1].add(word2)
            wordtosimilar[word2].add(word1)
        
        for i in range(len(sentence1)):
            word1=sentence1[i]
            word2=sentence2[i]
            if word1 == word2:
                continue

            if word1 not in wordtosimilar:
                return False
            
            if word2 not in wordtosimilar[word1]:
                return False
                
        return True
