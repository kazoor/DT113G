def formatNameFiled(url_in):
    byte_url = b''
    headers = chr(23).encode('ascii') + chr(117).encode('ascii') + \
        chr(1).encode('ascii') + chr(0).encode('ascii') + \
        chr(0).encode('ascii') + chr(1).encode('ascii') + \
        chr(0).encode('ascii') + chr(0).encode('ascii') + \
        chr(0).encode('ascii') + chr(0).encode('ascii') + \
        chr(0).encode('ascii') + chr(0).encode('ascii')

    queries = chr(0).encode('ascii') \
        + chr(0).encode('ascii') \
        + chr(1).encode('ascii') \
        + chr(0).encode('ascii') \
        + chr(1).encode('ascii')

    for i in url_in.split("."):
        byte_url += chr(len(i)).encode('ascii') + \
            i.encode('ascii')

    return headers + byte_url + queries


print(formatNameFiled("bbc.co.uk"))
print(formatNameFiled("facebook.com"))
print(formatNameFiled("mixteco.utm.mx"))
print(formatNameFiled("eluniversal.com.mx"))
