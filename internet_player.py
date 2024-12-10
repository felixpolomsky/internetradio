from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-background-timer-throttling")
options.add_argument("--disable-backgrounding-occluded-windows")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-gpu")
options.add_argument("--disable-infobars")
options.add_argument("--disable-features=EnableAutomation")
options.add_argument("--disable-logging")

driver = webdriver.Chrome(service=Service("/bin/chromedriver"), options=options)
driver.maximize_window()
driver.get("https://www.thfradio.de/de")

time.sleep(2)

play_button = driver.find_element(By.XPATH, "//button[@aria-label='Play Live Broadcast']")
driver.execute_script("arguments[0].scrollIntoView();", play_button)

is_visible = driver.execute_script("return arguments[0].offsetParent !== null;", play_button)

play_button.click()

time.sleep(1800)

driver.quit()
