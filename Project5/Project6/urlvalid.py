import validators

url_link = input("Paste your URL link here: ")

if validators.url == url_link:
    print('URL is valid')

else:
    print('Not valid')
