from bs4 import BeautifulSoup
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://explorer.injective.network/contracts/'
driver = Chrome()  # Vous devez avoir le pilote Chrome (chromedriver) installé et dans le PATH
driver.get(url)

#span class="max-w-[160px] overflow-hidden overflow-ellipsis whitespace-nowrap text-base">Astroport pair</span>

print(elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.max-w-[160px].overflow-hidden.overflow-ellipsis.whitespace-nowrap.text-base'))
))

html = driver.page_source

driver.quit()

soup = BeautifulSoup(html, "html.parser")

print(soup.prettify())

