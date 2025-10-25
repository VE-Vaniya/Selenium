@echo off
REM Selenium Grid Pull Script

REM Configuration
SET SELENIUM_VERSION=3.141.59

REM Pull Hub
echo Pulling Selenium Hub %SELENIUM_VERSION%...
docker pull selenium/hub:%SELENIUM_VERSION%

REM Pull Nodes
echo Pulling Chrome Node %SELENIUM_VERSION%...
docker pull selenium/node-chrome-debug:%SELENIUM_VERSION%

echo Pulling Firefox Node %SELENIUM_VERSION%...
docker pull selenium/node-firefox-debug:%SELENIUM_VERSION%

echo Pulling Opera Node %SELENIUM_VERSION%...
docker pull selenium/node-opera-debug:%SELENIUM_VERSION%

echo All images pulled successfully!