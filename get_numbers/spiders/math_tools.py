from urllib import parse

from scrapy import Request

from get_numbers.spiders import BaseNumberSpider


class MathToolsSpider(BaseNumberSpider):
    """
    It seems that it's using the same base library than tools4noobs.com but extended,
    as it support all the locales in that other website adding some extra locales.
    Then names of the locales are the same. However, this website doesn't support "zero"
    and the responses are capitalized.
    """

    name = 'math.tools'
    allowed_domains = ['math.tools']
    supported_locales = [
        'bg',
        'cs',
        'de',
        'dk',
        'en_GB',
        'en_IN',
        'en_US',
        'es',
        'es_AR',
        'es_MX',
        'es_VE',
        'et',
        'fr',
        'fr_BE',
        'he',
        'hu_HU',
        'id',
        'it_IT',
        'lt',
        'nl',
        'pl',
        'pt_BR',
        'ro_RO',
        'ru',
        'sv',
        'tr_TR',
        'ua',
    ]

    def crawl_numbers(self, numbers, locale):
        url = 'https://math.tools/calculator/numbers/words'

        headers = {
            # "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            # "Content-Type": "application/x-www-form-urlencoded",
            # "X-Requested-With": "XMLHttpRequest",
        }

        for number in numbers:
            query_params = {'number': str(number), 'lang': locale, 'result': ' '}

            yield Request(
                url=url,
                method='POST',
                headers=headers,
                body=parse.urlencode(query_params),
                meta={'number': number},
            )

    def extract_number(self, response):
        return response.css('#result::text').get(default='').strip()
