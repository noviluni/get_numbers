# Get numbers

Scraping number conversion tools.

To use it:

```bash
scrapy crawl tools4noobs.com -a max_number=100 -a locale=en_US -o numbers_en_US.csv
```

or

```bash
scrapy crawl clevert.com.br -a max_number=100 -a locale=es -o numbers_es.csv
```

You can set the `max_number` to reach, the desired `locale` and the name of the result file. You can also add an optional `start_number` parameter.

The produced CSV file can be sorted by using the `sort_csv` function. Example:

```python
from get_numbers.utils import sort_csv

sort_csv('numbers_en_US.csv')
```

The content can also be checked by using the `check_missing_numbers` function. Example:

```python
from get_numbers.utils import check_missing_numbers

check_missing_numbers('numbers_en_US.csv', max_number=100)
```

You can also get the permutations files by running something similar to:
```bash
scrapy crawl japanesenumberconverter.com -a permutations=1 -a locale=ja -o numbers_ja2.csv
```
