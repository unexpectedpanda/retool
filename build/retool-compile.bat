REM Compile Retool for Windows
pyinstaller -F retool.py
cd dist
del retool-*-win-x86-64.zip
..\build\7z a retool-x.xx-win-x86-64.zip retool.exe
del retool.exe
cd ..