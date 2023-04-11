from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
# driver = webdriver.Firefox(executable_path=r'geckodriver.exe', options=options)
driver = webdriver.Firefox(options=options)

# driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("python")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()