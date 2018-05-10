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
driver.find_element_by_xpath("""//*[@id="placesList"]/ul/li[11]/a""").click()
driver.find_element_by_xpath("""//*[@id="main"]/table[1]/tbody/tr/td[2]/a[2]/i""").click()
driver.find_element_by_xpath("""//*[@id="main"]/center[2]/a[6]""").click()