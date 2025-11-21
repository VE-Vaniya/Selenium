java -Dwebdriver.edge.driver=C:\WebDriver\bin\msedgedriver.exe ^
-jar C:\Users\ahmad\PycharmProjects\Selenium\selenium-server-4.38.0.jar node ^
--port 5558 ^
--publish-events tcp://172.23.16.1:4442 ^
--subscribe-events tcp://172.23.16.1:4443
