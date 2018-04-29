def loadFile(item):
    with open('example_project/' + item + '.md') as file:
        for line in file:
            readLine(line)

def readLine(line):
    if line[:2] == '# ':
        tex = '\n' + '\chapter{' + line[2:] + '}' + '\n'
        writeOutput(tex)
    if line[:3] == '## ':
        tex = '\n' + '\section{' + line[3:] + '}' + '\n'
        writeOutput(tex)

def writeOutput(line):
    with open('build.tex', "a") as file:
        file.write(line)

