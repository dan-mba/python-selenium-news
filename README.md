# python-selenium-news

This project uses [Selenium](https://www.seleniumhq.org/) to scrape articles from a Google News search for JavaScript.
I chose JavaScript over Python to avoid the disambiguation problems that arise when searching for Python.
The articles are then parsed and output to a markdown file using [Pandas](https://pandas.pydata.org/).

A GitHub action schedules the scraping to run every day and update the README.md file.
\n$(date +%A %B %d %Y)\n\n
| Title                                                             | Website          | Link                                                                                                                                               |
|:------------------------------------------------------------------|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| New JavaScript runtime Bun challenges Deno, Node.js               | TechTarget       | https://www.techtarget.com/searchsoftwarequality/news/252522622/New-JavaScript-runtime-Bun-challenges-Deno-Nodejs                                  |
| ES6 Object Destructuring and JavaScript  HTMLGoodies.com          | HTML Goodies     | https://www.htmlgoodies.com/javascript/es6-destructuring-javascript/                                                                               |
| 8 new JavaScript features to start using today                    | InfoWorld        | https://www.infoworld.com/article/3665748/8-new-javascript-features-to-start-using-today.html                                                      |
| A New Javascript Runtime Fresh Out Of The Oven                    | Hackaday         | https://hackaday.com/2022/07/08/a-new-javascript-runtime-fresh-out-of-the-oven/                                                                    |
| Stripe Migrated Its Largest JavaScript Codebase to TypeScript     | Business Insider | https://www.businessinsider.com/stripe-migrated-its-largest-javascript-codebase-to-typescript-2022-7                                               |
| Zig-based Bun appears in beta: 'An incredibly fast all-in-one ... | DevClass         | https://devclass.com/2022/07/06/zig-based-bun-appears-in-beta-an-incredibly-fast-all-in-one-javascript-runtime/                                    |
| How To Enable Or Disable JavaScript On Browser?                   | Tech News Today  | https://www.technewstoday.com/how-to-enable-disable-javascript/                                                                                    |
| 'IconBurst' supply chain attack uses typo-squatting to spread ... | SC Magazine      | https://www.scmagazine.com/news/third-party-risk/iconburst-supply-chain-attack-uses-typo-squatting-to-spread-malicious-javascript-packages-via-npm |
| JavaScript does the job                                           | Gadget           | https://gadget.co.za/javascript-does-the-job/                                                                                                      |
| Recreate a Simple Pokemon Game With 70 Lines of Javascript        | HackerNoon       | https://hackernoon.com/recreate-a-simple-pokemon-game-with-70-lines-of-javascript                                                                  |