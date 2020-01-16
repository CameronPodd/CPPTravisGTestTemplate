import os
from lib import goToProjectRootDir, cmake

def main():
    goToProjectRootDir()
    cmake()
    os.system("ctest -VV")

if __name__ == "__main__":
    main()
