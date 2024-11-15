from urllib.request import urlopen
url = 'https://t.me/Creativising_lis/1638'
page = urlopen(url)
print(page.read().decode('utf-8'))
