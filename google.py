
def smallest_alphabet(a, n) :


    min = 'z'

    # Find smallest alphabet
    for i in range (n - 1) :
        if (a[i] < min):
            min = a[i]

            # Returning smallest alphabet
    return min


def Solution( A,B):

    wordsA=A.split(" ")
    wordsB=B.split(" ")
    res=list()

    count=0
    for w in wordsB:
        smallest=smallest_alphabet(w,len(w))
        f1=w.count(smallest)
        for w2 in wordsA:
           smallest2=smallest_alphabet(w2,len(w2))
           f2=w2.count(smallest2)
           if f1>f2:
               count+=1
        res.append(count)
        count=0


    return res


print(Solution("abcd aabc bd","aaa aa"))