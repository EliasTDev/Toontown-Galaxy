@echo off

title Toontown Galaxy Alpha Game Launcher

echo Choose your connection method!
echo.
echo #1 - Localhost
echo #2 - Development Server
echo #3 - Custom
echo #4 - Local RemoteDB
echo #5 - Production Server
echo.

:selection

set INPUT=-1
set /P INPUT=Selection: 

if %INPUT%==1 (
    set TTG_GAMESERVER=127.0.0.1
) else if %INPUT%==2 (
    set TTG_GAMESERVER=52.147.202.54
) else if %INPUT%==4 (
    set TTG_GAMESERVER=127.0.0.1
) else if %INPUT%==5 (
    SET TTG_GAMESERVER=gameserver.toontowngalaxy.com
) else if %INPUT%==3 (
    echo.
    set /P TTG_GAMESERVER=Gameserver: 
) else (
	goto selection
)

echo.

if %INPUT%==2 (
    set /P TTG_PLAYCOOKIE="Username: "
) else if %INPUT%==4 (
    set /P ttgUsername="Username: "
    set /P ttgPassword="Password: "
) else (
    set /P TTG_PLAYCOOKIE=Username: 
)

echo.

echo ===============================
echo Starting Toontown Galaxy...
echo ppython: "dependencies/panda/python/ppython.exe"

if %INPUT%==2 (
    echo Username: %TTG_PLAYCOOKIE%
) else if %INPUT%==4 (
    echo Username: %ttgUsername%
) else (
    echo Username: %TTG_PLAYCOOKIE%
)

echo Gameserver: %TTG_GAMESERVER%
echo ===============================

cd ../../
"dependencies/panda/python/ppython.exe" -m pip install -r requirements.txt
:main
if %INPUT%==2 (
    "dependencies/panda/python/ppython.exe" -m toontown.toonbase.ToontownStart
) else if %INPUT%==4 (
    "dependencies/panda/python/ppython.exe" -m toontown.toonbase.ToontownStartRemoteDB
) else (
    "dependencies/panda/python/ppython.exe" -m toontown.toonbase.ToontownStart
)
pause

goto main
