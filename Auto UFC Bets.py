from selenium import webdriver

chrome_path = r"C:\Users\user\Desktop\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
print("Logging in...")
driver.get("http://hobowars.com")
driver.find_element_by_xpath("""//*[@id="login"]""").click()
driver.find_element_by_xpath("""//*[@id="login"]""").send_keys("purplerober")
driver.find_element_by_xpath("""//*[@id="password"]""").click()
driver.find_element_by_xpath("""//*[@id="password"]""").send_keys("e8iopqas")
driver.find_element_by_xpath("""//*[@id="submitLogin"]""").click()
print("Loading betting page...")
driver.find_element_by_xpath("""//*[@id="placesList"]/ul/li[16]/a""").click()
driver.find_element_by_xpath("""//*[@id="checkAll"]""").click()
driver.find_element_by_xpath("""//*[@id="main"]/form/table[29]/tbody/tr/td[1]/input""").click()
print("UFC Betting Complete")