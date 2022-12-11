import sys
import os

def sysinfo():
    print(sys.platform)
    print(os.getlogin())
    print(os.getcwd())

sysinfo()