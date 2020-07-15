from scrapy import Spider


class BaseNumberSpider(Spider):
    def start_requests(self):
        if not hasattr(self, 'locale'):
            self.logger.error(f'Missing the `locale` parameter')
            return

        if not hasattr(self, 'max_number'):
            self.logger.error(f'Missing the `max_number` parameter')
            return

        if self.locale not in self.supported_locales:
            self.logger.error(f'"{self.locale}" is not a supported locale')
            return

        start_number = int(self.start_number) if hasattr(self, 'start_number') else 0

        yield from self.crawl_numbers(
            start_number, max_number=int(self.max_number), locale=self.locale
        )

    def parse(self, response):
        yield {
            'number': response.meta['number'],
            'text': self.extract_number(response),
        }

    def crawl_numbers(self, start_number, max_number, locale):
        raise NotImplementedError

    def extract_number(self, response):
        raise NotImplementedError
