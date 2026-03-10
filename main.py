import os
from subprocess import call

global dir
global prompt
prompt = []
dir = "/"


def justExecApp():

    try:
        os.chdir(dir)
        call(prompt)
    except:
        print(prompt[0], " don't exist.")


def main():
    global dir

    print("meow")
    while True:
        line = ""
        czyCd = False

        while len(line) == 0:
            print("shellMadeInPython>", end="")
            line = input()

        normalString = ""

        for i in range(len(line)):
            if line[i] != ' ':
                normalString += line[i]
            if i + 1 == len(line) or line[i] == ' ' and normalString != "":
                prompt.append(normalString)
                normalString = ""

        if len(prompt) != 0:
            if prompt[0] == "exit" or prompt[0] == "quit":
                return
            elif prompt[0][0] == '/':
                takCzyNie = True
                try:
                    os.chdir(prompt[0])
                except:
                    takCzyNie = False
                if takCzyNie:
                    dir = prompt[0]
                    dir+='/'
                    czyCd = True
            elif prompt[0][0] == '.':
                doDodania = ""
                for n in range(len(prompt[0])-2):
                    doDodania+=prompt[0][n+2]
                testDir = dir + doDodania + '/'
                takCzyNie = True
                try:
                    os.chdir(testDir)
                except:
                    takCzyNie = False
                if takCzyNie:
                    dir = testDir
                    czyCd = True

            if czyCd == False:
                justExecApp()
            prompt.clear()


# def main
main()