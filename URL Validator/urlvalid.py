import validators

#Input your link to check if it's valid or not
url_link = input("Paste your URL link here: ")


if validators.url(url_link):
    print('This URL is valid')

else:
    print('Not valid')
