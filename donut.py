#!/usr/bin/env python

""" be you broadened """
from collections import namedtuple
import random
import sys
import urllib.request

Family = namedtuple("Family", "name count formalness")

def download_tsv(url):
    """ fetch spreadsheet """
    with urllib.request.urlopen(url) as response:
        data = response.read()
        text = data.decode("utf-8")
        return parse_tsv(text)


def read_local_tsv(path):
    """ fetch spreadsheet locally """
    with open(path, "r") as sheet:
        return parse_tsv(sheet.read())


def parse_tsv(text):
    """ parse tsv """
    return [Family(*r.split("\t")) for r in text.split("\n")]


def make_pick(people, count_requested, booked=[]):
    """ make picks """
    if count_requested < 1:
        return booked

    options = [p for p in people if p.name not in booked]
    if not options:
        return booked

    pick = random.choice(options)
    booked.append(pick.name)
    return make_pick(people, count_requested - int(pick.count), booked)


if __name__ == "__main__":
    formalness = 1
    count = 6
    if len(sys.argv) > 2:
        formalness = int(sys.argv[2])
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
    p = [p for p in read_local_tsv("people.tsv") if int(p.formalness) <= formalness]
    print(make_pick(p, count))
