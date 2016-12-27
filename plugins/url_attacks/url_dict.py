import requests


def main(dict_name, url):
    with open(dict_name) as url_dict:
        line = url_dict.readline()
        while line != '':
            attacked_url = url + line.replace('\n', '')
            response = requests.get(attacked_url)
            print response.status_code, line.replace('\n', '')
            line = url_dict.readline()

if __name__ == '__main__':
    main('dict', "http://137.74.193.103")