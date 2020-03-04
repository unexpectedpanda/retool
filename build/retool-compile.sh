# Compile Retool for MacOS
pyinstaller -F retool.py
cd dist
rm retool-*-macos*.zip
zip retool-x.xx-macos-x86-64.zip retool
rm retool
cd ..