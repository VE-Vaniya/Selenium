java -Dwebdriver.chrome.driver=C:\WebDriver\bin\chromedriver.exe ^
-jar D:\Selenium_Grid\selenium-server-4.38.0.jar node ^
--port 5556 ^
--publish-events tcp://192.168.18.38:4442 ^
--subscribe-events tcp://192.168.18.38:4443
