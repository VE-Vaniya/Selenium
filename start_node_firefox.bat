java -Dwebdriver.gecko.driver=C:\WebDriver\bin\geckodriver.exe ^
-jar D:\Selenium_Grid\selenium-server-4.38.0.jar node ^
--port 5557 ^
--publish-events tcp://192.168.18.38:4442 ^
--subscribe-events tcp://192.168.18.38:4443
