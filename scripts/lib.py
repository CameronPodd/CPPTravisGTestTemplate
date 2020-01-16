import os

def goToProjectRootDir():
    cwd = os.getcwd()
    cwdList = cwd.split('/')
    if cwdList[-1] == "scripts":
        os.chdir("..")

def cmake():
    if not os.path.isdir("build"):
        os.system("mkdir build")
    os.chdir("build")
    os.system("cmake ..")
    os.system("cmake --build .")

