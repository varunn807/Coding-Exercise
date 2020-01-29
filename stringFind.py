import itertools
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        answer=[]
        permutations=list(itertools.permutations(words))
        print(permutations)
        length=len(list(itertools.permutations(words)))
        myString=""
        for i in range(length):
            for element in permutations[i]:
                myString=myString+element
            print(myString)
            found=s.find(myString)
            print(found)
            if found>-1:
                answer.append(found)

                myString=""
            myString = ""
        return(list((answer)))






sol=Solution()
"foobarfoobar"
["foo","bar"]


s = "foobarfoobar"
words = ["foo","bar"]
print(sol.findSubstring(s,words))
