from urllib import parse

from scrapy import Request

from get_numbers.spiders import BaseNumberSpider


class ClevertComBrSpider(BaseNumberSpider):
    name = 'clevert.com.br'
    allowed_domains = ['clevert.com.br']
    start_urls = ['http://clevert.com.br/']

    def crawl_numbers(self, start_number, max_number, locale):
        url = 'https://clevert.com.br/t/en/numbers_to_words/generate'

        headers = {
            # "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
            # "Accept": "*/*",
            # "Accept-Language": "ca,en-US;q=0.7,en;q=0.3",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            # "Origin": "https://clevert.com.br",
            # "Connection": "keep-alive",
            # "Referer": "https://clevert.com.br/t/en/numbers-to-words",
            # "Pragma": "no-cache",
            # "Cache-Control": "no-cache"
        }

        # cookies = {
        #     "ci_session": "r1iefqp2g4u0d704blfmiid77u6tfln3"
        # }

        for number in range(start_number, int(max_number) + 1):
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
