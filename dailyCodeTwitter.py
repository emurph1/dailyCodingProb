query= "de"
words = ["dog", "deer", "deal"]
newWords = []
def findW(que):
    for item in words:
        if item[:len(que)] == que:
            newWords.append(item)
    return newWords
print(findW(query))