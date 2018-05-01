def loadFile(item):
    with open('example_project/' + item) as file:
        if item[-3:] == '.md':
            for line in file:
                readLine(line)
        elif item[-4:] == '.tex':
            with open('example_project/' + item) as input:
                for line in input:
                    writeOutput(line)

def readLine(line):
    if line[:2] == '# ':
        writeOutput('\n' + '\chapter{' + line[2:] + '}' + '\n')
    if line[:3] == '## ':
        writeOutput('\n' + '\section{' + line[3:] + '}' + '\n')
    if line[:4] == '### ':
        writeOutput('\n' + '\subsection{' + line[3:] + '}' + '\n')
    if line[:5] == '#### ':
        writeOutput('\n' + '\header{' + line[3:] + '}' + '\n')
    if line[:2] == '> ':
        writeOutput('\n' + r'\begin{quotebox}' + line[2:] + '\end{quotebox}' + '\n')

def writeOutput(line):
    with open('build.tex', "a") as file:
        file.write(line)

