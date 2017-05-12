from lxml import html
import requests

# Send request to get the web page
response = requests.get('https://news.google.com/news/section?cf=all&pz=1&topic=b&siidp=b458d5455b7379bd8193a061024cd11baa97&ict=ln')

# Check if the request succeeded (response code 200)
if (response.status_code == 200):

# Parse the html from the webpage
	pagehtml = html.fromstring(response.text)

# search for news headlines
news = pagehtml.xpath('//h2[@class="esc-lead-article-title"] \
                      /a/span[@class="titletext"]/text()')

# Print each news item in a new line
#print("\n \n".join(news))

tf = open("news.txt", "w")

tf.write("\n".join(news).lower())

tf.close()
# puts as lower case in text file named headlines

