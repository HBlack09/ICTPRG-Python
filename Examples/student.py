f = open("students.txt", "a")
f.write('Phillip Locke\nDavid Beckett\nEdmund Burke\n')
f.close()
print(open("students.txt", "r").read())
