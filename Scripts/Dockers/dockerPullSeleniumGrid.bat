@echo off
REM Selenium Grid Pull Script

SET SELENIUM_VERSION=4.10.0

echo Pulling Files for %SELENIUM_VERSION%...
docker-compose up -d
echo All images pulled successfully!
