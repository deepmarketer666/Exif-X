import os
windows = os.name == 'nt'
python = input("Python3 are installed as (python/python3): ")
os.system(f"{python} -m pip install -r requirements.txt")
if not windows:
    os.system('mkdir /usr/share/exifx')
    os.system('cp -r * /usr/share/exifx')
    os.system('ln -s /usr/share/exifx/exifx.py /usr/bin/exifx')
else:
    os.system("mkdir C:\\exifx")
    os.system("copy * C:\\exifx")
    os.system("mkdir C:\\exifx\\include")
    os.system("copy include C:\\exifx\\include\\")
    os.system("echo @echo off > C:\\Windows\\System32\\exifx.bat")
    os.system(f"echo {python} C:\\exifx\\exifx.py %* >> C:\\Windows\\System32\\exifx.bat")

print("[+]Exifx installed!")
