@echo off

echo The file generator will make a
echo Folder Name
echo - static folder
echo    - style.css
echo - templates folder
echo    - index.html
echo - main.py                          (that contains that contains Flask)

set /P name=What will be the name of the folder?

mkdir %name%
cd %name%

echo from flask import Flask > main.py  
echo.  >> main.py
echo app = Flask(__name__) >> main.py
echo.  >> main.py
echo @app.route('/') >> main.py
echo.  >> main.py
echo def index(): >> main.py
echo     return index.html >> main.py
echo.  >> main.py
echo if __name__ == "__main__": >> main.py
echo     app.run(debug=True) >> main.py

mkdir static
mkdir templates

cd static 

echo body { > style.css
echo    background-color: #222831; >> style.css
echo } >> style.css

cd ..
cd templates

echo ^<!DOCTYPE html^> > index.html
echo ^<html lang="en"^> >> index.html
echo ^<head^> >> index.html
echo     ^<meta charset="utf-8"^> >> index.html
echo     ^<meta name="viewport" content="width=device-width, initial-scale=1"^> >> index.html
echo     ^<title^>HTML5 Boilerplate^</title^> >> index.html
echo     ^<link rel="stylesheet" href="styles.css"^> >> index.html
echo ^</head^> >> index.html
echo ^<body^> >> index.html
echo     ^<h1^>Page Title^</h1^> >> index.html
echo ^</body^> >> index.html
echo ^</html^> >> index.html


echo The files had been generated in the %name% folder

pause