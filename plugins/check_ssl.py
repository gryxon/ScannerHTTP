import requests


def main(url):
    url = '137.74.193.103:8080'
    ssl_url = url.replace('http://', 'https://') if url.startswith('http://') else 'https://' + url
    try:
        requests.get(ssl_url)
    except Exception as e:
        if 'certificate verify failed' in str(e.message):
            print 'bad signed ssl'
        elif 'unknown protocol' in str(e.message):
            print 'no ssl certificate'
        else:
            print 'unknown error'

