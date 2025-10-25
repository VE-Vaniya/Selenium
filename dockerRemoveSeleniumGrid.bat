@echo off
REM Remove Selenium Grid Containers and Network

REM Configuration
SET HUB_NAME=selenium-hub
SET CHROME_NODE_NAME=chrome-node
SET FIREFOX_NODE_NAME=firefox-node
SET EDGE_NODE_NAME=edge-node
SET NETWORK_NAME=gridnetwork

docker rm -f %HUB_NAME% %CHROME_NODE_NAME% %FIREFOX_NODE_NAME% %EDGE_NODE_NAME% >nul 2>&1

docker network rm %NETWORK_NAME% >nul 2>&1

echo.
echo All Selenium containers and network stopped successfully!
pause
