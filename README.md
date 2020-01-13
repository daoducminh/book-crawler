# Book Crawler Project

## Installation
1. Install Python 3
2. Install `pip`
3. Install `bs4` and `scrapy` from `pip`

## Running

> `scrapy crawl <SPIDER>`

For example: `scrapy crawl demo`

## Debugging

- If you're using PyCharm, please follow this steps:
  1. Open **Run > Edit Configuration**
  2. Add new configuration for Pure Python
  3. In **Configuration** tab, choose *Module name* and fill it with `scrapy.cmdline`
  4. Set parameters as your commands. For example: if you want to run: `scrapy crawl demo`, you will set it with:
     > crawl demo
  5. Set **Working Directory** as your project's root path.
  6. Save it and enjoys.