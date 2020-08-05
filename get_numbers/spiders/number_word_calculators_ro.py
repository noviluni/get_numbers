from urllib import parse

from scrapy import Request

from get_numbers.spiders import BaseNumberSpider


class NumberWordCalculatorsRoSpider(BaseNumberSpider):
    name = 'number-word.calculators.ro'
    allowed_domains = ['number-word.calculators.ro']
    supported_locales = ['en']  # add 'ro'? (`extract_number()` should be adapted)

    def crawl_numbers(self, start_number, max_number, locale):
        url = 'https://number-word.calculators.ro/convert-ordinal-numbers-to-English-text-words.php'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        cookies = {
            'calculators[lang]': locale,
        }

        for number in range(start_number, max_number + 1):
            query_params = {
                'rulare': '1',
                'ordinal_number': str(number),
                'submit': 'convert',
            }

            yield Request(
                url=url,
                method='POST',
                headers=headers,
                body=parse.urlencode(query_params),
                meta={'number': number},
                cookies=cookies,
            )

    def extract_number(self, response):
        return (
            response.css('.result')
            .xpath('h3[contains(text(), "lowercase")]/following::h4[1]/text()')
            .get()
        )
