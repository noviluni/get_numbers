from urllib import parse

from scrapy import Request

from get_numbers.spiders import BaseNumberSpider


class ClevertComBrSpider(BaseNumberSpider):
    name = 'clevert.com.br'
    allowed_domains = ['clevert.com.br']
    supported_locales = [
        'af',
        'sq',
        'ar',
        'hy',
        'az',
        'be',
        'bg',
        'ca',
        'zh',
        'hr',
        'cs',
        'da',
        'nl',
        'en',
        'eo',
        'et',
        'mk',
        'fo',
        'fa',
        'fi',
        'fr',
        'ka',
        'de',
        'el',
        'he',
        'hi',
        'hu',
        'is',
        'id',
        'it',
        'ja',
        'ko',
        'lv',
        'lt',
        'ms',
        'mt',
        'nb',
        'nn',
        'pl',
        'pt-br',
        'ro',
        'ru',
        'sr',
        'sk',
        'sl',
        'es',
        'sv',
        'ta',
        'th',
        'tr',
        'uk',
        'vi',
        'cy',
    ]

    def crawl_numbers(self, numbers, locale):
        """Maximum allowed value:  2147483647.99"""
        url = 'https://clevert.com.br/t/en/numbers_to_words/generate'

        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
        }

        for number in numbers:
            query_params = {
                'number': str(number),
                'currency': '',
                'numLanguage': locale,
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
