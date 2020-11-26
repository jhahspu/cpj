import sys
import os
import pathlib
import time

def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

def createLocalPrj(fn, pt):
    fdn = str(pathlib.Path().absolute()) + "\\" + fn
    print('creating project: ' + fn + ' at: ' + fdn)
    if (pt == 'html'):
        os.mkdir(fdn)
        os.chdir(fdn)
        save_to_file("## Title\n\n\n### Sub title\n\n- List\n- \n- \n\n```json\n{\n\t'key' : 'val'\n}\n```\n\n\n", "readme.md")
        save_to_file("$main-0: hsla(0, 0, 2%, 1);\n$main-1: hsla(0, 0, 12%, 1);\n$main-2: hsla(0, 0, 22%, 1);\n$main-3: hsla(0, 0, 32%, 1);\n$main-4: hsla(0, 0, 42%, 1);\n$main-5: hsla(0, 0, 52%, 1);\n$main-6: hsla(0, 0, 62%, 1);\n$main-7: hsla(0, 0, 72%, 1);\n$main-8: hsla(0, 0, 82%, 1);\n$main-9: hsla(0, 0, 92%, 1);\n$acc: #04a2e4;\n \n$text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.4);\n@mixin container {\n\twidth: 87%;\n\tmax-width: 1024px;\n\tmargin: 0 auto;\n\t@media ( max-width: 45rem) {\n\t\twidth: 90%;\n\t}\n}\n\n@mixin btn {\n\tbackground-color: $acc; \n\tpadding: 0.3rem 0.8rem; \n\tborder-radius: 4px; \n\ttransition: filter 0.2s ease-in-out; \n\t&:hover {\n\t\tfilter: brightness(0.86); \n\t}\n} \n\n*, *::before, *::after {\n\tmargin: 0;\n\tpadding: 0;\n\tbox-sizing: border-box;\n}\n\n:root {\n\tbackground-color: $main-1;\n\tcolor: $main-9;\n\tfont-size: 18px;\n\tfont-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;\n}\n\n", "style.scss")
        save_to_file("// index.js \n\n\n\n", "index.js")
        save_to_file('<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<link rel="stylesheet" href="styles.min.css">\n\t<title>TITLE</title>\n</head>\n<body>\n<h1>Hello World !</h1>\n\n\n\n\n<script src="index.js"></script>\n</body>\n</html>', "index.html")
        os.system('git init')
        time.sleep(3)
        os.system('git add .')
        time.sleep(3)
        os.system('git commit -m "first commit"')
        time.sleep(3)
        os.system('code .')
        print("setup finished...")
        time.sleep(5)

if (len(sys.argv) > 3):
    print('creating local project: ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' ' + str(sys.argv[3]))
    createLocalPrj(str(sys.argv[1]), str(sys.argv[2]))
else:
    print('creating remote project: ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]))

