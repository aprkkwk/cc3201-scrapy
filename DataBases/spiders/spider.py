import scrapy
from scrapy.exceptions import CloseSpider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from DataBases.items import DatabasesItem


class AnimeSpider(CrawlSpider):
    name = 'anime'
    allowed_domain = ['www.myanimelist.net']  # toda la info de este dominio
    start_urls = ['https://myanimelist.net/topanime.php']  # Donde empieza a scrapear

    rules = {
        Rule(LinkExtractor(allow=(), restrict_xpaths=
        ('//*[@id="content"]/div[3]/div/a'))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="di-ib clearfix"]/a[@class="hoverinfo_trigger fl-l fs14 fw-b"]')), callback='parse_item',
             follow=False)
    }


    def parse_item(self, response):
        ml_item = DatabasesItem()

        # info de Anime
        ml_item['Titulo'] = response.xpath('normalize-space(//*[@id="contentWrapper"]/div[1]/h1/span/text())').extract()
        ml_item['Titulo_Japones'] = response.xpath('normalize-space(//*[@id="content"]//div/div[8]/text())').extract()
        ml_item['Tipo'] = response.xpath('normalize-space(//*[@id="content"]//div/div[9]/a)').extract()

        return ml_item
