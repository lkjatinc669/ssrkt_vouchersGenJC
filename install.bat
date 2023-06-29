@echo off
echo [91mPlease Connect to Internet Then Press Enter [0m
pause
echo [32mInstalling Modules[0m
pip install -r requirements.txt
echo [32mInstallation Complete[0m
echo [91mChange the Database Constants in the following file [0m
echo [91mFile Path : "receipt-app/statics/dbStatics.json"[0m
echo [91mTry Not to Change the Database Name [0m
echo [91mAfter Changing Run "database.bat"[0m
pause