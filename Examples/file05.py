# Read students.txt in and print the file
infile = open('students.txt','r')
filedata = infile.read()
print(filedata)
infile.close()