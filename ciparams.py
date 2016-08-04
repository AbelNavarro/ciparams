#!/usr/bin/python

import argparse
import urllib2
import ssl
import re
import string


def main():
    parser = argparse.ArgumentParser(description='ciparams - get build parameters from build number')
    parser.add_argument('build_number', type=int, help="Build number, i.e. 28945")
    args = parser.parse_args()

    print "build_number: {}".format(args.build_number)

    # Build parameters page
    url = "https://ci.suse.de/job/openstack-mkcloud/{}/parameters".format(args.build_number)
    print "url: " + url

    context = ssl._create_unverified_context()
    data = urllib2.urlopen(url, context=context)
    prevparam = 'cloudsource'
    for line in data:
        if not 'input readonly' in line:
            continue

        #print "line: " + line

        value = line.split('"')[5]
        elems = re.split('<|>', line)
        param = ''
        for elem in elems:
            cleanelem = re.sub('[ |\n]', '', filter(lambda x: x in set(string.printable), elem))
            if not cleanelem or re.match(r't.*|/t.*|input.*', cleanelem):
                continue

            param = cleanelem


        if value:
            print "export {}={}".format(prevparam, value)

        prevparam = param


if __name__ == '__main__':
    main()
