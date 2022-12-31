import scrapy
from scrapy.linkextractors import LinkExtractor
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):

        le = LinkExtractor(allow=("pep-"), deny="#", unique=True)
        for link in le.extract_links(response):
            # print(link.url)
            yield response.follow(link.url, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css("h1.page-title::text").get()
        dash_position = str(title).find(" – ")
        number = int(title[4:dash_position])
        name = title[dash_position + 3 :]
        status = response.xpath(
            '//dt[contains(., "Status")]/following-sibling::dd[1]//text()'
        ).get()
        yield PepParseItem({"number": number, "name": name, "status": status})
