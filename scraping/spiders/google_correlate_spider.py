import scrapy

class BaseSpider(scrapy.Spider):
    ''' create the Base Spider '''

    name = "google"
    url = 'https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=hello'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}


    def start_requests(self):
        ''' request using a POST HTTP request on url '''
        yield scrapy.Request(url=self.url, callback=self.extract, method='POST', headers=self.headers)

    
    def extract(self, response):
        ''' extracts the page data using XPATH selectors and recursively follows each page '''
        pass