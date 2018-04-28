def loadFile(item):
    with open('example_project/' + item + '.md') as file:
        for line in file:
            readLine(line)

def readLine(line):
    # print line
    if line[0] == '#':
