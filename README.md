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
<br/>
You can install all of these with pip.<br/><br/>
I've never had an issue, but it is a good idea to use a VPN when running these. This will ensure:<br/>
- Your regular IP doesn't get blocked by any site<br/>
- You have some protection from any malicious sites you may mistakenly add to the list
<br/><br/>
Make sure that the browser doesn't launch with you logged into any social medias which may block your account such as LinkedIn.
You can check this by running the first 28 lines and followed by: browser.open_page("RELEVANT SITE URL SUCH AS LINKEDIN")

<h2>Chrome Driver</h2>
This project has been built to run on Chrome version 106.0.5249.119 and Windows 
If you have an earlier version of chrome, you should update it.
If you have a later version of chrome, or a different operating system, you can clone this repository and add the appropriate chrome driver .exe for your version to the "drivers" folder.
If you need to change the chromedriver, you can find the appropriate chrome driver here:
https://chromedriver.chromium.org/downloads
