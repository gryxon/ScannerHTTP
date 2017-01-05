import httplib
c = httplib.HTTPConnection('183.61.236.55:3128')
# Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0
headers = { 'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/5.00 (Nikto/2.1.5) (Evasions:None) (Test:Port Check)'}
c.request('HEAD', 'http://103.ip-137-74-193.eu:80/', '', headers)
