# python-selenium-news

This project uses [Selenium](https://www.seleniumhq.org/) to scrape articles from a Google News search for JavaScript.
I chose JavaScript over Python to avoid the disambiguation problems that arise when searching for Python.
The articles are then parsed and output to a markdown file using [Pandas](https://pandas.pydata.org/).

A GitHub action schedules the scraping to run every day and update the README.md file.
