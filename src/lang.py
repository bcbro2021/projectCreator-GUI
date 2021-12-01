import sys,os

python = ["""import src\nsrc.main()""",
          """import sys, os\n\ndef main():\n    print('Hello World')"""]

def pyLang(name,type,path):
    os.chdir(path)
    try:
        os.mkdir(name)
        os.chdir(name)
    except FileExistsError:
        sys.exit()

    with open(f"{name}.py", "w") as mainFile:
        mainFile.write(python[0])

    os.mkdir("src")
    os.chdir("src")

    if type == "Empty":
        with open("__init__.py", "w") as initFile:
            initFile.write("from .main import *")
        with open("main.py", "w") as file:
            file.write(python[1])

def cppLang(name,type,path):
    os.chdir(path)
    #creates the first folder
    try:
        os.mkdir(name)
        os.chdir(name)
    except FileExistsError:
        sys.exit()

    if type == "Empty":
        with open(f"main.cpp", "w") as MainFile:
            MainFile.write('#include <iostream>\n\nusing namespace std;\n\nint main(){\n    cout << "Hello World" << endl;\n    return 0;\n}')

        with open("build.sh", "w") as buildFile:
            buildFile.write(f'g++ -o main main.cpp\n./main')
            os.system("chmod u=rwx,g=r,o=r build.sh")
