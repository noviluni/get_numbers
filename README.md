# Get numbers

Scraping number conversion tools.

To use it:

```bash
crawl tools4noobs.com -a max_number=100 -a locale=en_US -o numbers_en_US.csv
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