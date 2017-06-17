HERE is a StackOverflow Question pertaining to our WebScraper asked on June 17, 2017 (answered). 


ANSWERED: WHY IS get.requests RETURNING PC INFO RATHER THAN XBOX INFO?

Q: I expected the results from setting the platform to xbox to be returned, instead, the results from the default platform, PC, are returned. I.E if i were to go to rl-trades.com instead of rl-trades.com/#pf=xbox – Tyler Albee 15 mins ago   
  	 	
A: That page uses Javascript to load the table. Open up your browser dev tools, switch to the network tab and changed the 'platform' option. Observe that https://www.rl-trades.com/?ajax=trades&pf=xbox&tk=6mopqedt1f‌​&_=1497707376134 is loaded for the XBox option. – Martijn Pieters
  	 	
The URL query fragment is just there to aid bookmarks, but doesn't affect how the page is served from the server. – Martijn Pieters

https://stackoverflow.com/questions/44605244/python3-requests-get-ignoring-part-of-my-url-beautifulsoup-python-webscraping
