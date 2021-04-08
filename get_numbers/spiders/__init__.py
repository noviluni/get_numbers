from scrapy import Spider

PERMUTATIONS = [
    1234,
    23451,
    345612,
    4567123,
    56781234,
    678912345,
    7890123456,
    89091234567,
    909812345678,
    987123456789,
    98761234567890,
    876512345678909,
    7654123456789098,
    65431234567890987,
    543212345678909876,
    4321123456789098765,
    32101234567890987654,
    210012345678909876543,
    1000123456789098765432,
    1234567890987654321,
    12345678909876543210,
    123456789098765432100,
    1234567890987654321000,
]


class BaseNumberSpider(Spider):
    def start_requests(self):
        if not hasattr(self, 'locale'):
            self.logger.error(f'Missing the `locale` parameter')
            return

        if hasattr(self, 'permutations'):
            numbers = PERMUTATIONS
        else:
            if not hasattr(self, 'max_number'):
                self.logger.error(f'Missing the `max_number` parameter')
                return

            if self.locale not in self.supported_locales:
                self.logger.error(f'"{self.locale}" is not a supported locale')
                return
            start_number = int(self.start_number) if hasattr(self, 'start_number') else 0
            numbers = list(range(start_number, int(self.max_number) + 1))

        yield from self.crawl_numbers(numbers, locale=self.locale)

    def parse(self, response, **kwargs):
        yield {
            'number': response.meta['number'],
            'text': self.extract_number(response),
        }

    def crawl_numbers(self, numbers, locale):
        raise NotImplementedError

    def extract_number(self, response):
        raise NotImplementedError
