import os
import shutil
import subprocess
#try:
#    import PyInstaller.__main__
#except ImportError:
#    os.system('python3 -m pip install pyinstaller')
#
#import PyInstaller.__main__

def createStartFile():
    pass
    #with open("safe_start.py", "w") as file:
    #    file.write('import src.levenstein as lev; lev.main()')


def install():
    #PyInstaller.__main__.run(['--onefile', '--clean', 'safe_start.py'])
    #string = "pyinstaller --onefile --clean safe_start.py"
    string = "gcc -Wall -o Levenstein main.c -lfoo "
    subprocess.run(string, shell=True)


def move():
    shutil.move("./dist/safe_start", "./safe_start")


def clean():
    #os.remove("./safe_start.py")
    shutil.rmtree("./build")
    shutil.rmtree("./dist")
    os.remove("./safe_start.spec")


def main():
    createStartFile()
    install()
    move()
    clean()


if __name__ == "__main__":
    main()
