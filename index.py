from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import model
# import sys

# sys.setProperty("webdriver.gecko.driver", "C:/Users/M1039303/Downloads/geckodriver-v0.21.0-win64")
driver = webdriver.Chrome('C:/Users/M1039303/Downloads/chromedriver_win32 (1)/chromedriver.exe')
driver.get("https://in.investing.com/stock-screener/")
assert "Investing" in driver.title

#selecting technical tab
try:
    tech_tab = driver.find_element_by_xpath("//*[@id='stockScreenerResultsTabs']/li[3]/a")
    tech_tab.click()
except: 
    tech_tab = driver.find_element_by_xpath("//*[@id='stockScreenerResultsTabs']/li[3]")
    tech_tab.click()
    

#selecting Market Cap
eq_market_cap = driver.find_element_by_xpath("//*[@id='directoryFilter']/a[2]")
actions = ActionChains(driver)
actions.move_to_element(eq_market_cap).perform()
eq_market_cap.click()

# select exchange
exchange = driver.find_element_by_xpath("//*[@id='exchange']")
exchange.click()

nse = driver.find_element_by_xpath("//*[@id='exchangesUL']/li[3]")
nse.click()

time.sleep(5)
name=[]
table = driver.find_element_by_id("resultsTable")
tr = table.find_elements_by_tag_name("tr")
i=1
TRADE = "Strong Buy"
for each in tr:                           
    name = each.find_element_by_xpath("//*[@id='resultsTable']/tbody/tr["+str(i)+"]/td[2]").text
    fifteen_min = each.find_element_by_xpath("//*[@id='resultsTable']/tbody/tr["+str(i)+"]/td[19]").text
    hour = each.find_element_by_xpath("//*[@id='resultsTable']/tbody/tr["+str(i)+"]/td[20]").text
    daily = each.find_element_by_xpath("//*[@id='resultsTable']/tbody/tr["+str(i)+"]/td[21]").text
    weekly = each.find_element_by_xpath("//*[@id='resultsTable']/tbody/tr["+str(i)+"]/td[22]").text
    monthly = each.find_element_by_xpath("//*[@id='resultsTable']/tbody/tr["+str(i)+"]/td[23]").text
    i = i+1
    # print(name, fifteen_min, hour, daily, weekly, monthly, sep="  --) ")
    if(fifteen_min == hour == daily == weekly == monthly == TRADE):
        print(name)
        model.start(name)
    if(i == 50):
        break



















# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# user = "mindtree stock price"
# pwd = "sss"
# driver = webdriver.Chrome('C:/Users/M1039303/Downloads/chromedriver_win32 (1)/chromedriver.exe')
# driver.get("https://www.google.com/")
# assert "Google" in driver.title
# elem = driver.find_element_by_id("lst-ib")
# submit = driver.find_element_by_name("btnK")

# elem.send_keys(user)
# elem.submit()

# lists= driver.find_elements_by_class_name("_Rm")


# print ("Found " + str(len(lists)) + " searches:")

# # iterate through each element and print the text that is
# # name of the search

# i=0
# for listitem in lists:
#    print (listitem.get_attribute("innerHTML"))
#    i=i+1
#    if(i>10):
#       break

# # close the browser window
# driver.quit()
# time.sleep(3000)

# data = driver.find_elements
# print(data)
# driver.close()