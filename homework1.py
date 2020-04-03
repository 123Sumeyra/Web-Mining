def apriori(D, minSup):

#Creadted a dictionary. if there is in F1 ,increase the number
    F1 = {}
    for T in D:
        for I in T:
            if I in F1:
                F1[I] += 1
            else:
                F1[I] = 1

    print("F1",F1)
    #keys in Dictinory
    _keys1 = F1.keys()


    keys1 = []
    for i in _keys1:
        keys1.append([i])


    n = len(D) #25
    cutKeys1 = []

    for k in keys1:
        if F1[k[0]] * 1.0 / n >= minSup: #compare F1 's value
            cutKeys1.append(k)
        #print(F1[k[0]] )


    cutKeys1.sort()


    keys = cutKeys1



    all_keys = []
    while keys != []:
        C = getC(D, keys)
        cutKeys = getCutKeys(keys, C, minSup, len(D))

        for key in cutKeys:
            all_keys.append(key)
        keys = aproiri_gen(cutKeys)



    return all_keys


def getC(D, keys): #calculate numbers

    C = []
    for key in keys:
        c = 0
        for T in D:
            have = True

            for k in key:
                if k not in T:
                    have = False
            if have:
                c += 1
        C.append(c)

    return C


def getCutKeys(keys, C, minSup, length):

    for i, key in enumerate(keys):
        if float(C[i]) / length < minSup:
            keys.remove(key)
       # print(i,key)  #teklileri sırayla çiftleri ... sırayla sıralıyor ...

    return keys



def keyInT(key, T):

    for k in key:
        if k not in T:
            return False
    return True


def aproiri_gen(keys1):

    keys2 = []
    for k1 in keys1:
        for k2 in keys1:
            if k1 != k2:
                key = []
                for k in k1:
                    if k not in key:
                        key.append(k)
                for k in k2:
                    if k not in key:
                        key.append(k)
                key.sort()
                if key not in keys2:
                    keys2.append(key)

    return keys2
def createData(dataSet):
    with open(dataSet) as f:
        content = f.readlines()

    content = [x.strip().split(",") for x in content]# strip()sondaki endofline kaldırıyor.
    #print(content)
    C = []
    for line in content:
        C.append(line)


    C.sort()

    return C



dataSet = createData("food.txt")
F = apriori(dataSet, 0.5)
print("frequent Itemset:\n", F)
