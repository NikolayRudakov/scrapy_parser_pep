import scrapy, re
from scrapy.linkextractors import LinkExtractor
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):

        le = LinkExtractor(allow=("pep-"), deny="#", unique=True)
        for link in le.extract_links(response):
            yield response.follow(link.url, callback=self.parse_pep)

    def parse_pep(self, response):
        title = str(response.css("h1.page-title::text").get())
        number = int(re.search(r"\d+", title).group(0))
        name = re.split(r" – ", title)[1]
        status = response.xpath(
            '//dt[contains(., "Status")]/following-sibling::dd[1]//text()'
        ).get()
        yield PepParseItem({"number": number, "name": name, "status": status})
