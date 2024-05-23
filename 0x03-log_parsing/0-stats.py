#!/usr/bin/python3
"""Log parsing """


import sys


if __name__ == '__main__':
    file_sz = [0]
    statuscodes = {200: 0, 301: 0, 400: 0, 401: 0,
                   403: 0, 404: 0, 405: 0, 500: 0}

    def printstats():
        """ Print stat """
        print('File size: {}'.format(file_sz[0]))
        for key in sorted(statuscodes.keys()):
            if statuscodes[key]:
                print('{}: {}'.format(key, statuscodes[key]))

    def parseline(line):
        """ Checks the line for matche """
        try:
            line = line[:-1]
            word = line.split(' ')
            file_sz[0] += int(word[-1])
            stat = int(word[-2])
            if stat in statuscodes:
                statuscodes[stat] += 1
        except BaseException:
            pass

    lnum = 1
    try:
        for line in sys.stdin:
            parseline(line)
            """ print after every 10 lines """
            if lnum % 10 == 0:
                printstats()
            lnum += 1
    except KeyboardInterrupt:
        printstats()
        raise
    printstats()
