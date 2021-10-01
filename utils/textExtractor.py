import time
import urllib.request
import urllib.parse
from w3lib.url import safe_url_string

import html2text

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'


def findTitle(html):
    str_html = str(html)
    title = str_html.split('<title>')[1].split('</title>')[0] if 'title' in str_html else 'not title was found'
    return title

def get_all_text_from_url(url, retries = 5):
    if retries == 0:
        raise Exception("could not handle request")
    try:
        url_utf_8 = safe_url_string(url)
        headers = {'User-Agent': USER_AGENT}
        request = urllib.request.Request(url_utf_8, None, headers)

        response = urllib.request.urlopen(request)
        given_encoding = response.headers.get_content_charset()
        encoding = 'utf-8' if given_encoding is None else given_encoding
        html = response.read().decode(encoding)



        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        title = findTitle(html)
        allText = h.handle(html)

        return allText, title
    except Exception as exc:
        if retries > 0:
            print("an exception occurred while trying to access url {} trying again \n more details: {}"
                  .format(url, exc))
            time.sleep(1)
            retries = retries - 1
            return get_all_text_from_url(url, retries)
        else:
            raise
