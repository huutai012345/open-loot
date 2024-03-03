from scrapy.http import Request, Response
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ['https://selenium-python.readthedocs.io/waits.html']
    
    def __init__(self):
        self.driver = webdriver.Firefox()
    
    # def parse(self, response):
    #     print(response.xpath("//div[contains(@class, 'css-8j0cob')]").get())
    #     yield {
    #         'total_price': response.xpath("//div[contains(@class, 'css-1s31xgj')]/text()").get(),
    #         'max_supply': response.xpath("//p[contains(@class, 'chakra-text css-eiaj9i')]/text()").get(),
    #         'item_name': response.xpath("//h6[contains(@class, 'chakra-text css-1ndsgfx')]/text()").get(),
    #         'game_name': response.xpath("//p[contains(@class, 'chakra-text css-1ndsgfx')]/text()").get(),
    #     }
    
    def parse(self, response):
        self.driver.get("https://openloot.com/items/BT0/Hourglass_Common")

        # Wait for the page to load
        # try:
        element1 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//h6[@class="chakra-heading css-we454d"]'))
            )
        # finally:
        #     self.driver.quit()
           
        # Now you can use Selenium to interact with the page
        print(element1.text)