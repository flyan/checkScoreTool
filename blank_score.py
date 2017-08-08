
import idDict

blankDict = {}
_subjectIndex = 1

def generateBlankDict():
    dict = {}
    blankFile = open( 'file\\'+str(_subjectIndex)+'_blank.txt')
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
    scoreFile = open( 'file\\'+str(_subjectIndex)+'_score.txt')
    newFile = open( 'file\\'+str(_subjectIndex)+'_blank_has_score.txt', 'w')
    allBlankFile = open( 'file\\'+str(_subjectIndex)+'_test_all_blank.txt', 'w')
    content = scoreFile.read()
    linesTemp = content.split('\n')
    index = 0
    lineCount = len(linesTemp)
    for line in linesTemp:
        index = index+1
        if index%1000==0:
            print str(index)+'/'+str(lineCount)
        list = line.split('\t')
        if len(list) < 4:
            continue
        id = idDict[list[0]]
        if not cardDict.has_key(list[2]):
            continue
        cardId = cardDict[list[2]]
        #cardId = list[2]
        key = id + '-' + list[1] + '-' + cardId
        if blankDict.has_key(key):
            allBlankList.append(id+'\t'+list[2]+'\t'+list[3])
            if float(list[3]) != 0.0:
                newLine = id+'\t'+list[0]+'\t'+list[1]+'\t'+list[2]+'\t'+list[3]+'\t'+blankDict[key]
                newList.append(newLine)
    newFile.write('\n'.join(newList))
    allBlankFile.write('\n'.join(allBlankList))
    scoreFile.close()
    newFile.close()
    allBlankFile.close()


idDict, cardDict = idDict.generageIdDict(_subjectIndex)
blankDict = generateBlankDict()
checkScore(idDict, cardDict, blankDict)
