import pickle

class File(object):

    def __init__(self, fileName):
        self.fileName = fileName

    def readInput(self):
        result = []
        f = open(self.fileName)
        result = f.read()
        return result

    def readFile(self):
        result = []
        f = open(self.fileName)
        line = f.readline().strip()
        while len(line) > 0:
            line = line.split(" ")
            result.append(line)
            line = f.readline().strip()
        f.close()
        return result

    def writeToFile(self, list):
        f = open(self.fileName, "w")
        for entity in list:
            f.write(entity)
        f.close()

    def writeToBinaryFile(self, list):
        f = open(self.fileName, "wb")
        pickle.dump(list, f)
        f.close()

    def readBinaryFile(self):
        try:
            f = open(self.fileName, "rb")
            return pickle.load(f)
        except EOFError:
            return []

    def useCript(self,text,encodeList):
        finalCode = []
        for word in text:
            for letter in word:
                if letter.lower().isalpha():
                    finalCode.append( str(encodeList[letter.lower()]))
                else:
                    finalCode.append( letter.lower())
        self.writeToBinaryFile(finalCode)

    def useDecript(self,decodeList):
        finalCode = self.readBinaryFile()
        result= []
        for code in finalCode:
            if code in decodeList:
                result.append(decodeList[code])
            else:
                result.append(code)
        self.writeToFile(result)