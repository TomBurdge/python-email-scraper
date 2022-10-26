<h1>Python Email Scraper</h1>
A python file which uses selenium to scrape email adresses from sites in a list. Saves the scraped emails to a CSV called "emails".
<br/>
<br/>
When using the file, you need to add your list manually.<br/>
You could also modify the file to read the column of a csv quite easily with pandas. I often follow this process but have left it out for simplicity.

<h2>Requirements</h2>

You will need python installed.
In addition, you will need the following modules installed in your environment:
- Pandas
- Selenium
- Pyisemail
You can isntall all of these with pip.

<h2>Chrome Driver</h2>
This project has been built to run on Chrome version 106.0.5249.119 and Windows 
If you have an earlier version of chrome, you should update it.
If you have a later version of chrome, or a different operating system, you can clone this repository and add the appropriate chrome driver .exe for your version to the "drivers" folder.
If you need to change the chromedriver, you can find the appropriate chrome driver here:
https://chromedriver.chromium.org/downloads
