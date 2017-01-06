import requests


def main(dict_name, url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}
    r = requests.get(url + '/robots.txt', headers=headers)
    robots_urls = False
    robots_lines = []
    if r.status_code == 200:
        for line in r.text.split('\n'):
            line = line.lower()
            if robots_urls and 'disallow' in line:
                robots_lines.append(line.split(' ')[1].replace('*', ''))
            else:
                robots_urls = 'user-agent' in line

    for attacked_line in robots_lines:
        response = requests.get(url + attacked_line)
        print response.status_code, attacked_line.replace('\n', '')

    if requests.get(url + '/phpinfo.php').status_code == 200:
        print 'Znaleziono phpinfo.php !!!'

    with open(dict_name) as url_dict:
        line = url_dict.readline()
        while line != '':
            attacked_url = url + line.replace('\n', '')
            response = requests.get(attacked_url)
            print response.status_code, line.replace('\n', '')
            line = url_dict.readline()

if __name__ == '__main__':
    main('dict', "http://192.168.209.131")