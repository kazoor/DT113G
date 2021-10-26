def formatNameFiled(url_in):
    byte_url = b''
    headers = (chr(23) + chr(117) + \
        chr(1) + chr(0) + \
        chr(0) + chr(1) + \
        chr(0) + chr(0) + \
        chr(0) + chr(0) + \
        chr(0) + chr(0)).encode('ascii')

    queries = (chr(0) \
        + chr(0) \
        + chr(1) \
        + chr(0) \
        + chr(1)).encode('ascii')

    for i in url_in.split("."):
        byte_url += (chr(len(i)) + i).encode('ascii')

    return headers + byte_url + queries


print(formatNameFiled("bbc.co.uk"))
print(formatNameFiled("facebook.com"))
print(formatNameFiled("mixteco.utm.mx"))
print(formatNameFiled("eluniversal.com.mx"))
