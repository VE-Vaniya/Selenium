@echo off
REM Stop and Remove Selenium Grid

REM Configuration
SET HUB_NAME=seleniumHub
SET CHROME_NODE_NAME=chromeNode
SET FIREFOX_NODE_NAME=firefoxNode
SET OPERA_NODE_NAME=operaNode
SET NETWORK_NAME=gridnetwork

echo Stopping and removing Selenium containers...

docker rm -f %HUB_NAME% %CHROME_NODE_NAME% %FIREFOX_NODE_NAME% %OPERA_NODE_NAME% >nul 2>&1

echo Removing Docker network if it exists...
docker network rm %NETWORK_NAME% >nul 2>&1

echo All Selenium containers and network removed successfully!
pause