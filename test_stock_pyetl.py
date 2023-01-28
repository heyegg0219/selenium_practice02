from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


twstock_code = input(str("請輸入股票代號:"))
options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)

chrome.get("https://histock.tw/")
chrome.find_element(By.ID, "tbxStock").send_keys(twstock_code)
chrome.find_element(By.ID, "btnGo").send_keys(Keys.ENTER)
time.sleep(0.5)

chrome.get("https://histock.tw/stock/tchart.aspx?no=" + twstock_code)
time.sleep(3)
chrome.execute_script('window.scrollTo(0, 500)')
stock_chart = chrome.find_element(By.ID, "twDayK_tv")
action = ActionChains(chrome)
action.move_to_element(stock_chart).perform()
chrome.get_screenshot_as_file("./static/" + twstock_code + "candlestick_chart" + ".png")

chrome.quit()
