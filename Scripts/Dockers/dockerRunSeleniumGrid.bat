@echo off
REM Selenium Grid Run Script

REM Configuration
SET HUB_NAME=seleniumHub
SET NETWORK_NAME=gridnetwork
SET HUB_PORT=4444
SET SELENIUM_VERSION=4.10.0

SET CHROME_NODE_NAME=chromeNode
SET FIREFOX_NODE_NAME=firefoxNode
SET EDGE_NODE_NAME=edgeNode

echo.
echo   Starting Selenium Grid %SELENIUM_VERSION%...

REM Create network if not exists
docker network create %NETWORK_NAME% >nul 2>&1

REM Remove old containers if they exist
docker rm -f %HUB_NAME% %CHROME_NODE_NAME% %FIREFOX_NODE_NAME% %EDGE_NODE_NAME% >nul 2>&1

echo.
echo Starting Hub...
docker run -d -p %HUB_PORT%:4444 --net %NETWORK_NAME% --name %HUB_NAME% selenium/hub:%SELENIUM_VERSION%

echo.
echo Starting Chrome Node...
docker run -d --net %NETWORK_NAME% ^
  -e SE_EVENT_BUS_HOST=%HUB_NAME% ^
  -e SE_EVENT_BUS_PUBLISH_PORT=4442 ^
  -e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 ^
  --name %CHROME_NODE_NAME% selenium/node-chrome:%SELENIUM_VERSION%

echo.
echo Starting Firefox Node...
docker run -d --net %NETWORK_NAME% ^
  -e SE_EVENT_BUS_HOST=%HUB_NAME% ^
  -e SE_EVENT_BUS_PUBLISH_PORT=4442 ^
  -e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 ^
  --name %FIREFOX_NODE_NAME% selenium/node-firefox:%SELENIUM_VERSION%

echo.
echo Starting Edge Node...
docker run -d --net %NETWORK_NAME% ^
  -e SE_EVENT_BUS_HOST=%HUB_NAME% ^
  -e SE_EVENT_BUS_PUBLISH_PORT=4442 ^
  -e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 ^
  --name %EDGE_NODE_NAME% selenium/node-edge:%SELENIUM_VERSION%

echo.
echo Selenium Grid is running successfully!
echo Open Hub console at: http://localhost:%HUB_PORT%/
pause
