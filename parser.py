def loadFile(item):
    with open('example_project/' + item + '.md') as file:
        for line in file:
            readLine(line)

def readLine(line):
    if line[:2] == '# ':
        writeOutput('\n' + '\chapter{' + line[2:] + '}' + '\n')
    if line[:3] == '## ':
        writeOutput('\n' + '\section{' + line[3:] + '}' + '\n')
    if line[:4] == '### ':
        writeOutput('\n' + '\subsection{' + line[3:] + '}' + '\n')
    if line[:5] == '#### ':
        writeOutput('\n' + '\header{' + line[3:] + '}' + '\n')

def writeOutput(line):
    with open('build.tex', "a") as file:
        file.write(line)

