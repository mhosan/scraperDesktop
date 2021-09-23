import requests
import lxml.html as html
import sys

original_stdout = sys.stdout

HOME_URL = 'https://www.larepublica.co/'
HOME_URL2 = 'https://www.clarin.com/'
#XPATH_LINK_TO_ARTICLE = '//h2[@data-h="17"]/a/@href'
XPATH_LINK_TO_ARTICLE = '//text-fill[not(@class)]/a/@href'
XPATH_LINK_TO_ARTICLE2 = '//article[@class="content-nota list-format twoxone_no_foto"]/a[@class="link_article"]/@href'
XPATH_TITLE = '//h2[@data-h="45"]/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p/text()'

#def parse_home():
try:
    response = requests.get(HOME_URL)
    if response.status_code == 200:
        home = response.content.decode('utf-8')
        with open ('prueba.txt', 'w') as f:
            sys.stdout = f
            print(home)
            sys.stdout = original_stdout
        parsed = html.fromstring(home)
        links_to_notices = parsed.xpath('//text-fill')
        print (links_to_notices)
        print (len(links_to_notices))
    else:
        raise ValueError(f'Error: {response.status_code}')
except ValueError as ve:
    print(ve)

#def run():
#    parse_home()

#if __name__ == __main__:
#    run()

