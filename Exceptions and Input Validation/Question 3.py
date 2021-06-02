def GetWordsFromUser(min, max):
    wordList = []

    while len(wordList) not in range(min, (max + 1)):
        words = input("Enter some words: ")
        for i in words.lower().split(" "): wordList.append(i)

    print(wordList)

GetWordsFromUser(8, 15)
