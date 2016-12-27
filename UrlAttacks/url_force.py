import requests
from itertools import product


def main(url, start, stop, large=False):
    for sets_num in xrange(start, stop + 1):
        letters_range = (range(65, 91) if large else []) + range(97, 123)
        letters = ''.join([chr(x) for x in letters_range])
        products = product(letters, repeat=sets_num)
        for subdir in products:
            subdir = '/' + ''.join(subdir) + '/'
            attacked_url = url + subdir
            response = requests.get(attacked_url)
            print response.status_code, subdir

if __name__ == '__main__':
    main('http://137.74.193.103', 2, 2, True)
