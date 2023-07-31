from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from time import sleep


def get_dawn_columns():
    url = "https://www.dawn.com/newspaper/column"

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    #driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


    driver.get(url)

    article_count = 10
    arts = []

    for i in range(1, article_count+1):
        # Get the i'th article
        art_name = driver.find_element(By.XPATH, f"//article[{i}]/h2").text
        art_author = driver.find_element(By.XPATH, f"//article[{i}]/span/a").text

        arts.append([art_name, art_author])
    
    driver.close()
    return arts
