# Justdial-Scrapping
I scrapped Justdial website for educational purpose using Scrapy bot  

There were restriction but to bypass them i tried three methods.


I used Google user-agent, then I used scrapy user agents and at last used Proxies.
The scrapy user agents worked fine for me, to bypass the restrictions in Justdial website.

Collecting Phone numbers was the most tricky part, I had to extract each digit of the number and then decode it through the attributes which were assigned to each number.

At last, all went well and you can see the results in the data.json file.


