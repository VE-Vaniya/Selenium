@echo off
REM Selenium Grid Run Script

REM Configuration
SET HUB_NAME=seleniumHub
SET NETWORK_NAME=gridnetwork
SET HUB_PORT=4445
SET SELENIUM_VERSION=3.141.59

SET CHROME_NODE_NAME=chromeNode
SET CHROME_VNC_PORT=4446

SET FIREFOX_NODE_NAME=firefoxNode
SET FIREFOX_VNC_PORT=4447

SET OPERA_NODE_NAME=operaNode
SET OPERA_VNC_PORT=4448

REM Remove old containers if they exist
docker rm -f %HUB_NAME% %CHROME_NODE_NAME% %FIREFOX_NODE_NAME% %OPERA_NODE_NAME% >nul 2>&1

REM Run Hub
docker run -d -p %HUB_PORT%:4444 --net %NETWORK_NAME% --name %HUB_NAME% selenium/hub:%SELENIUM_VERSION%

REM Run Chrome Node
docker run -d -p %CHROME_VNC_PORT%:5900 --net %NETWORK_NAME% -e HUB_HOST=%HUB_NAME% --name %CHROME_NODE_NAME% selenium/node-chrome-debug:%SELENIUM_VERSION%

REM Run Firefox Node
docker run -d -p %FIREFOX_VNC_PORT%:5900 --net %NETWORK_NAME% -e HUB_HOST=%HUB_NAME% --name %FIREFOX_NODE_NAME% selenium/node-firefox-debug:%SELENIUM_VERSION%

REM Run Opera Node
docker run -d -p %OPERA_VNC_PORT%:5900 --net %NETWORK_NAME% -e HUB_HOST=%HUB_NAME% --name %OPERA_NODE_NAME% selenium/node-opera-debug:%SELENIUM_VERSION%

echo Selenium Grid is running!
echo Open Hub console at: http://localhost:%HUB_PORT%/grid/console
pause
