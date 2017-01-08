def ssl_scan(url):
    """
    Method which change url to ssl url (https).

    :param url: Main url of scanned Website.
    :return: Link with changed Url (http to https)
    """
    if url.startswith('http://'):
        return url.replace('http://', 'https://')
    return 'https://' + url