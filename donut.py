""" be you broadened """
from collections import namedtuple
import urllib.request

Family = namedtuple("Family", "name count formalness")

def download_tsv(url):
    """ fetch spreadsheet """
    with urllib.request.urlopen(url) as response:
        data = response.read()
        text = data.decode("utf-8")
        return text


def parse_tsv(text):
    """ parse tsv """
    return [Family(r.split("\t")) for r in text.split("\n")]

def make_pick(people, count_requested, booked):
    """ make picks """
    if not count_requested:
        return [f.name for f in booked]

    options = [p for p in people if p.name not in booked]
    pick = random.choice(options)
    booked.append(pick.name)
    return make_pick(people, count_requested - pick.count, booked)

if __name__ == "__main__":
    test_url = ""
    test_data = download_tsv(test_url)
    test_people = parse_tsv(test_data)
    print(make_pick(test_people, 6, []))
