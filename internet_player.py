from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service("/bin/chromedriver"), options=options)
driver.maximize_window()
driver.get("http://your_url")

time.sleep(2)

play_button = driver.find_element(By.XPATH, "//button[@aria-label='Play Live Broadcast']")
driver.execute_script("arguments[0].scrollIntoView();", play_button)

is_visible = driver.execute_script("return arguments[0].offsetParent !== null;", play_button)

play_button.click()

time.sleep(1800)

driver.quit()
