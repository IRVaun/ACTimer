@echo off
echo Building ACTimer executable...
py -m PyInstaller ACTimer.spec --clean
echo.
echo Build complete! Executable is in dist\ACTimer.exe
pause
