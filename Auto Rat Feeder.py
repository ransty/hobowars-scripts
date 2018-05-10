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
driver.find_element_by_xpath("""//*[@id="placesList"]/ul/li[7]/a""").click()
first_rat = driver.find_element_by_xpath("""//*[@id="main"]/table/tbody/tr[2]/td[6]/font""").get_attribute("innerHTML")
second_rat = driver.find_element_by_xpath("""//*[@id="main"]/table/tbody/tr[4]/td[6]/font""").get_attribute("innerHTML")
firstRatMeals = int(first_rat)
secondRatMeals = int(second_rat)
print("The first rat has " , first_rat , " meals left")
print("The second rat has " , second_rat , " meals left")
print("Attempting to feed first rat")
if firstRatMeals > 0:
	print("Feeding rat...")
	driver.find_element_by_xpath("""//*[@id="main"]/table/tbody/tr[3]/td[3]/ul/li[1]/a""").click()
	for x in range(0, firstRatMeals):
		driver.find_element_by_xpath("""//*[@id="main"]/table/tbody/tr[3]/td[2]/ul/li[1]/a""").click()
else:
	print("Cannot feed rat - Has no meals")
print("Attempting to feed second rat")
if secondRatMeals > 0:
	print("Feeding rat...")
	driver.find_element_by_xpath("""//*[@id="main"]/table/tbody/tr[5]/td[3]/ul/li[1]/a""").click()
	for x in range(0, secondRatMeals):
		driver.find_element_by_xpath("""//*[@id="main"]/table/tbody/tr[5]/td[2]/ul/li[1]/a""").click()
else:
	print("Cannot feed rat - Has no meals")

print("Automation Complete -- Rats have been fed")