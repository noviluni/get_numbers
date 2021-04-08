from urllib import parse

from scrapy import Request

from get_numbers.spiders import BaseNumberSpider


class Tools4noobsComSpider(BaseNumberSpider):
    name = 'tools4noobs.com'
    allowed_domains = ['tools4noobs.com']
    supported_locales = [
        'bg',
        'cs',
        'de',
        'dk',
        'en_GB',
        'en_US',
        'es',
        'es_AR',
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
        'ru',
        'sv',
    ]

    def crawl_numbers(self, numbers, locale):
        url = 'https://www.tools4noobs.com/'

        headers = {
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://www.tools4noobs.com",
        }

        for number in numbers:

            query_params = {
                'action': 'ajax_number_spell_words',
                'number': str(number),
                'type': 0,
                'locale': locale,
            }

            yield Request(
                url=url,
                method='POST',
                headers=headers,
                body=parse.urlencode(query_params),
                meta={'number': number},
            )

    def extract_number(self, response):
        return response.css('::text').get()
