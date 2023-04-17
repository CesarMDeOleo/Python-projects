def combos(Fiveletterword):
    words = []
    for i in range(len(Fiveletterword)):
        for j in range(len(Fiveletterword)):
            for k in range(len(Fiveletterword)):
                if len(set([i, j, k])) == 3:
                    words.append(Fiveletterword[i]+Fiveletterword[j]+Fiveletterword[k])
    return words


Fiveletterword = input("Please enter a five-letter word: ")
print("The possible combinations of letters are: ")
print(combos(Fiveletterword))