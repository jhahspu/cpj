import sys
import os
import pathlib

def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

def createLocalPrj(fn):
    fdn = str(pathlib.Path().absolute()) + "\\" + fn
    print('creating project: ' + fn + ' at: ' + fdn)
    os.mkdir(fdn)
    os.chdir(fdn)
    save_to_file("## Hello World \n### Another line...", "readme.md")

if (len(sys.argv) > 3):
    print('creating local project: ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' ' + str(sys.argv[3]))
    createLocalPrj(str(sys.argv[1]))
else:
    print('creating remote project: ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]))

