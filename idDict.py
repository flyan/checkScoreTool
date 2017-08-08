
def generageIdDict(subjectIndex):
    idDict = {}
    cardDict = {}

    idFile = open('file_test\\'+'id_replace.txt')
    content = idFile.read()
    lines = content.split('\n')
    for line in lines:
        list = line.split('\t')
        if len(list) < 2:
            continue
        idDict[list[0]] = list[1]
    idFile = open( 'file_test\\'+str(subjectIndex)+'_card_replace.txt')
    content = idFile.read()
    lines = content.split('\n')
    for line in lines:
        list = line.split('\t')
        if len(list) < 2:
            continue
        cardDict[list[0]] = list[1]
    idFile.close()
    return idDict, cardDict