from bs4 import BeautifulSoup
import html5lib
from .api import redirectTwitterPage

html = redirectTwitterPage()
def scripts(html):
    print(html)
    if html:
        soup = BeautifulSoup(html, 'html5lib')
        print(soup.title)
    else:
        return None
