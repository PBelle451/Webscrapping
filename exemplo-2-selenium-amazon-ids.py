from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://www.amazon.com.br/gp/bestsellers/?ref_=nav_cs_bestsellers")

ids = driver.find_elements(By.XPATH, '//*[@id]')
for ii in ids:
    #print ii.tag_name
    print(ii.get_attribute('id'))    # id name as string

driver.quit()