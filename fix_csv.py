#! /usr/bin/env python

import csv
import argparse
import string


parser = argparse.ArgumentParser(description="Standarize CSV file")
parser.add_argument("--in-quote", help="Input quote character")
parser.add_argument("--in-delimiter", help="Input delimiter character")
parser.add_argument("infile", help="Input filename", type=argparse.FileType('r'))
parser.add_argument("outfile", help="Output filename", type=argparse.FileType('w'))

args = parser.parse_args()
guess = { 'delimiter': None, 'quote': None }

if args.in_delimiter:
    guess['delimiter'] = args.in_delimiter

if args.in_quote:
    guess['quote'] = args.in_quote


def guess_tokens():
    with (open(args.infile.name, 'r')) as csvfile:
        line = csvfile.readline()

    if (guess['quote'] is None) and (line[0] in string.punctuation):
        guess['quote'] = line[0]
    else:
        guess['quote'] = '"'

    if guess['delimiter'] is None:
        delimiter = [character for character in line
                     if (character in string.punctuation or character in string.whitespace) and character is not guess['quote']]
        guess['delimiter'] = delimiter[0]

if guess['delimiter'] is None or guess['quote'] is None:
    guess_tokens()
with open(args.outfile.name, 'w') as csvoutput:
    with open(args.infile.name, 'r') as csvinput:
        csvreader = csv.reader(csvinput, delimiter=guess['delimiter'], quotechar=guess['quote'])
        csvwriter = csv.writer(csvoutput, delimiter=',', quotechar='"')
        for row in csvreader:
            csvwriter.writerow(row)





