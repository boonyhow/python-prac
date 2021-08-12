string = open("sample_article.txt", "r").read()

article = string.replace(',', '')
listOfSentencesForward = article.split(".")
listOfSentencesBackward = article.split(".")
listOfSentencesBackward.reverse()
listOfWords = article.lower().replace(".", "").replace('"', '').split(" ")
listOfUniqueWords = set(listOfWords)

dictionary = {}
for i in listOfUniqueWords:
    dictionary[i] = listOfWords.count(i)

wordOccurences = sorted(dictionary.items(), key=lambda x: (-x[1], x[0]))[:10]

answer = []

for i in wordOccurences:
    answerStructure = {
        "keyword": "",
        "frequency": "",
        "first_time": "",
        "last_time": "",
    }
    answerStructure["keyword"] = i[0]
    answerStructure["frequency"] = i[1]
    for j in listOfSentencesForward:
        wordsInSentence = j.lower().split()
        if i[0] in wordsInSentence:
            answerStructure["first_time"] = j
            break
    for k in listOfSentencesBackward:
        wordsInSentence = k.lower().split()
        if i[0] in wordsInSentence:
            answerStructure["last_time"] = k
            break
    answer.append(answerStructure)

print(answer)
