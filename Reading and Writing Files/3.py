inputFile = open('names.txt', 'r')
outputFile = open('names-formatted.txt', 'w')

for i in inputFile:
    outputFile.write(i.title())

inputFile.close()
outputFile.close()
