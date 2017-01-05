def ssl_scan(url):
    if url.startswith('http://'):
        return url.replace('http://', 'https://')
    return 'https://' + url
