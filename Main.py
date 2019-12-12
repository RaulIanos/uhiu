from FileService import  File
import random

codeFile = File ("code.txt")
inputFile = File("input.txt")
outputFile = File("output.txt")

text_to_code = inputFile.readInput()

code = codeFile.readFile()

encodeList = {}
decodeList = {}

for l in code:
    encodeList[l[0]] = l[1]
    decodeList[l[1]] = l[0]

print("Do you want to encode or decode?\n    For encoding press 1\n"
                   "    For decoding press 2\n"
                   "    For exiting press 0\n")

while True:
    option = input()
    if option == '1':
        outputFile.useCript(text_to_code, encodeList)
    elif option =='2':
        outputFile.useDecript(decodeList)
    elif option == 'SecretCommand':
        codeList= []
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for letter in alphabet:
            while True:
                s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                passlen = 15
                p =  "".join(random.sample(s,passlen ))
                if p not in decodeList:
                    encodeList[letter] = p
                    decodeList[p]= letter
                    codeList.append(str(letter) + " " +str(p)+"\n")
                    break
        codeFile.writeToFile(codeList)
    elif option == '0':
        exit()
    else:
        print("You are a dumbfuck!")