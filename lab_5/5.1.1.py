def formatNameFiled(url_in):
    byte_url = b''

    for i in url_in.split("."):
        byte_url += (chr(len(i)) + i).encode('ascii')

    return byte_url + chr(0).encode('ascii')


print(formatNameFiled("bbc.co.uk"))
print(formatNameFiled("facebook.com"))
print(formatNameFiled("mixteco.utm.mx"))
print(formatNameFiled("eluniversal.com.mx"))
