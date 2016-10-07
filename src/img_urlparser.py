from urllib.parse import urlparse
from posixpath import basename, dirname

import re


def get_netloc(url):
    parse_object = urlparse(url)
    netloc = parse_object.netloc
    return str(netloc.replace('www.', ''))


def get_path(url):
    parse_object = urlparse(url)
    return str(parse_object.path)


def get_dirname(url):
    parse_object = urlparse(url)
    return dirname(parse_object.path)


def get_basename(url):
    parse_object = urlparse(url)
    return basename(parse_object.path)


def remove_eol_character(list_of_url):
    return list(map(lambda string: string.strip(), list_of_url))


def remove_empty_lines(list_of_url):
    filtered = filter(lambda x: not re.match(r'^\s*$', x), list_of_url)
    return list(filtered)


def remove_duplicates(list_of_url):
    seen = set()
    seen_add = seen.add
    list_of_urls_no_duplicates = [x for x in list_of_url if not (x in seen or seen_add(x))]
    return list_of_urls_no_duplicates
