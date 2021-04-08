import re
from urllib import parse

from scrapy import Request

from get_numbers.spiders import BaseNumberSpider


class JapaneseNumberConverterSpider(BaseNumberSpider):
    name = 'japanesenumberconverter.com'
    allowed_domains = ['japanesenumberconverter.com']
    supported_locales = ['ja']

    def crawl_numbers(self, numbers, locale):
        url = 'https://japanesenumberconverter.com/converter/'

        for number in numbers:
            query_params = {'convert_number': str(number)}
            print(query_params)
            yield Request(
                url=url,
                method='POST',
                body=parse.urlencode(query_params),
                meta={'number': number},
                headers={
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                },
            )

    def extract_number(self, response):
        return re.findall(r'Kanji: (.*)', response.json().get('kanji'))[0]
