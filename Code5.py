def most_frequent(word):
    d=dict()
    word=word.lower()
    for key in word:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    print ("The frequency of letters in the decreasing order: ")
    d_sorted = sorted(d, key=d.get, reverse=True)
    for r in d_sorted:
        print(r,"=",d[r])
            
word = input("Please enter a string: ")

most_frequent(word)
