#!/usr/bin/python

import argparse


def main():
    parser = argparse.ArgumentParser(description='ciparams - get build parameters from build number')
    parser.add_argument('build_number', type=int, help="Build number, i.e. 28945")
    args = parser.parse_args()

    print "build_number: {}".format(args.build_number)

if __name__ == '__main__':
    main()
