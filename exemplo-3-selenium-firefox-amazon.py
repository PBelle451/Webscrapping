from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import json
import csv
import pandas as pd

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
driver = webdriver.Firefox(executable_path=r'geckodriver.exe', options=options)

# driver.get("https://www.amazon.com.br/gp/bestsellers/?ref_=nav_cs_bestsellers")
driver.get("https://www.amazon.com.br/gp/bestsellers/sports/ref=zg_bs_nav_0")

# ids = driver.find_elements(By.XPATH, '//*[@id]')
# for ii in ids:
#     #print ii.tag_name
#     print(ii.get_attribute('id'))    # id name as string

# ids = driver.find_elements(By.CLASS_NAME, '_cDEzb_p13n-sc-css-line-clamp-3_g3dy1')
# id gridItemRoot
ids = driver.find_elements(By.CLASS_NAME, 'zg-grid-general-faceout')

class Product:
  def __init__(self, id, description, imgSrc, price):
    self.id = id
    self.description = description
    self.imgSrc = imgSrc
    self.price = price

productList = []

for ii in ids:
    # print('Produto')
    #print ii.tag_name
    # print(ii.get_attribute('id'))    # id name as string

    idElement = ii.find_element(By.CLASS_NAME, 'p13n-sc-uncoverable-faceout')
    id = idElement.get_attribute('id')
    # print(id)

    descricao = ii.find_element(By.CLASS_NAME, '_cDEzb_p13n-sc-css-line-clamp-3_g3dy1')
    description = descricao.text
    # print(descricao.text)

    imageElement = ii.find_element(By.CLASS_NAME, 'p13n-product-image')
    imgSrc = imageElement.get_attribute('src')
    # print(imageElement.get_attribute('src'))

    priceElement = ii.find_element(By.CLASS_NAME, '_cDEzb_p13n-sc-price_3mJ9Z')
    price = priceElement.text
    # print('preço: ', priceElement.text)

    # children = ii.find_elements(By.XPATH, ".//*")
    # for child in children:
    #     print('filho')
    #     print(child.get_attribute('id'))
    #     print(child.get_attribute('class'))
    #     print(child.get_attribute('innerHTML'))
    #     print(child.get_attribute('value'))
    #     print(child.get_attribute("textContent"))
    #     print(child.get_attribute('href'))
    #     # print(child.getText())
    #     print(child.text)
    #     print('--')
    # print('--------------------------------')

    productList.append(Product(id, description, imgSrc, price))

driver.quit()

# print(len(productList))
jsonStr = json.dumps([obj.__dict__ for obj in productList], ensure_ascii=False)
# print(jsonStr)
jsonFile = open("amzProductList.json", "w", encoding='utf8')
jsonFile.write(jsonStr)
jsonFile.close()


with open('amzProductList.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';')
    for x in productList:
        writer.writerow([x.id, x.description, x.imgSrc, x.price])

myDataFrame = pd.DataFrame([obj.__dict__ for obj in productList])

print (myDataFrame.to_markdown())     