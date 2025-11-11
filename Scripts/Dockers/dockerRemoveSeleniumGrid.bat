@echo off
REM Remove Selenium Grid Containers and Network

REM Configuration
SET HUB_NAME=seleniumHub
SET CHROME_NODE_NAME=chromeNode
SET FIREFOX_NODE_NAME=firefoxNode
SET EDGE_NODE_NAME=edgeNode
SET NETWORK_NAME=gridnetwork

echo.
echo   Removing Selenium Grid Containers...
echo.

docker rm -f %HUB_NAME% %CHROME_NODE_NAME% %FIREFOX_NODE_NAME% %EDGE_NODE_NAME% >nul 2>&1
echo Containers removed (if they existed).

echo.
echo   Removing Docker Network...
echo.

docker network rm %NETWORK_NAME% >nul 2>&1
echo Network removed (if it existed).

echo.
echo All Selenium containers and network removed successfully!
pause
