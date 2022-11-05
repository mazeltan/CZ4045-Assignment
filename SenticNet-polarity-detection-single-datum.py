import requests, xlrd, xlwt

def getPolaritySenticNet(datum):
    LANG = 'en'
    APIKEY = 'jFz4p0loUTjnz'
    APIURL = 'https://sentic.net/api/' + LANG + '/' + APIKEY + '.py?text='

    text = str(datum)

    for c in [';' , '&', '#', '{', '}']: text = text.replace(c, ':')

    label = str(requests.get(APIURL + text).content)[2:-3]

    # print for debugging
    print("text" + text + "label:" + label)

    return label
