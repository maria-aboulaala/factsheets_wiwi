from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def save_dash_app_as_pdf(url, output_filename):
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--print-to-pdf=' + output_filename)

    # Path to your chromedriver
    driver_path = '/path/to/chromedriver'
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

    # Open the Dash app
    driver.get(url)
    # Give it time to load completely
    driver.implicitly_wait(10)

    # Close the driver
    driver.quit()

# Usage
save_dash_app_as_pdf('http://localhost:8050', 'Factsheet.pdf')
