from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By

def values(candles, index):
    data = candles[index].get_attribute("d").split()
    color = candles[index].get_attribute("fill")
    if color == "#32ea32":
        color = "g"
    else:
        color = "r"
    return {"high": data[2], "low": data[5], "color": color, "index": index}


driver = webdriver.Chrome('C:/Users/M1039303/Downloads/chromedriver_win32 (1)/chromedriver.exe')
driver.get("https://in.investing.com/stock-screener/")

def start(name):
    search_tab = driver.find_element_by_xpath("//*[@id='searchTextTop']")
    search_tab.send_keys(name)
    time.sleep(5)
    search_tab.send_keys(Keys.ENTER)

    time.sleep(4)
    candle_tab = driver.find_element_by_xpath("//*[@id='js_instrument_chart_wrapper']/div[1]/ul[1]/li[1]/a")
    candle_tab.click()

    time.sleep(5)
    candle_list = driver.find_elements(By.TAG_NAME,"path")

    last_candle = values(candle_list, 85)
    status = True
    last_green = {}
    middle_candles = []
    index = 85

    while(status):
        last_green = values(candle_list,index)
        index = index - 1
        if last_green.get("color") == "g":
            status = False
        elif index == 0:
            status = False
        else:
            middle_candles.append(last_green)
    print("last green: ", last_green)
    print("middle: ", middle_candles)
    if len(middle_candles) != 0:
        for each in middle_candles:
            if (last_green.get("low") > each.get("low")) and (each.get("color") == "r"):
                print("bearish")

    if (last_green.get("low") > last_candle.get("low")) and (last_candle.get("color") == "r"):
        print("bearish")

if __name__ == "__main__":
    start("Tata Consultancy")