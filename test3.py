from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--no-sandbox') # Bypass OS security model
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\driver/chromedriver.exe')
driver.get('http://www.python.org')
print(driver.title)
driver.quit()