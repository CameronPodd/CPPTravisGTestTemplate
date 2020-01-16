import os
from subprocess import call
from sys import argv
from lib import goToProjectRootDir, cmake

def main():
    goToProjectRootDir()
    cmake()
    if len(argv) > 1:
        exeTarget = "".join(["./EXE/", argv[1]])
        call([exeTarget])

if __name__ == "__main__":
    main()
