
import idDict

blankDict = {}
_subjectIndex = 1

def generateBlankDict():
    dict = {}
    blankFile = open( 'file_test\\'+str(_subjectIndex)+'_blank.txt')
    blankContent = blankFile.read()
    linesTemp = blankContent.split('\n')
    for line in linesTemp:
        list = line.split('\t')
        if len(list) < 4:
            continue
        listNoPic = list[:3]
        key = ('-').join(listNoPic)
        value = list[3]
        dict[key] = value
    blankFile.close()
    return dict

def checkScore(idDict, cardDict, blankDict):
    newList = []
    allBlankList = []
    scoreFile = open( 'file_test\\'+str(_subjectIndex)+'_score.txt')
    newFile = open( 'file_test\\'+str(_subjectIndex)+'_blank_has_score.txt', 'w')
    allBlankFile = open( 'file_test\\'+str(_subjectIndex)+'_test_all_blank.txt', 'w')
    content = scoreFile.read()
    linesTemp = content.split('\n')
    index = 0
    lineCount = len(linesTemp)

    for keyDict in cardDict.keys():
        min=999999
        minValue=-1
        for value in cardDict.values():
            count=0
            for line in linesTemp:
                index = index + 1
                #if index % 1000 == 0:
                    #print str(index) + '/' + str(lineCount)
                list = line.split('\t')
                if len(list) < 4:
                    continue
                id = idDict[list[0]]
                cardDictKey = list[2]
                if not cardDictKey==keyDict:
                    continue
                if not cardDict.has_key(cardDictKey):
                    continue
                #cardId = cardDict[cardDictKey]
                cardId = value
                # cardId = list[2]
                key = id + '-' + list[1] + '-' + cardId
                if blankDict.has_key(key):
                    allBlankList.append(id + '\t' + list[2] + '\t' + list[3])
                    if float(list[3]) != 0.0:
                        newLine = id + '\t' + list[0] + '\t' + list[1] + '\t' + cardDictKey + '\t' + list[3] + '\t' + blankDict[key]
                        newList.append(newLine)
                        count = count+1
            if min > count:
                min = count
                minValue = value
                print 'key:',keyDict,' ','value:',value,' ',str(min)
            elif count < 20:
                print 'key:', keyDict, ' ', 'value:', value, ' ', str(count)
        print '--------'

    newFile.write('\n'.join(newList))
    allBlankFile.write('\n'.join(allBlankList))
    scoreFile.close()
    newFile.close()
    allBlankFile.close()


idDict, cardDict = idDict.generageIdDict(_subjectIndex)
blankDict = generateBlankDict()
checkScore(idDict, cardDict, blankDict)
