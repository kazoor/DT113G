import sys


def parseMessage(inputString):
    # Since every row basically contains a key and a value we could easily split every line
    # and then split at every : because then we could simply put the key and value in the field
    # into a dictionairy.

    # Split the string at every newline
    rows = inputString.split("\r\n")

    # Manually take out request type and protocol version.
    protocol = rows[0].split(" ")

    # Make sure to remove unecessary parts like the request type "GET"
    # since we have already parsed the line containing this data and it wont work in a dictionairy.
    rows = rows[1:]

    # Create the dictionairy.
    data = {}

    # Loop through all the rows and split at : to get a key and its value
    # and then insert it into the data dictionairy.
    for row in rows:
        if not row:
            continue
        key, val = row.split(":")
        data[key] = val

    # Print out a formatted string with all the values.
    return f'("{protocol[1]}", "{data["User-Agent"].replace(" ", "")}", "{protocol[2]}", "{data["Accept-Language"].replace(" ", "")}")'


def main():
    string1 = 'GET /index.html HTTP/1.1\r\nHost: www-net.cs.umass.edu\r\nUser-Agent: Firefox\r\nAccept: text/html,application/xhtml+xml\r\nAccept-Language: en-us\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7\r\nKeep-Alive: 115\r\nConnection: keep-alive\r\n'

    function_output = parseMessage(string1)

    # Here you will print:
    # the requested_resource,
    # the client’s_browser
    # the HTTP version
    # the language
    print(function_output)


main()
